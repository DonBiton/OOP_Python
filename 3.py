#1 Управление счётом в банке
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number  
        self.__balance = balance  
    
    @classmethod
    def create_empty_account(cls, account_number): # Создание аккаунта с 0$
        return cls(account_number, balance=0)

    def deposit(self, amount): # вносим деньги на счёт
        self.check_positive_amount(amount)
        self.__balance = self.__balance + amount

    def withdraw(self, amount):
        self.check_positive_amount(amount)
        if self.__balance - amount < 0:
            raise ValueError("Недостаточео средств")
        else:
            self.__balance = self.__balance - amount

    def get_balance(self):
        return self.__balance

    @staticmethod
    def check_positive_amount(amount):
        if amount <= 0:
            raise ValueError("Сумма  должна быть положительным числом.")
        
acc = BankAccount.create_empty_account("123456789")  
acc.deposit(500)  
acc.withdraw(200)  
print(acc.get_balance())  # Вывод: 300



#2 Управление пользователями
class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
    
    @staticmethod
    def check_length_password(password):
        if len(password) < 6:
            raise ValueError("Ошибка: пароль слишком короткий")
    @classmethod
    def create_default_user(cls, username):
        return cls(username,password = "1234567890" )
    def set_password(self, password):
        self.check_length_password(password)      
        self.__password = password 
        print("Пароль успешно изменён  ")
    def get_username(self):
        return self.__username
        
user = User.create_default_user("Alice")
print(user.get_username())  # Вывод: Alice
# user.set_password("12345")  # Ошибка: пароль слишком короткий
user.set_password("securePass")  # Пароль успешно изменён            


#3 Управление библиотекой
class Book:
    def __init__(self, title, author, year = 0):
        self.__title = title
        self.__author = author
        self.__year = year

    @staticmethod
    def check_year(year):
        if year > 2025:
            raise ValueError("Год указан неверно")
    @classmethod
    def create_default_year(cls, title, author):
        return cls(title, author, year = 2024)
    def get_info(self):
        return f'{self.__title}, автор: {self.__author}, год: {self.__year}'

book1 = Book("1984", "George Orwell", 1949)
print(book1.get_info())  # Вывод: "1984, автор: George Orwell, год: 1949"

book2 = Book.create_default_year("Brave New World", "Aldous Huxley")
print(book2.get_info())  # Вывод: "Brave New World, автор: Aldous Huxley, год: 2024"
