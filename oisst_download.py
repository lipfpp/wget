
oisst_data= open ('/..../list_oisst.txt', 'w+')

start_year=1981
end_year=2021

for i in range(start_year, end_year+1):
     oisst_data.write('ftp://ftp2.psl.noaa.gov/Datasets/noaa.oisst.v2.highres/sst.day.mean.' + str(i) + '.nc\n')
oisst_data.close()

!wget -i /..../list_oisst.txt
