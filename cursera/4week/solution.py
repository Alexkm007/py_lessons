import os.path
import tempfile

class File:
    def __init__(self,path):
        self.path = path
        if not os.path.exists(path):
            f = open(path,'w')
            f.close()
    def read(self):
        with open(self.path,'r') as f:
            return f.read()

    def write(self,data):
        with open(self.path, 'w') as f:
            return f.write(data)

    def __iter__(self):
        self.f = open(self.path,'r')
        self.poz = self.f.tell()
        return self

    def __next__(self):
      if self.poz != 0:
        self.f.seek(self.poz)
      line = self.f.readline()
      self.poz = self.f.tell()
      if len(line) != 0:
        return line
      else:
          self.f.close()
          raise StopIteration

    def __add__(self, other):
        newFile =  os.path.join(tempfile.gettempdir(),"new_file.txt")
        data = []
        for line in self:
            data.append(line)
        for line in other:
            data.append(line)
        with open(newFile,'w') as f:
            for line in data:
                f.write(line)
        return File(newFile)
    def __str__(self):
        return self.path


if __name__ == "__main__":
    f = File('test.txt')
    for line in f:
        print(line)

    file = f + File('test2.txt')
    for line in file:
        print(line)
    print(file)