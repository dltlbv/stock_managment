import csv
from uuid import UUID
from datetime import datetime, timedelta

users_filepath = "./users.csv"
stocks_filepath = "./stocks.csv"
items_filepath = "./items.csv"


with open(users_filepath, encoding="UTF-8", mode="r") as users_file:
    users = csv.DictReader(users_file)
    print("Юзеры: ")
    for user in users:
        user_id = user["user_id"]
        try:
            user_id = UUID(user_id)
            print(user_id)
        except ValueError:
            print("Невалидный тип данных")

with open(stocks_filepath, encoding="UTF-8", mode="r") as stocks_file:
    stocks = csv.DictReader(stocks_file)
    print("Стокс: ")
    for stock in stocks:
        stock_id = stock["stock_id"]
        try:
            stock_id = int(stock_id)
            print(stock_id)
        except ValueError:
            print("Невалидный тип данных")
        capacity_sq_m = stock["capacity_sq_m"]
        try:
            capacity_sq_m = float(capacity_sq_m)
            print(capacity_sq_m)
        except ValueError:
            print("Невалидный тип данных")
        owner_id = stock["owner_id"]
        try:
            owner_id = UUID(owner_id)
            print(owner_id)
        except ValueError:
            print("Невалидный тип данных")


with open(items_filepath, encoding="UTF-8", mode="r") as items_file:
    items = csv.DictReader(items_file)
    print("Итемс: ")
    for item in items:
        item_id = item["item_id"]
        try:
            item_id = int(item_id)
            print(item_id)
        except ValueError:
            print("Невалидный тип данных")
        stock_id = item["stock_id"]
        try:
            stock_id = int(stock_id)
            print(stock_id)
        except ValueError:
            print("Невалидный тип данных")
        size = item["size"]
        try:
            size = float(size)
            print(size)
        except ValueError:
            print("Невалидный тип данных")
        arrive_at = item["arrive_at"]
        try:
            arrive_at = datetime.strptime(arrive_at, "%Y-%m-%d")
            print(arrive_at)
        except Exception:
            print("Невалидный тип данных")
        expiration_time = item["expiration_time"]
        try:
            expiration_time = timedelta(days=float(expiration_time))
            print(expiration_time)
        except ValueError:
            print("Невалидный тип данных")
