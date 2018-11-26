from multiprocessing import Process, Lock, Pool
from time import sleep
import random

processes = []
forks = [Lock() for _ in range(5)]


class PairOfForks:
    def __init__(self, idx):
        if idx != 0:
            self.right_fork = forks[idx]
            self.left_fork = forks[(idx - 1) % 5]
        else:
            self.right_fork = forks[(idx - 1) % 5]
            self.left_fork = forks[idx]

    def take(self):
        self.left_fork.acquire()
        self.right_fork.acquire()

    def give_away(self):
        self.left_fork.release()
        self.right_fork.release()


class Philosopher:
    def __init__(self, idx):
        self.idx = idx
        self.forks = PairOfForks(idx)

    def run(self):
        while True:
            self.forks.take()
            print("Philospoher #", self.idx, " is eating")
            sleep(random.random())
            self.forks.give_away()
            sleep(random.random())


philosophers = [Philosopher(i) for i in range(5)]
pool = Pool(processes=5)


def run_philosopher(idx, name):
    print("Creating: ", name)
    return philosophers[idx].run()


for i in range(5):
    processes.append(Process(target=run_philosopher, args=(i, "Philosopher")))
    processes[i].start()

for i in range(5):
    processes[i].join()


