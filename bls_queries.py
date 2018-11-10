from subscripts import bls_api_query_app as BLS

BLS_API_KEY = '5d111c391937452b82d6878bbb76783c'

# Show avg expenditure on rent in urban vs rural areas
s1 = 'CXURNTDWELLLB0806M' # urban
s2 = 'CXURNTDWELLLB0809M' # rural
series = BLS.get_series([s1, s2], 1980, 2017, BLS_API_KEY)