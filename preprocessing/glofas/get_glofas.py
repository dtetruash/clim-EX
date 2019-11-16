import cdsapi

c = cdsapi.Client()

for year in range(1979, 2020):
    c.retrieve(
        'cems-glofas-historical',
        {
            'format':'zip',
            'dataset':'Consolidated reanalysis',
            'variable':'River discharge',
            'version':'2.1',
            'year':[str(year)],
            'month':[
                '01','02','03',
                '04','05','06',
                '07','08','09',
                '10','11','12'
            ],
            'day':[
                '01','02','03',
                '04','05','06',
                '07','08','09',
                '10','11','12',
                '13','14','15',
                '16','17','18',
                '19','20','21',
                '22','23','24',
                '25','26','27',
                '28','29','30',
                '31'
            ]
        },
        f'GLOFAS_{year}.zip')
