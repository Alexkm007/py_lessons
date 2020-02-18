class open_file:
    def __init__(self,filename,mode):
        self.f = open(filename,mode)

    def __enter__(self):
        return self.f

    def __exit__(self, *args):
        self.f.close()

with open_file('test.txt','w') as f:
    f.write(" test string")

with open_file("test.txt","r") as f:
    print(f.readlines())

