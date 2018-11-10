from subscripts import bls_api_query_app as BLS

BLS_API_KEY = '5d111c391937452b82d6878bbb76783c'

series = BLS.get_series(['CUUR0000SA0L1E'], 2000, 2015, BLS_API_KEY)