class Flower:

    def __init__(self, name, color, stem_length, price, freshness, life_time):
        self.name = name
        self.color = color
        self.stem_length = stem_length
        self.price = price
        self.freshness = freshness
        self.life_time = life_time

    def __repr__(self):
        return f"{self.name}"


class Rose(Flower):

    def __init__(self, color, stem_length, price, freshness, life_time):
        super().__init__("Роза", color, stem_length, price, freshness, life_time)


class Tulip(Flower):

    def __init__(self, color, stem_length, price, freshness, life_time):
        super().__init__("Тюльпан", color, stem_length, price, freshness, life_time)


class Chamomile(Flower):

    def __init__(self, color, stem_length, price, freshness, life_time):
        super().__init__("Ромашка", color, stem_length, price, freshness, life_time)


rose = Rose("Красный", 50, 300, 8, 7)
tulip = Tulip("Желтый", 40, 150, 8, 5)
chamomile = Chamomile("Белый", 30, 400, 8, 5)


class Bouquet:

    def __init__(self, flowers):
        self.flowers = flowers

    #  Высчитываем общуюю стоимость букета
    def get_total_price(self):

        price_bouquet = 0
        for flower in self.flowers:
            price_bouquet += flower.price
        return price_bouquet

    #  Высчитываем среднее время жизни букета
    def get_avg_life_time(self):

        # counter_flower = 0
        full_time = 0
        for flower in self.flowers:
            full_time += flower.life_time
            # counter_flower += 1

        return round(full_time / len(self.flowers), 1)

    #  Сортировка по свежести
    def sort_by_freshness(self):

        return sorted(self.flowers, key=lambda flower: flower.freshness)

    #  Сортировка по цвету
    def sort_by_color(self):

        return sorted(self.flowers, key=lambda flower: flower.color)

    #  Сортировка по длине стебля
    def sort_by_stem_length(self):

        return sorted(self.flowers, key=lambda flower: flower.stem_length)

    #  Сортировка по цене
    def sort_by_price(self):

        return sorted(self.flowers, key=lambda flower: flower.price)

    #  Поиск цветов в букете по времени жизни
    def get_flower_life_time(self, user_want_life_time):

        return list(
            flower for flower in self.flowers if user_want_life_time <= flower.life_time
        )


bouquet1 = Bouquet([rose, tulip, chamomile])
print(bouquet1.get_total_price())
print(bouquet1.get_avg_life_time())
print(bouquet1.sort_by_freshness())
print(bouquet1.sort_by_color())
print(bouquet1.sort_by_stem_length())
print(bouquet1.sort_by_price())
print(bouquet1.get_flower_price(3))
