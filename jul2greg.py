import datetime

def juliandate_to_gregoriandatetime(julian_date):
    aData = int(julian_date) + 32044
    bData = int((4 * aData + 3) / 146097)
    cData = aData - int((bData * 146097) / 4)
    dData = int((4 * cData + 3) / 1461)
    eData = cData - int((1461 * dData) / 4)
    mData = int((5 * eData + 2) / 153)
    day = eData - int((153 * mData + 2) / 5) + 1
    month = mData + 3 - 12 * int(mData / 10)
    year = bData * 100 + dData - 4800 + int(mData / 10)
    fraction = julian_date - int(julian_date)
    total_seconds = int(86400 * fraction)
    seconds = total_seconds % 60
    total_minutes = int(total_seconds / 60)
    minutes = total_minutes % 60
    hours = int(total_minutes / 60)
    DT = datetime.datetime(year, month, day, hours, minutes, seconds)
    return DT.strftime('%Y-%m-%d %H:%M:%S')

