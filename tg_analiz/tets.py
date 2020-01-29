def makedatetime(date,time):
    """20012017"""
    year = date[0:2]
    mons = date[2:4]
    day = date[4:6]
    hour = date[6:8]
    min = time.split(".")[0]
    return  day+"."+mons+"."+"20"+year+" "+hour+":" + min


data = "20012417"
time = "41:53.670001-0"
timerow = time.split('.')[0]

print(makedatetime(data,timerow))