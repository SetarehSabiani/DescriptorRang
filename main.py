# Descriptor for rang of character
class RangeCharacter:
    def __init__(self, min=2, max=10):
        self.max = max
        self.min = min

    def __set_name__(self, owner, name):
        self._attribute_name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self._attribute_name]

    def __set__(self, instance, value):
        if not isinstance(value, str) or len(value) > self.max or len(value) < self.min:
            raise ValueError(f'Invalid value for {self._attribute_name}')

        instance.__dict__[self._attribute_name] = value


class User:
    username = RangeCharacter()

    def __init__(self, username, password):
        self.username = username
        self.password = password


User("star3", "111")
