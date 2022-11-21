class Auto():
    def __init__(self, number, brand, model, NorU, color, ep, year, price):
        self.number = number
        self.brand = brand
        self.model = model
        self.NorU = NorU
        self.color = color
        self.ep = ep
        self.year = year
        self.price = price

    def __str__(self):
        return f"«{self.number} {self.brand} {self.model} {self.NorU} {self.color} " \
               f"{self.ep}л.с {self.year}г. {self.price}р.»"

    def update_price(self, new_price):
        return self.price + new_price

    def __eq__(self, other):  # ==
        if self.year == other.year and self.ep == other.ep:
            return True
        return False

    def __lt__(self, other):  # <
        if self.year != other.year:
            return self.year < other.year
        elif self.ep != other.ep:
            return self.ep < other.ep
        return False

    def __le__(self, other):  # <=
        if self.__eq__(other):
            return True
        if self.__lt__(other):
            return True
        return False


class Dealership():
    def __init__(self, name, adres, FIO, phone):
        self.name = name
        self.adres = adres
        self.FIO = FIO
        self.phone = phone
        self.sp = []

    def insert_auto(self, auto):
        self.sp.append(auto)

    def sale_auto(self, number):
        for auto in self.sp:
            if auto.number == number:
                self.sp.remove(auto)
                break

    def __str__(self):
        return f"«Салон: «{self.name}» {self.adres} {self.FIO} {self.phone}»"

    def print_autos(self):
        print(*self.sp, sep="\n")

    def __eq__(self, other):  # ==
        nov_s = len(list(filter(lambda x: x.NorU == 'новый', self.sp)))
        nov_o = len(list(filter(lambda x: x.NorU == 'новый', other.sp)))
        return len(self.sp) == len(other.sp) and nov_s == nov_o

    def __lt__(self, other):  # <
        nov_s = len(list(filter(lambda x: x.NorU == 'новый', self.sp)))
        nov_o = len(list(filter(lambda x: x.NorU == 'новый', other.sp)))
        if len(self.sp) != len(other.sp):
            return len(self.sp) < len(other.sp)
        elif len(self.sp) == len(other.sp):
            return nov_s < nov_o
        return False

    def __le__(self, other):  # <=
        if self.__eq__(other):
            return True
        if self.__lt__(other):
            return True
        return False


p1 = Auto('а235бв750', 'audi', 'q5', 'новый', 'чёрный', 223, 2022, 2500000)
p2 = Auto('b220c999', 'BMW', 'Norev', 'новый', 'белый', 220, 2019, 1500000)
p3 = Auto('b211c999', 'BMW', 'Norev', 'с пробегом', 'серый', 225, 2020, 1700000)
print(p1)
print(p2)
print(p1.update_price(100000))
print(p1 > p2)
c1 = Dealership('Авторевью', 'г. Москва, Новорязанское шоссе, д.154,', 'Филиппов Ф.Ф.', '8485-415-5555')
c2 = Dealership('Авто', 'г. Москва, Рязанское шоссе, д.15,', 'Путин В.В.', '8485-415-5555')
c1.insert_auto(p1)
c1.insert_auto(p2)
c2.insert_auto(p3)
c1.sale_auto('b220c999')
print(c1)
c1.print_autos()
print(c1 == c2)
print(c1 > c2)
