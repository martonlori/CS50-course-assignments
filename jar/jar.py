class Jar:
    def __init__(self, capacity=12):
        size = 0
        self._capacity = capacity
        self._size = size
        if capacity < 0:
            raise ValueError

    def __str__(self):
        return f"{self._size * '🍪'}"

    def deposit(self, n):
        if (self._capacity - self._size) < n:
            raise ValueError
        else:
            self._size += n
            return self._size

    def withdraw(self, n):
        if self._size < n:
            raise ValueError
        else:
            self._size = self.size - n

    @property
    def capacity(self):
        return self._capacity


    @property
    def size(self):
        return self._size

    




