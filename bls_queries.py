from subscripts import bls_api_query_app as BLS

BLS_API_KEY = '5d111c391937452b82d6878bbb76783c'

# A year has many consumer demographics
# A consumer demographic has many expenditures
# An expenditure belongs to a consumer demographic
# A consumer demographic belongs to a year

def get_bls_row(query_code):
    df = BLS.get_series([query_code], 2003, 2017, BLS_API_KEY)
    years = [year.year for year in df.axes[0]]
    values = [year[0] for year in df.values]
    return(list(zip(years,values)))

query_code = 'CXUHOUSINGLB0806M' # Post-Tax income, non-mortgage homeowners
print(get_bls_row(query_code))