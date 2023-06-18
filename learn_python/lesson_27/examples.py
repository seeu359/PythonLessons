from django.views.generic import DetailView

class Counter:
    def __init__(self, value):
        if value > 2:
            self.value = value
        raise ValueError('Wrong value')

    def inc(self):
        self.value += 10

    def dec(self):
        self.value -= 1



class NonDecreasingCounter(Counter):  # в скобках указан класс-предок
    def get_value(self):
        return self.value




nc = NonDecreasingCounter(1)
print(nc.value)