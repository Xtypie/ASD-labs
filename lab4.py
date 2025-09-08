def sortc(mas):
    gap = len(mas)
    s = 1.247
    sor = False

    while not sor:
        gap = int(gap / s)
        if gap <= 1:
            gap = 1
            sor = True

        i = 0
        while i + gap < len(mas):
            if mas[i] > mas[i + gap]:
                mas[i], mas[i + gap] = mas[i + gap], mas[i]
                sor = False
            i += 1

    return mas

mas = [4, 2, 1, 7, 5, 3, 10, 15, 12, 9, 8]

print(sortc(mas))