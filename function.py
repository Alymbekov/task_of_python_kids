import sys
def silly_age_joke():
    print('Сколько вам лет?')
    age = int(sys.stdin.readline())
    if age >= 10 and age <=13:
        print('13 + 49 + 84 + 155 +97: что получиться?Головная боль!')
    else:
        print('Что-что')
silly_age_joke()