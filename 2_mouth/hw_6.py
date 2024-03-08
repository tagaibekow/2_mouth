# class BankAccount:
#     def __init__(self, account_number):
#         self.account_number = account_number
#         self.balance = 0

#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Средства в размере {amount} были успешно зачислены на счет.")
    
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f"Средства в размере {amount} были успешно сняты со счета.")
#         else:
#             print("Недостаточно средств на счете.")

#     def check_balance(self):
#         print(f"Текущий баланс на счете: {self.balance}")

# class User:
#     def __init__(self, first_name, last_name, age, status):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.status = status

# def register_user():
#     first_name = input("Введите ваше имя: ")
#     last_name = input("Введите вашу фамилию: ")
#     age = input("Введите ваш возраст: ")
#     status = input("Введите ваш статус: ")
#     return User(first_name, last_name, age, status)

# if __name__ == "__main__":
#     user = register_user()
#     account_number = input("Введите номер вашего счета: ")
#     account = BankAccount(account_number)

#     account.deposit(1000)
#     account.check_balance()
#     account.withdraw(500)
#     account.check_balance()

# доп дз

def num(num1, num2):
    for i in range(num1 + 1):
        a = num1 - i
        if abs(i - a) == num2:
            return i, a

num1 = int(input("Введите возраст первого человека: "))
num2 = int(input("Введите разницу возраст двух человек: "))

age1, age2 = num(num1, num2)

print('Первому человеку',age1 ,'лет', 'Второму человеку', age2 ,'лет.')