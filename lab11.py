# быстрая сортировка

def quicksort(mas):

    if len(mas) <= 1:
        return(mas)

    else:
        pivot = mas[0]
        l = [x for x in mas[1:] if x < pivot]
        r = [x for x in mas[1:] if x >= pivot]
        return quicksort(l) + [pivot] + quicksort(r)

mas = [12, 5, 7, 2, 4, 8, 9, 1, 0, 55, 21, 30, -1]

print(quicksort(mas))