import sys, os
import argparse

def returnFilter():
    """считываем файл фильтра, он должен лежать рядом со скриптом и наываться filter.txt"""
    filterlist = []
    if os.path.exists('filter.txt'):
        filter = open('filter.txt','r',encoding="utf-8")
        for i in filter:
            filterlist.append(i.rstrip())
    return filterlist
def returnPath():
    """возвращаем путь из параметра"""
    parser = argparse.ArgumentParser()
    parser.add_argument("path",nargs="?")
    namespace = parser.parse_args()
    if namespace.path:
        print(namespace.path)
        return namespace.path
    else:
        return None
def makedatetime(date,time):
    """20012017"""
    year = date[0:2]
    mons = date[2:4]
    day  = date[4:6]
    hour = date[6:8]
    min  = time.split(".")[0]
    return  day+"."+mons+"."+"20"+year+" "+hour+":" + min

def chekerrors(rowstr,f):
    '''Проверяем запись на наличие ошибок, если ошибка есть то приводим к нужному виду'''
    rowlist = rowstr.split(",")
    if len(rowlist) == 14:
        decr = rowlist[13].replace("\n"," ")
        if rowlist[13].find("Descr") > -1 and rowlist[11].find("Usr") > -1:
            strerr = (rowlist[4].replace("p:processName=","") + "," + rowlist[7].replace("t:applicationName=","")
                     + "," + rowlist[8].replace("t:computerName=","") + ","
                     + rowlist[11].replace("Usr=","") +","+ decr.replace("Descr=","") + "\n")
            return strerr
    elif len(rowlist) == 15:
        decr = rowlist[13].replace("\n", " ")
        if rowlist[13].find("Descr") > -1 and rowlist[11].find("Usr") > -1:
            strerr = (rowlist[4].replace("p:processName=", "") + "," + rowlist[7].replace("t:applicationName=", "")
                      + "," + rowlist[8].replace("t:computerName=", "") + ","
                      + rowlist[11].replace("Usr=", "") + "," + decr.replace("Descr=", "") + "\n")
            return strerr
    elif len(rowlist) == 8:
        decr = rowlist[7].replace("\n", " ")
        if rowlist[7].find("Descr") > -1 and rowlist[5].find("Usr") > -1:
            strerr = (rowlist[3].replace("process=","") + ","+"client"+ "," +"NA" +","
                      + rowlist[5].replace("Usr=","") + "," + decr.replace("Descr=","") + "\n")
            return strerr
        elif rowlist[5].find("OSThread") > -1 and rowlist[3].find("CONN") ==-1 and rowlist[3].find("rmngr") ==-1:
            strerr = (rowlist[3].replace("process=", "") + ","+"client"+ "," +"NA" +","
                      + "NA" + "," + decr.replace("Descr=", "") + "\n")
            return strerr
    elif len(rowlist) == 7:
        decr = rowlist[6].replace("\n", " ")
        if rowlist[4].find("OSThread") != -1 and rowlist[3].find("1cv8") !=-1:
            strerr = (rowlist[3].replace("process=", "") + ","+"client"+ "," +"NA" +","
                      + "NA" + "," + decr.replace("Descr=", "") + "\n")
            return strerr

    return ""

def add_or_none(i):
    """Проверяем это новая запись или продолжение"""
    listwords = i.split(",")
    if len(listwords) <= 3:
        return True
    else:
        time_ = listwords[0].split(':')
        if len(time_)!=2:
            return True
        else:
            duration = time_[1].split("-")
            if len(duration) != 2:
                return True
    return False
def seracherrors(file,path,errorsList,f):
    filesource = open(path,'r', encoding="utf-8")
    stradd = ""
    wrstr = ""
    strErrors = ""
    oldErrors = ""
    for i in filesource:
        if stradd == "" or add_or_none(i):
            stradd +=i
        else:
            timerow = stradd.split(',')[0].split("-")[0]
            date = makedatetime(f, timerow)
            strErrors = chekerrors(stradd,f)
            if len(strErrors) > 0 and oldErrors != strErrors:
                file.write(date + ","+strErrors)
                oldErrors = "" + strErrors
                wrstr = "" + stradd
            stradd = i
    if stradd != wrstr:
        timerow = stradd.split(',')[0].split("-")[0]
        date = makedatetime(f, timerow)
        strErrors = chekerrors(stradd,f)
        if len(strErrors) > 0 and oldErrors != strErrors:
            wrstr = "" + stradd
            file.write(date + ","+strErrors)

if __name__ == '__main__':
    path = returnPath()
    #filter = returnFilter()
    if path == None:
        print("Не указан путь для анализа")
        sys.exit()

    tree = os.walk(path)
    if os.path.exists('errorlogs.txt'):
        os.remove('errorlogs.txt')
    allog = open('errorlogs.txt','w',encoding="utf-8")
    errorsList = []
    summerrors = []
    for i in tree:
        folder = i[0]
        files  = i[2]
        for f in files:
            s = f.split(".")
            if s[1] == "log":
                fullpath = os.path.join(folder,f)
                print("Анализирую файл ",fullpath)
                seracherrors(allog, fullpath,errorsList,f)
    allog.close()







