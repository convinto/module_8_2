def personal_sum(numbers):
    result = 0
    incorrect_dat = 0
    for i in numbers:
        try:
            result += i
        except TypeError:
            incorrect_dat += 1
            print(f"Некорректный тип данных для подсчёта суммы - {i}")
    return result, incorrect_dat

def calculate_average(numbers):
    try:
        total_sum, incorrect_data_count = personal_sum(numbers)
        average = total_sum / (len(numbers) - incorrect_data_count)
    except TypeError:
        print("В numbers записан некорректный тип данных.")
        return None
    except ZeroDivisionError:
        return 0
    return average

print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')