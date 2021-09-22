import time


class BubbleSort:
    def __init__(self, array):
        self.array = array
        self.n = len(array)
        self.start_time = 0
        self.end_time = 0

    def sort(self):
        self.start_time = time.time()
        for i in range(self.n):
            for j in range(0, self.n - i - 1):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
        self.end_time = time.time()
        return self.array

    def execution_time(self):
        return self.end_time - self.start_time
