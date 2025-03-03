import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def __repr__(self):
        """
        Возвращает информацию об объекте класса в режиме отладки
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        """
        Возвращает информацию об объекте класса для пользователей
        """
        return f"{self.name}"

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise ValueError("Сложение возможно только с объектами класса Item и дочерних от него")

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) <= 10:
            self.__name = new_name
        else:
            return "Длина наименования не должна быть более 10 символов!"

    @classmethod
    def instantiate_from_csv(cls):
        file_path = os.path.join("..", "src", "items.csv")
        try:
            with open(file_path, "r", newline='') as item_file:
                reader = csv.DictReader(item_file)
                for row in reader:
                    try:
                        cls(row["name"], row["price"], row["quantity"])
                    except Exception:
                        raise InstantiateCSVError

        except FileNotFoundError:
            raise FileNotFoundError("_Отсутствует файл item.csv_")

    @staticmethod
    def string_to_number(string):
        return int(float(string))


class InstantiateCSVError(Exception):
    """
    Класс-исключение при отсутствии колонки данных в файле
    """

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "_Файл item.csv поврежден_"

    def __str__(self):
        return self.message
