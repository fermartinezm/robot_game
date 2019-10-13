class FallException(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self, *args, **kwargs):
        return repr(self.value)

    def get_msg(self):
        return self.value
