import time


class TrafficLight:
    __color = {'red': 7, 'yellow': 2, 'green': 4}

    def running(self):
        for k, v in TrafficLight.__color.items():
            time.sleep(v)
            print(k)


a = TrafficLight()
a.running()
