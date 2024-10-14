from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        knights_power = 100
        battle_days = 0
        print(f'{self.name}, на нас напали!')
        for i in range(knights_power):
            if knights_power > 0:
                knights_power -= self.power
                battle_days += 1
                sleep(1)
                print(f'{self.name} сражается {battle_days} день(дня)..., осталось {knights_power} войнов.')
                if knights_power <= 0:
                    print(f'{self.name} одержал победу спустя {battle_days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print(f'Все битвы закончились!')
