import os,sys
import tempfile
import argparse
import json

def read_data():
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    try:
        with open(storage_path, 'r') as f:
            return f.read()
    except IOError:
        pass

def save_date(data):
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    try:
        with open(storage_path, 'w') as f:
            f.write(json.dumps(data))
    except IOError:
        print("An IOError has occurred!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--key')
    parser.add_argument('--val')
    data = read_data()
    param = parser.parse_args()
    if data == None:
        data = {}
        if param.key != None:
            if param.val != None:
                data[param.key] = [param.val]
                save_date(data)
                sys.exit()
            else:
                print(None)
        else:
            print(None)
            sys.exit()
    else:
        data = json.loads(data)
        if param.key != None:
            if param.val != None:
                if (param.key in data):
                    vals = data[param.key]
                else:
                    vals = []
                vals.append(param.val)
                data[param.key] = vals
                save_date(data)
            else:

                if (param.key in data):
                    strval = ""
                    for i in data[param.key]:
                        strval += ", "+str(i)
                    strval = strval[2:]
                    print(strval)