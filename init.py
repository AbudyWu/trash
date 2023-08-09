import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)


class M1_OPT:
    pos = 20
    neg = 21
    input_reset = 24
    input_set = 23

    def __init__(self):
        GPIO.setup(self.input_reset, GPIO.IN)
        GPIO.setup(self.input_set, GPIO.IN)
        GPIO.setup(self.pos, GPIO.OUT)
        GPIO.setup(self.neg, GPIO.OUT)
        self.stop()

    @property
    def reset(self):
        return GPIO.input(self.input_reset)

    @property
    def set(self):
        return GPIO.input(self.input_set)

    def __positive(self):
        print("m1 positive")
        GPIO.output(self.pos, True)
        GPIO.output(self.neg, False)

    def __back(self):
        print("m1 negative")
        GPIO.output(self.pos, False)
        GPIO.output(self.neg, True)

    def stop(self):
        print("m1 stop")
        GPIO.output(self.pos, False)
        GPIO.output(self.neg, False)

    def front(self):
        self.__positive()
        start = time.time()
        while True:
            # print(self.set)
            if self.set == True or time.time() - start > 1.4:
                self.stop()
                break

    def back(self):
        self.__back()
        start = time.time()
        while True:
            # print(self.reset)
            if self.reset == True or time.time() - start > 1.35:
                self.stop()
                self.__positive()
                time.sleep(0.01)
                self.stop()
                break


class M2_OPT:
    pos = 5
    neg = 6
    input_reset = 17
    input_set = 27

    def __init__(self):
        GPIO.setup(self.input_reset, GPIO.IN)
        GPIO.setup(self.input_set, GPIO.IN)
        GPIO.setup(self.pos, GPIO.OUT)
        GPIO.setup(self.neg, GPIO.OUT)
        self.stop()

    @property
    def reset(self):
        return GPIO.input(self.input_reset)

    @property
    def set(self):
        return GPIO.input(self.input_set)

    def __positive(self):
        print("m2 positive")
        GPIO.output(self.pos, False)
        GPIO.output(self.neg, True)

    def __negative(self):
        print("m2 negative")
        GPIO.output(self.pos, True)
        GPIO.output(self.neg, False)

    def stop(self):
        print("m2 stop")
        GPIO.output(self.pos, True)
        GPIO.output(self.neg, True)

    def positive(self):
        self.__positive()
        start = time.time()
        while True:
            # print(self.set)
            if self.set == True or time.time() - start > 1.7:
                self.stop()
                break

    def negative(self):
        self.__negative()
        start = time.time()
        while True:
            # print(self.set)
            if self.set == True or time.time() - start > 1.7:
                self.stop()
                break

    def move(self, type):
        while True:
            if type == 0:
                break
            elif type == 1:
                self.__positive()
                start = time.time()
                if self.set == True or (time.time() - start) > 1.7:
                    self.stop()
                    break
            elif type == 2:
                self.__negative()
                start = time.time()
                if self.set == True or (time.time() - start) > 1.7:
                    self.stop()
                    break

    def allreset(self, type):
        while True:
            if type == 0:
                break
            elif type == 1:
                self.__negative()
                start = time.time()
                if self.reset == True or time.time() - start > 1.7:
                    self.stop()
                    break
            elif type == 2:
                self.__positive()
                start = time.time()
                if self.reset == True or time.time() - start > 1.7:
                    self.stop()
                    break


m1 = M1_OPT()
m2 = M2_OPT()


if __name__ == "__main__":
    m2.stop()
    while 1:
        id = int(input("0/1/2/3="))
        if id == 3:
            break
        elif (id == 0) or (id == 1) or (id == 2):
            m2.move(id)
            time.sleep(0.1)
            m1.front()
            time.sleep(1)
            m1.back()
            time.sleep(0.1)
            m2.allreset(id)
        else:
            continue
    GPIO.cleanup()
