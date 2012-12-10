<h1>GeonamesPy</h1>

<h3>Python module for querying data dumps of www.geonames.org</h3>

You can find more information here: http://download.geonames.org/export/dump/

<h4>Usage</h4>

    from Geonames import Geonames
    api = Geonames()

<h5>Getting all features of a country</h5>
Get array of dicts of all features for Bavaria. Each dict has the keys listed below.

    data_rows = api.get_features_dump('BV') 

data_rows looks like this:

    [{'elevation': None, 'name': u'Williams Reef', 'modification_date': u'2012-01-18', 'geonameid': 3371096, 'feature_class': u'H', 'admin3_code': None, 'admin2_code': None, 'longitude': 3.4183300000000001, 'cc2': None, 'timezone': u'Europe/Oslo', 'latitude': -54.448610000000002, 'feature_code': u'RF', 'dem': 232, 'country_code': u'BV', 'admin1_code': u'00', 'alternatenames': u'Williams Reef,Williamsrevet', 'asciiname': u'Williams Reef', 'admin4_code': None, 'population': 0}, ...]


<h5>Getting all features of all countries</h5>

    data_rows = api.get_features_dump(country_code=None)

<h5>Filtering columns</h5>
Now get only name, latitude, and longitude for all Bavarian features:

    data_rows = api.get_features_dump('BV', columns=['name', 'latitude', 'longitude'])

data_rows now looks like this:

    [{'latitude': -54.448610000000002, 'name': u'Williams Reef', 'longitude': 3.4183300000000001}, ...]
    
<h5>Filtering features</h5>
Get lakes in Bavaria (their feature codes have LK in them - see http://download.geonames.org/export/dump/featureCodes_en.txt):

    data_rows = api.get_features_dump('BV', feature_code_filters='LK')
    
Get names of military bases, business centers, and housing developments in Bavaria:

    data_rows = api.get_features_dump('BV', columns=['name'], feature_code_filters=['MILB', 'CTRB', 'DEVH'])
    
<h5>Getting only cities</h5>
Get only cities in Bavaria:

    data_rows = api.get_all_cities('BV')

<h5>Allowed columns and returned keys</h5>
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
