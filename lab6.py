def selectSort(mas):

    for i in range(len(mas) - 1):
        minimum = mas[i]
        min_index = i

        for j in range(i + 1, len(mas)):
            if minimum > mas[j]:
                minimum = mas[j]
                min_index = j

        if min_index != i:
            mas[i], mas[min_index] = mas[min_index], mas[i]

        return mas


mas = [1, 2, 4, 5, 3, 7, 6, 9, 8, -1, -10, 12]

print(selectSort(mas))
