# we use these when we don't work with object, but we work with class
# it is defined with @classmethod and it has cls necessary attr


class Pizza:
    def __init__(self, size):
        self.size = size

    @classmethod
    def get_large_pizza(cls):
        return cls(42)

    @classmethod
    def get_standard_pizza(cls):
        return cls(30)


large_pizza = Pizza.get_large_pizza()
print(large_pizza.size)

standard_pizza = Pizza.get_standard_pizza()
print(standard_pizza.size)
