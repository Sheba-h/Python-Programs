#program to find date from a string and convert the date into a required format
#here in this example, the format given in string is MM/DD/YYYY and required final format is  YYYYMMDD
import re 
import datetime
str_dt='Applications to be submitted by 04/10/2024'
dt = re.findall('\d{2}/\d{2}/\d{4}', str_dt)[0]
dt = datetime.datetime.strptime(dt, '%m/%d/%Y')
dt=dt.strftime('%Y%m%d')
print('last date  for the application is ', dt)
