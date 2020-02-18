class Test_class:

    def __getitem__(self, item):
        print("Вы обратились по ключу или индексу =",item)

    def __setitem__(self, key, value):
        print("Вы присваиваете значение {0} по ключу {1}".format(value,key))


a = Test_class()

a[1]
a['abc']

a['ddd'] = 100