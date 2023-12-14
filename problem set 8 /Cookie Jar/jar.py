class Jar:


    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0



    def __str__(self):
        return "🍪" * self.size



    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Deposit error")
        self.size += n



    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Withdraw error")
        self.size -= n


    @property
    def capacity(self):
        return self._capacity



    @capacity.setter
    def capacity(self, capacity):
        if capacity < 1:
            raise ValueError("@capacity.setter error")
        self._capacity = capacity



    @property
    def size(self):
        return self._size



    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("@size.setter error")
        self._size = size





def main():
    n = Jar()
    print(n)
    n.deposit(1)
    print(n)
    n.deposit(3)
    print(n)
    n.withdraw(2)
    print(n)





if __name__ == "__main__":
    main()