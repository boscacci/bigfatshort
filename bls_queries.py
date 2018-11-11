from subscripts import bls_api_query_app as BLS

BLS_API_KEY = '5d111c391937452b82d6878bbb76783c'

# Show avg expenditures in urban vs rural areas

s1 = 'CXURNTDWELLLB0806M' # avg spending on rent: urban renters
s2 = 'CXURNTDWELLLB0809M' # avg spending on rent: rural renters
s3 = 'CXUTRANSLB0806M' # avg spending on transpo: urban renters
s4 = 'CXUTRANSLB0809M' # avg spending on transpo: rural renters

series = BLS.get_series([s3, s4], 1980, 2017, BLS_API_KEY)
