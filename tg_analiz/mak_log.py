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
def addFilter(i,filter):
    '''Проверяем строку на наличие не нужных слов или фраз'''
    for word in filter:
        if i.find(word) != -1:
            return  False
    return True
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
def addloginfiles(file,path,filter):
    filesource = open(path,'r', encoding="utf-8")
    stradd = ""
    wrstr = ""
    for i in filesource:
        if stradd == "" or add_or_none(i):
            stradd +=i
        else:
            if addFilter(stradd,filter):
                wrstr = ""+stradd
                file.write(stradd)
            stradd = i
    if stradd != wrstr:
        if addFilter(stradd, filter):
            file.write(stradd)

if __name__ == '__main__':
    path = returnPath()
    filter = returnFilter()
    if path == None:
        print("Не указан путь для анализа")
        sys.exit()

    tree = os.walk(path)
    if os.path.exists('allog.txt'):
        os.remove('allog.txt')
    allog = open('allog.txt','w',encoding="utf-8")
    for i in tree:
        folder = i[0]
        files  = i[2]
        for f in files:
            s = f.split(".")
            if s[1] == "log":
                fullpath = os.path.join(folder,f)
                print("Добавляю данные из файла ",fullpath)
                addloginfiles(allog, fullpath,filter)
    allog.close()







