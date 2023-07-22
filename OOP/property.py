# we use it to work with private(_namevar) vars
# getter is to return it, setter is to set it and deleter is to delete

class C:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        print('getter')
        return self._value

    @value.setter
    def value(self, new_value):
        print('setter')
        self._value = new_value

    @value.deleter
    def value(self):
        print('deleter')
        del self._value


c = C(5)
# we use getter here
print(c.value)
# we use setter
c.value = 15
print(c.value)
# deleter
del c.value
