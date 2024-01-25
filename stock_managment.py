import csv
from uuid import UUID, uuid4
from datetime import datetime, timedelta


# a = 18.01.2024
# b = 10days
# a + b => 28.01.2024


class Stock:
    def __init__(
        self,
        stock_id: int,
        location: str,
        capacity_sq_m: float,
        owner_id: UUID,
    ):
        self.__stock_id = stock_id
        self.__location = location
        self.__capacity_sq_m = capacity_sq_m
        self.__owner_id = owner_id

    @property
    def owner_id(self):
        return self.__owner_id

    @property
    def stock_id(self):
        return self.__stock_id

    def __repr__(self):
        return f"Stock(id: {self.__stock_id}, owner_id: {self.__owner_id}, location: {self.__location}, capacity: {self.__capacity_sq_m})"


class Item:
    def __init__(
        self,
        item_id: int,  #
        stock_id: int,  #
        name: str,
        size: float,  #
        category: str,
        description: str,
        arrive_at: datetime,  #
        expiration_time: timedelta,  #
    ):
        self.__item_id = item_id
        self.__stock_id = stock_id
        self.__name = name
        self.__size = size
        self.__category = category
        self.__description = description
        self.__arrive_at = arrive_at
        self.__expiration_time = expiration_time

    @property
    def stock_id(self):
        return self.__stock_id

    def __repr__(self) -> str:
        return f"Item(item_id: {self.__item_id}, name: {self.__name}, description: {self.__description})"


class User:
    def __init__(self, user_id: UUID, phone: str, username: str, password: str):
        self.__user_id = user_id
        self.__phone = phone
        self.__username = username
        self.__password = password

    def __repr__(self) -> str:
        return f"User(id: {self.__user_id}, username: {self.__username}, phone: {self.__phone})"

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @property
    def user_id(self):
        return self.__user_id


class Controller:
    def __init__(self):
        self.__current_user: User = None
        self.__current_stock: Stock = None

    def signup(self):
        user_id = uuid4()
        username = input("Введите ваш ник для регистрации: ")
        password = input("Введите ваш пароль для регистрации: ")
        phone = input("Введите ваш номер телефона для регистрации: ")

        new_user = User(
            user_id=user_id,
            phone=phone,
            username=username,
            password=password,
        )
        database["users"].append(new_user)
        print("Вы успешно зарегистрировались!")

    def auth_user(self):
        while True:
            username = input("Введите ваш ник для входа: ")
            password = input("Введите ваш пароль для входа: ")

            for user in database["users"]:
                if user.username == username and user.password == password:
                    print("Вы вошли в аккаунт!")
                    self.__current_user = user
                    return
            print("Неверно введены данные!")

    def logout(self):
        pass

    def get_stock_information(self):
        if self.__current_user is None:
            print("Сначала надо войти в аккаунт")
            return

        if self.__current_stock is None:
            self.choose_stock()

        stock_id = self.__current_stock.stock_id
        stocks_items = list(
            filter(lambda item: item.stock_id == stock_id, database["items"])
        )
        for item in stocks_items:
            print(item)

    def choose_stock(self):
        if self.__current_user is None:
            print("Сначала надо войти в аккаунт")
            return
        user_id = self.__current_user.user_id
        user_stocks: list[Stock] = list(
            filter(lambda stock: stock.owner_id == user_id, database["stocks"])
        )

        while True:
            print("Выберите склад")
            for index in range(len(user_stocks)):
                print(f"{index + 1}. ID склада: {user_stocks[index].stock_id}")
            selected_stock_index = int(input("Выберите порядковый номер склада: "))

            self.__current_stock = user_stocks[selected_stock_index - 1]
            return

    def add_items_to_stock(self):
        pass

    def remove_items_in_stock(self):
        pass

    def move_item_to_diff_stock(self):
        pass

    def search_available_item(self):
        pass


database = {
    "users": [],
    "stocks": [],
    "items": [],
}
users_filepath = "./users.csv"
with open(users_filepath, encoding="UTF-8", mode="r") as users_file:
    users = csv.DictReader(users_file)
    print("Юзеры: ")
    for user in users:
        user_id = user["user_id"]
        try:
            user_id = UUID(user_id)
        except ValueError:
            print("Невалидный тип данных")
        database["users"].append(
            User(
                user_id=user_id,
                phone=user["phone"],
                username=user["username"],
                password=user["password"],
            )
        )

stocks_filepath = "./stocks.csv"
with open(stocks_filepath, encoding="UTF-8", mode="r") as stocks_file:
    stocks = csv.DictReader(stocks_file)
    print("Стокс: ")
    for stock in stocks:
        stock_id = stock["stock_id"]
        try:
            stock_id = int(stock_id)
        except ValueError:
            print("Невалидный тип данных")
        capacity_sq_m = stock["capacity_sq_m"]
        try:
            capacity_sq_m = float(capacity_sq_m)
        except ValueError:
            print("Невалидный тип данных")
        owner_id = stock["owner_id"]
        try:
            owner_id = UUID(owner_id)
        except ValueError:
            print("Невалидный тип данных")
        database["stocks"].append(
            Stock(
                stock_id=stock_id,
                location=stock["location"],
                capacity_sq_m=stock["capacity_sq_m"],
                owner_id=stock["owner_id"],
            )
        )

items_filepath = "./items.csv"
with open(items_filepath, encoding="UTF-8", mode="r") as items_file:
    items = csv.DictReader(items_file)
    print("Итемс: ")
    for item in items:
        item_id = item["item_id"]
        try:
            item_id = int(item_id)
        except ValueError:
            print("Невалидный тип данных")
        stock_id = item["stock_id"]
        try:
            stock_id = int(stock_id)
        except ValueError:
            print("Невалидный тип данных")
        size = item["size"]
        try:
            size = float(size)
        except ValueError:
            print("Невалидный тип данных")
        arrive_at = item["arrive_at"]
        try:
            arrive_at = datetime.strptime(arrive_at, "%Y-%m-%d")
        except Exception:
            print("Невалидный тип данных")
        expiration_time = item["expiration_time"]
        try:
            expiration_time = timedelta(days=float(expiration_time))
        except ValueError:
            print("Невалидный тип данных")
        database["items"].append(
            Item(
                item_id=item["item_id"],
                stock_id=item["stock_id"],
                name=item["name"],
                size=item["size"],
                category=item["category"],
                description=item["description"],
                arrive_at=item["arrive_at"],
                expiration_time=item["expiration_time"],
            )
        )

controller = Controller()
controller.auth_user()
controller.get_stock_information()
