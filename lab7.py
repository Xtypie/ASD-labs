

def shell_sort(mas):
    gap = len(mas) // 2

    while gap > 0:
        for i in range(gap, len(mas)):
            current_value = mas[i]
            j = i
            while j >= gap and mas[j - gap] > current_value:
                mas[j] = mas[j - gap]
                j -= gap
            mas[j] = current_value
        gap //= 2

    return mas

mas = [7.91, 5.16, -5.21, 5.88, -11.98]

shell_sort(mas)
print(mas)
