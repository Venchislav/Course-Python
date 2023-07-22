# these are similar to functions. They work with class logic(without using attrs or calling class), but they don't work with object of class
# we use @staticmethod with it

class APIClient:
    def __init__(self, *args, **kwargs):
        self._ = 'hey'

    @staticmethod
    def get_default_headers():
        return {'Content-Type': 'application/json'}
