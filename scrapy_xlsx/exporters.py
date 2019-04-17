from openpyxl import Workbook
from openpyxl.cell.cell import KNOWN_TYPES
from scrapy.exporters import BaseItemExporter


class XlsxItemExporter(BaseItemExporter):
    """XlsxItemExporter allows exporting the output items to a XLSX file."""

    def __init__(self, file, include_header_row=True, join_multivalued=',',
                 default_value=None, **kwargs):
        self._configure(kwargs, dont_fail=True)

        self.file = file
        self.include_header_row = include_header_row
        self._join_multivalued = join_multivalued
        self.default_value = default_value
        self._headers_not_written = True

        self.workbook = Workbook(write_only=True)
        self.sheet = self.workbook.create_sheet()

    def serialize_field(self, field, name, value):
        serializer = field.get('serializer', self._default_serializer)
        return serializer(value)

    def _default_serializer(self, value):
        """
        Provide a valid XLSX serialization for value.

        This method serializes the item fields trying to respect their type.
        Strings, numbers, booleans and dates are handled by openpyxl and they
        should appear with proper formatting in the output file. Lists and
        tuples of strings are converted into a single string when possible.
        Complex types like dict or set do not have a proper representation in
        XLSX format so they will just be converted into a string. You can
        override this method to provide a custom serialization, like a JSON
        representation using json.dumps(). Individual scrapy.Item fields can
        provide a custom serializer too:
            my_field = Field(serializer=custom_serializer)
        """
        # Do not modify values supported by openpyxl.
        if isinstance(value, KNOWN_TYPES):
            return value

        # Convert lists and tuples of strings into a single string.
        if self._join_multivalued is not None and \
                isinstance(value, (list, tuple)):
            try:
                return self._join_multivalued.join(value)
            except TypeError:
                pass

        # Convert complex types like dict into a string as fallback mechanism.
        return str(value)

    def export_item(self, item):
        if self._headers_not_written:
            self._headers_not_written = False
            self._write_headers_and_set_fields_to_export(item)

        fields = self._get_serialized_fields(item,
                                             default_value=self.default_value,
                                             include_empty=True)
        values = list(value for _, value in fields)
        self.sheet.append(values)

    def finish_exporting(self):
        # XXX: ideally, Scrapy would pass the filename and let the exporter
        # create the output file, however, it passes a file object already
        # open in "append" mode, so this method ignores this file object and
        # only uses it to retrieve the filename.
        self.workbook.save(self.file.name)

    def _write_headers_and_set_fields_to_export(self, item):
        """
        Write the header row using the field names of the first item.

        This method writes the header row using the field names of the first
        exported item. This works fine with scrapy.Item objects because they
        provide a formal schema definition, but you need to be careful when
        using dictionaries that may omit some fields. It is recommended to
        set fields_to_export when using dictionaries to avoid omitting fields
        accidentally.
        """
        if self.fields_to_export is None:
            if isinstance(item, dict):
                self.fields_to_export = list(item.keys())
            else:
                self.fields_to_export = list(item.fields.keys())

        if self.include_header_row:
            row = list(self.fields_to_export)
            self.sheet.append(row)
