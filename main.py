months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def month(first_day: int, prev_month: int, current_month: int):
    result = []
    counter = first_day - 1
    len_month = prev_month
    for i in range(5):
        result.append([])
        for j in range(7):
            if counter < len_month:
                counter += 1
                result[i].append(counter)
            else:
                len_month = current_month
                counter = 1
                result[i].append(counter)
    return result


def calendar(num_month: int):
    first_day_first_week = 28
    prev_month = 31
    result = []
    for i in range(num_month):
        if first_day_first_week == 1:
            prev_month = 0
        result = month(first_day_first_week, prev_month, months[i])
        prev_month = months[i]
        first_week = result[4]
        first_day_first_week = first_week[0]

        if 1 not in first_week:
            first_day_first_week = 1
    return result


def main():
    for week in calendar(num_month=4):
        print(week)


if __name__ == '__main__':
    main()

"""Реализовать функцию, которая будет возвращать двумерный массив целых чисел в виде календаря на заданный месяц. Функция должна принимать два числа – номер и номер года, например:

(11, 2017) → { { 30, 31, 1, 2, 3, 4, 5 },

{ 6, 7, 8, 9, 10, 11, 12 },

{ 13, 14, 15, 16, 17, 18, 19 },

{ 20, 21, 22, 23, 24, 25, 26 },

{ 27, 28, 29, 30, 1, 2, 3 } }"""
