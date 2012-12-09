<h1>GeonamesPy</h1>

<h3>Python module for querying www.geonames.org</h3>

<h4>Usage</h4>

    from Geonames import Geonames
    api = Geonames()
    
    # Get array of dicts for Bavaria. Each dict has the keys listed below.
    data_rows = api.get_country_data('BV') 
    # data_rows:
    # [{'elevation': None, 'name': u'Williams Reef', 'modification_date': u'2012-01-18', 'geonameid': 3371096, 'feature_class': u'H', 'admin3_code': None, 'admin2_code': None, 'longitude': 3.4183300000000001, 'cc2': None, 'timezone': u'Europe/Oslo', 'latitude': -54.448610000000002, 'feature_code': u'RF', 'dem': 232, 'country_code': u'BV', 'admin1_code': u'00', 'alternatenames': u'Williams Reef,Williamsrevet', 'asciiname': u'Williams Reef', 'admin4_code': None, 'population': 0}, ...]

    # Now get only name, latitude, and longitude for Bavarian cities
    data_rows = api.get_country_data('PK', columns=['name', 'latitude', 'longitude'])
    # data_rows:
    # [{'latitude': -54.448610000000002, 'name': u'Williams Reef', 'longitude': 3.4183300000000001}, ...]
    
The keys in the returned dicts, and the allowed values in the columns array are: 
['geonameid', 'name', 'asciiname', 'alternatenames', 'latitude', 'longitude', 'feature_class', 'feature_code', 'country_code', 'cc2', 'admin1_code', 'admin2_code', 'admin3_code', 'admin4_code', 'population', 'elevation', 'dem', 'timezone', 'modification_date']
These correspond to the columns listed at: http://download.geonames.org/export/dump/

If you experience any issues, let me know...

<h4>License</h4>
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
