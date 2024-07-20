from threading import Thread, Lock, Condition

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.lock = Lock()
        self.cond = Condition(self.lock)
        self.turn = 0

    # printNumber.accept(x) outputs "x", where x is an integer.
    def zero(self, printNumber):
        with self.lock:
            for i in range(1, self.n + 1):
                while self.turn != 0:
                    self.cond.wait()
                printNumber(0)
                self.turn = (i % 2 == 0) * 2 + (i % 2)
                self.cond.notify_all()

    def even(self, printNumber):
        with self.lock:
            for i in range(2, self.n + 1, 2):
                while self.turn != 2:
                    self.cond.wait()
                printNumber(i)
                self.turn = 0
                self.cond.notify_all()

    def odd(self, printNumber):
        with self.lock:
            for i in range(1, self.n + 1, 2):
                while self.turn != 1:
                    self.cond.wait()
                printNumber(i)
                self.turn = 0
                self.cond.notify_all()