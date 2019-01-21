zemnoi_ves = int(input('Ваш вес:'))
for i in range(2018,2034):
    zemnoi_ves = zemnoi_ves + 1
    moon_high = zemnoi_ves * 0.165
    print(moon_high,'Лунный вес %s' % i)
