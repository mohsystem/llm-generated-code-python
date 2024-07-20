from threading import Lock, Condition

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.current = 0
        self.zero_lock = Lock()
        self.even_odd_lock = Lock()
        self.even_odd_lock.acquire()  # Initially block even/odd threads

    # printNumber(x) will write value x to the generated output
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n):
            self.zero_lock.acquire()
            printNumber(0)
            self.current += 1
            if self.current % 2 == 0:
                self.even_odd_lock.release()
            else:
                self.zero_lock.release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1, 2):
            self.even_odd_lock.acquire()
            printNumber(i)
            self.zero_lock.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
            self.even_odd_lock.acquire()
            printNumber(i)
            self.zero_lock.release()