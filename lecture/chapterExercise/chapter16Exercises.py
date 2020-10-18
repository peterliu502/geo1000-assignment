class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    # Exercise 16.0.1
    def print_time(self):
        print("{:02d}:{:02d}:{:02d}".format(self.hour, self.minute, self.second))

    # Exercise 16.0.2
    def increment(self, second):
        self.second += second
        self.minute += self.second // 60
        self.second %= 60
        self.hour += self.minute // 60
        self.minute %= 60

    # Exercise 16.0.3
    def increment_pure(self, second):
        second_new = self.second + second
        minute_new = self.minute + second_new // 60
        second_new %= 60
        hour_new = self.hour + minute_new // 60
        minute_new %= 60
        return Time(hour_new, minute_new, second_new)

    def time_to_int(self):
        minute_new = self.hour * 60 + self.minute
        return int(minute_new * 60 + self.second)

    def int_to_time(self, second):
        second_new = second
        minute_new = second_new // 60
        second_new %= 60
        hour_new = minute_new // 60
        minute_new %= 60
        self.__init__(hour_new, minute_new, second_new)

    # Exercise 16.0.4
    def increment1(self, second):
        self.int_to_time(self.time_to_int() + second)

    # Exercise 16.1
    def mul_time(self, num):
        time = Time(0, 0, 0)
        time.int_to_time(num * self.time_to_int())
        return time


if __name__ == "__main__":
    time1 = Time(1, 12, 45)
    time1.print_time()
    time2 = time1.increment_pure(12100)
    time2.print_time()
    time1.print_time()
    time1.increment(12100)
    time1.print_time()
    time3 = Time(1, 12, 45)
    time3.print_time()
    time3.increment1(12100)
    time3.print_time()
    time4 = Time(1, 1, 1)
    time4.mul_time(60).print_time()
