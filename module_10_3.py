import threading
from random import randint
from time import sleep

class Bank:
    def __init__(self, balance=0):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self):
        count_transactions = 100
        for _ in range(count_transactions):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sum_of_transaction = randint(50, 500)
            self.balance += sum_of_transaction
            print(f'Пополнение: {sum_of_transaction}. Баланс: {self.balance}.')
        sleep(0.001)

    def take(self):
        count_transactions = 100
        for _ in range(count_transactions):
            sum_of_transaction = randint(50, 500)
            print(f'Запрос на {sum_of_transaction}')
            if sum_of_transaction <= self.balance:
                self.balance -= sum_of_transaction
                print(f'Снятие: {sum_of_transaction}. Баланс: {self.balance}')
            else:
                print('Запрос отклонен, недостаточно средств')
                self.lock.acquire()


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')