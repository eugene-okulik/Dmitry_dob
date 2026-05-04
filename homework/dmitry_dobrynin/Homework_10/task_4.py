PRICE_LIST = """тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р"""

transformation_price_list = PRICE_LIST.split()
product = transformation_price_list[::2]
price_product = transformation_price_list[1::2]

# первое решение, но тут же внутри всё равно получаем цикл


new_price_list = list(zip(product, price_product))
result = {key: int(value.rstrip("р")) for key, value in new_price_list}
print(result)


# вообще без цикла, но с map


clear_price = list(map(lambda x: int(x.rstrip("р")), price_product))
result_2 = dict(zip(product, clear_price))
