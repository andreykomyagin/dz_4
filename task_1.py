n = int(input("Введите количество элементов первого множества: "))
count = 0
plenty_1 = set()
while count < n:
    plenty_1.update((input("Введите элемент множества: ")))
    count += 1
print(plenty_1)
m = int(input("Введите количество элементов второго множества: "))
count = 0
plenty_2 = set()
while count < m:
    plenty_2.update((input("Введите элемент множества: ")))
    count += 1
print(plenty_2)
unification = plenty_1.intersection(plenty_2)
unification = list(unification)
for i in range(len(unification)):
    unification[i] = int(unification[i])
min_number = 0
temporary = 0
for i in range(len(unification)-1):
    min_number = i
    for j in range(i+1, len(unification)):
        if (unification[j] < unification[min_number]):
            min_number = j
    temporary = unification[min_number]
    unification[min_number] = unification[i]
    unification[i] = temporary
    print(unification)
        
print(f"{unification} - отсортированный ответ ")
