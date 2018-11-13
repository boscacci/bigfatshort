import csv

countries = []

def get_usa_gdp_per_cap():
    with open('global_GDPs.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
        for row in spamreader:
            countries.append(row)

    years = list(range(1960,2018))
    usa_gdp_pc = ((countries[254][4:][0][24:-2].split('","')))

    cleaned_gdps = list(zip(years,usa_gdp_pc))

    return dict(cleaned_gdps[-16:-5])
