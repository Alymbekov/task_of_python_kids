import sys
def moon_weight():
    print("Введите ваш нынеший земной вес")
    ves = int(sys.stdin.readline())
    print("Введите ежегодный прирост вашего веса")
    plus_ves = int(sys.stdin.readline())
    print("Введите количество лет")
    years = int(sys.stdin.readline())
    velicina = 0.165
    
    for i in range(1,years):
        ves = ves + plus_ves
        moon_h = ves * velicina
        print('%s' % moon_h,'Лунный вес',i)
moon_weight()
