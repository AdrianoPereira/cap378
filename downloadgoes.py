import s3fs
import numpy as np
import datetime as dt


def to_julian_day(year, month, day):    
    date = dt.datetime.strptime('%d-%d-%d'%(year,month, day), '%Y-%m-%d')    
    return str(date.timetuple().tm_yday).zfill(3)


def downloadABI(**kargs):
    if kargs.get('day'):
        day = kargs.get('day')
    if kargs.get('month'):
        month = kargs.get('month')
    if kargs.get('year'):
        year = kargs.get('year')
    
    julian_day = to_julian_day(year, month, day)
    bucket = 'noaa-goes17/ABI-L2-CMIPF' 
    query = aws.ls('%s/%d/%s'%(bucket, year, julian_day))
    
    
    hours = np.array(query)    

    for hour in hours:
        files = aws.ls(hour)
        for file in files:
            print('Downloading %s...'%file.split('/')[-1])
            aws.get(file, file.split('/')[-1])            
#        fs.get(files[0], files[0].split('/')[-1])

#    print(files)


if __name__ == "__main__":
    DAY=1
    MONTH=1
    YEAR=2019
    aws = s3fs.S3FileSystem(anon=True)    

    downloadABI(day=DAY, month=MONTH, year=YEAR)
