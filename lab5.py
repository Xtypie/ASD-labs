#сортировка вставками

def insort(mas):
    for i in range(len(mas)):
        j = i - 1
        k = mas[i]
        while mas[j] > k and j >= 0:
            mas[j + 1] = mas[j]
            j -= 1
        mas[j + 1] = k
    return mas

mas = [3, 1, 5, 2, 8, 10, 7, 4]

print(insort(mas))