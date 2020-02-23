import datetime
year=input('Enter a year: ')
month=input('Enter a month: ')
day=input('Enter a day: ')
f=datetime.date(int(year),int(month),int(day))
if (month=='1' or month=='3' or month=='5' or month=='7' or month=='8' or month=='10' or month=='12'):
    print('This month has 31 days')
elif (month=='2'):
    if (int(year)%4!=0):
        print('This month has 28 days')
    elif (int(year)%100!=0):
        print('This month has 29 days')
    elif (int(year)%400!=0):
        print('This month has 28 days')
    else:
        print('This month has 29 days')
