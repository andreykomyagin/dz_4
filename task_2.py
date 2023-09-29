
n = int(input("Введите количество грядок: "))
if n >= 3:
    import random
    garden =list()
    for _ in range(n):
        garden.append(random.randint(4,10))
    print(garden)
    sum_max = garden[0]+garden[1]+garden[2]
    for i in range(0, len(garden)-2):
        if ((garden[i]+garden[i+1]+garden[i+2]) > sum_max):
            sum_max = garden[i]+garden[i+1]+garden[i+2]
    if (sum_max < (garden[len(garden)-2]+garden[len(garden)-1]+garden[0])):
        sum_max = garden[len(garden)-2]+garden[len(garden)-1]+garden[0]
    if (sum_max < (garden[len(garden)-1]+garden[0]+garden[1])):
        sum_max = garden[len(garden)-1]+garden[0]+garden[1]
    print(sum_max)
else:
    print("Неверное количество грядок")

