gengos = [
    ('令和', 2019),
    ('平成', 1989),
    ('昭和', 1926),
    ('大正', 1912),
    ('明治', 1868),
]

def gengo(year):
    if year < 1869 or year > 2020:
        return 'Unknown'

    for name, base_year in gengos:
        if year >= base_year:
            return f'{name}{year - base_year + 1}年'

for year in range(1868, 2022):
    print(f'{year}: {gengo(year)}')
