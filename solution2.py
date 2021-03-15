months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def code_year(year: int):
    digits = []
    for i in range(2):
        digits.append(int(year % 10))
        year = divmod(year, 10)[0]
    last_two_digits = int(str(digits[1]) + str(digits[0]))
    return (6 + last_two_digits + divmod(last_two_digits, 4)[0]) % 7


def code_month(m: int):
    if m == 1 or m == 10:
        return 1
    elif m == 5:
        return 2
    elif m == 8:
        return 3
    elif m == 2 or m == 3 or m == 11:
        return 4
    elif m == 6:
        return 5
    elif m == 12 or m == 9:
        return 6
    elif m == 4 or m == 7:
        return 0
    else:
        return -1


def day_week(month: int, year: int):
    code = divmod(1 + code_month(month) + code_year(year), 7)[1]
    if code < 2:
        return code + 6
    else:
        return code - 2


def prev_month(cur_month: int):
    if cur_month == 0:
        return months[12]
    else:
        return months[cur_month]


def empty_matrix(row, col):
    matrix = []
    for i in range(row):
        matrix.append([])
        for j in range(col):
            matrix[i].append(-1)
    return matrix


def calendar(month: int, year: int):
    result = empty_matrix(5, 7)
    # 0-пон, 6 - воск
    day_w = day_week(month, year)
    counter = day_w

    for i in range(5):
        for j in range(7):
            if j < day_w:
                counter = prev_month(month) - day_w
            else:
                day_w = 0
            counter += 1
            if counter == months[month] +1:
                counter = 1
            result[i][j] = counter

    return result


def main():
    print(calendar(3, 2021))


if __name__ == '__main__':
    main()

"""Реализовать функцию, которая будет возвращать двумерный массив целых чисел в виде календаря на заданный месяц. Функция должна принимать два числа – номер и номер года, например:

(11, 2017) → { { 30, 31, 1, 2, 3, 4, 5 },

{ 6, 7, 8, 9, 10, 11, 12 },

{ 13, 14, 15, 16, 17, 18, 19 },

{ 20, 21, 22, 23, 24, 25, 26 },

{ 27, 28, 29, 30, 1, 2, 3 } }"""
