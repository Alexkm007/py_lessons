class Value():
    def __init__(self):
        self.ammaunt = 0

    def __get__(self, obj, obj_type):
        return self.ammaunt

    def __set__(self, obj, value):
      self.ammaunt = value - value * obj.commission
      return self.ammaunt

class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission