import csv

class Csv_reader:
    def __init__(self,path):
        self.path = path
        self.rows = []
        self.count_fields = 5
    '''метод получает на вход запись ипроверяет ее на валидность, если все ок он ее добавляет в массив записией'''
    def __validaterow(self,row):
        if row["car_type"].strip() == "":
            return False
        car_typs = ["spec_machine","car","truck"]
        if not row["car_type"].strip().lower() in car_typs:
            return False
        if row["brand"].strip() == "":
            return False
        extensions = ['png', 'jpg', 'jpeg', 'gif']
        ls_photo = row["photo_file_name"].strip().split(".")
        if len(ls_photo) >= 2:
            file_Extension = ls_photo[-1].lower()
            if not file_Extension  in extensions:
                return False
        else:
            return False
        #if not row["carrying"].isdigit():
        #    return False
        try:
            if float(row["carrying"]) <=0.0:
                return False

            if row["car_type"].strip().lower() =='car' and not row["passenger_seats_count"].isdigit():
                return False
            elif row["car_type"].strip().lower() =='car' and int(row["passenger_seats_count"]) <=0:
                return False

            if row["car_type"].strip().lower() =='spec_machine' and row["extra"].strip() == "":
                return False
        except:
            return False

        return True

    '''читает файл '''
    def readfile(self):
        try:
            with open(self.path) as csv_fd:
                reader = csv.reader(csv_fd,delimiter =';')
                i = 0
                for row in reader:
                    if i == 0:
                        headdict = self.return_headers(row)
                        if headdict == None:
                             self.headdict = headdict
                             return False
                        self.headdict = headdict
                        i += 1
                        continue
                    if len(row) <= 4:
                        continue
                    row_dict = {}
                    row_dict["brand"] = row[self.headdict['brand']].strip()
                    row_dict["photo_file_name"] = row[self.headdict['photo_file_name']].strip()
                    row_dict["carrying"] = row[self.headdict['carrying']].strip()
                    row_dict["passenger_seats_count"] = row[self.headdict['passenger_seats_count']].strip()
                    row_dict["car_type"] = row[self.headdict['car_type']].strip()
                    row_dict["extra"] = row[self.headdict['extra']].strip()
                    row_dict["body_whl"] = row[self.headdict['body_whl']].strip()
                    if self.__validaterow(row_dict):
                        self.rows.append(row_dict)

        except IOError:
            return False
        return True

    def return_headers(self,row):
        dicthead = {"brand":-1,"photo_file_name":-1,"carrying":-1,"car_type":-1}
        for item in row:
                dicthead[item] = row.index(item)
        if dicthead.get(-1) != None:
            return None
        return dicthead


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        return '.'+self.photo_file_name.split('.')[-1]

class Car(CarBase):
    car_type = 'car'
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count=0):
        super(Car,self).__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)

class Truck(CarBase):
    car_type = 'truck'
    def __init__(self, brand, photo_file_name, carrying, body_whl=''):
        super(Truck,self).__init__(brand, photo_file_name,carrying)
        self.body_whl = body_whl
        if body_whl != "":
           list_prop = self.body_whl.split('x')
           if len(list_prop) == 3:
                    self.body_length	= float(list_prop[0])
                    self.body_width = float(list_prop[1])
                    self.body_height = float(list_prop[2])
           else:
                    self.body_length = 0.0
                    self.body_width = 0.0
                    self.body_height = 0.0
        else:
            self.body_length = 0.0
            self.body_width = 0.0
            self.body_height = 0.0
    def get_body_volume(self):
        return self.body_length*self.body_width*self.body_height

class SpecMachine(CarBase):
    car_type = 'spec_machine'
    def __init__(self, brand, photo_file_name, carrying, extra=''):
        super(SpecMachine,self).__init__(brand, photo_file_name, carrying)
        self.extra = extra

class CrateCar:
    def __init__(self,row):
        self.row = row

    def create_car(self):
        if self.row["car_type"].strip().lower() == "car":
            return(Car(self.row["brand"],self.row["photo_file_name"],self.row["carrying"],
                       self.row["passenger_seats_count"]))
        elif self.row["car_type"].strip().lower() == "spec_machine":
            return (SpecMachine(self.row["brand"], self.row["photo_file_name"], self.row["carrying"],
                        self.row["extra"]))
        elif self.row["car_type"].strip().lower() == "truck":
            return (Truck(self.row["brand"], self.row["photo_file_name"], self.row["carrying"],
                            self.row["body_whl"]))

def get_car_list(csv_filename):
    car_list = []
    car_read = Csv_reader(csv_filename)
    if not car_read.readfile():
        return car_list
    for row in car_read.rows:
        cc = CrateCar(row)
        car_list.append(cc.create_car())
    return car_list

if __name__ == "__main__":
    car_list = get_car_list("coursera_week3_cars.csv")
    for car in car_list:
        print(car.get_photo_file_ext())

    print(get_car_list("ccoursera_week3_cars.csv"))
