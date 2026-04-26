def fibonachchi():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


need_numbers = [5, 200, 1000, 100_000]
for num in need_numbers:
    count = 1
    for a in fibonachchi():
        if count == num:
            print(a)
            break
        count += 1
