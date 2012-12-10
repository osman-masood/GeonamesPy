# -*- coding: utf-8 -*-

import zipfile
import urllib2
import StringIO
import csv
import codecs

#
#class UTF8Recoder:
#    """
#    Iterator that reads an encoded stream and reencodes the input to UTF-8
#    """
#    def __init__(self, f, encoding):
#        self.reader = codecs.getreader(encoding)(f)
#
#    def __iter__(self):
#        return self
#
#    def next(self):
#        return self.reader.next().encode("utf-8")
#
#class UnicodeReader:
#    """
#    A CSV reader which will iterate over lines in the CSV file "f",
#    which is encoded in the given encoding.
#    """
#
#    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
#        f = UTF8Recoder(f, encoding)
#        self.reader = csv.reader(f, dialect=dialect, **kwds)
#
#    def next(self):
#        row = self.reader.next()
#        return [unicode(s, "utf-8") for s in row]
#
#    def __iter__(self):
#        return self


class Geonames():
    def __init__(self):
        self._base_url = "http://download.geonames.org/export/dump/"
        # _columns must be in the same order as in the data file
        self._columns = ['geonameid', 'name', 'asciiname', 'alternatenames', 'latitude', 'longitude', 'feature_class', 'feature_code',
                         'country_code', 'cc2', 'admin1_code', 'admin2_code', 'admin3_code', 'admin4_code', 'population',
                         'elevation', 'dem', 'timezone', 'modification_date']

        self._column_to_index = dict()
        for index, column_name in enumerate(self._columns):
            self._column_to_index[column_name] = index

    def get_all_cities(self, country_code="US", columns=[]):
        return self.get_features_dump(country_code=country_code, columns=columns, feature_code_filters='PPL')

    # country_code = None gets all country data. columns are the required columns, [] is all countries
    # feature_code_filters is array of feature codes, or empty is all: http://download.geonames.org/export/dump/featureCodes_en.txt
    # if feature_code_filters is string, will match all feature codes with it as a substring, i.e. "PPL" will get "PPLA", "PPLA2", etc.
    def get_features_dump(self, country_code="US", columns=[], feature_code_filters=[]):
        country_code = country_code.upper()
        # Query URL
        url = "%s%s.zip" % (self._base_url, country_code) if country_code else "allCountries.zip"
        response = urllib2.urlopen(url)
        zipped_data = response.read()

        # Write .zip data to temporary file
        output_file = StringIO.StringIO()
        output_file.write(zipped_data)

        # Unzip file and store data files in array
        zfobj = zipfile.ZipFile(output_file)
        #unzipped_file_array = []
        unzipped_files = []
        for name in zfobj.namelist():
            # print "name in zfobj", name
            if "readme" not in name:
                #unzipped_file = StringIO.StringIO()
                filename = "%s.txt" % country_code
                # print "filename", filename
                read_data = zfobj.read(filename)
                # print read_data
                unzipped_files.append(read_data)
                #unzipped_file.write(read_data)
                #unzipped_file_array.append(unzipped_file)
        zfobj.close()
        output_file.close()

        # Get data rows from the extracted file(s)
        if not columns: columns = self._columns

        data_rows = []
        for unzipped_file in unzipped_files:
            rows = unzipped_file.split('\n')
            for row in rows:
                input_columns = row.split('\t')
                if input_columns and len(input_columns) >= len(columns):
                    # Filter by feature code filters, if given. Can be string or array
                    if not feature_code_filters:
                        pass
                    else:
                        feature_code_filters_is_string = isinstance(feature_code_filters, basestring)
                        input_feature_code = input_columns[self._column_to_index['feature_code']]
                        if not feature_code_filters_is_string and (input_feature_code in feature_code_filters):
                            pass
                        elif feature_code_filters_is_string and (feature_code_filters in input_feature_code):
                            pass
                        else:
                            continue
                    data_dict = dict()
                    for column_name in columns:
                        data_dict[column_name] = input_columns[self._column_to_index[column_name]]
                        # Format value
                        if not data_dict[column_name]:
                            data_dict[column_name] = None
                        elif column_name in ('latitude', 'longitude'):
                            data_dict[column_name] = float(data_dict[column_name])
                        elif column_name in ('geonameid', 'elevation', 'dem', 'population'):
                            data_dict[column_name] = int(data_dict[column_name])
                        else:
                            data_dict[column_name] = data_dict[column_name].decode('utf-8')
                    data_rows.append(data_dict)

#        # Aggregate all rows into single array of dicts
#        data_rows = []
#        for unzipped_file in unzipped_file_array:
#
#            print "unzipped file", unzipped_file
#            if not columns: # If they want all columns, just use DictReader
#                csv_reader = csv.DictReader(unzipped_file, fieldnames=self._columns, dialect='excel', delimiter="\t")
#                print "csv reader", csv_reader
#                for row_as_dict in csv_reader:
#                    print "row as dict", row_as_dict
#                    data_rows.append(row_as_dict)
#
#            else: # Otherwise, only get the desired columns with normal reader
#                csv_reader = UnicodeReader(unzipped_file, delimiter='\t')
#                #csv_reader = csv.reader(unzipped_file, delimiter='\t', quoting=csv.QUOTE_NONE)
#                print "csv reader", csv_reader
#                print "first", csv_reader.next()
#                for row in csv_reader:
#                    print "row", row
#                    data_dict = dict()
#                    for column_name in columns: data_dict[column_name] = row[self._column_to_index(column_name)]
#                    data_rows.append(data_dict)
#                    print "data dict", data_dict
#
#            # Close unzipped file obj
#            unzipped_file.close()

        return data_rows
