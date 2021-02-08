# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел
# к полученной ранее сумме и после этого завершить программу.

def my_sum ():
    sum_res = 0
    nx = False
    while nx == False:
        num = input('Вводите числа или E для окончания цикла - ').split()

        res = 0
        for el in range(len(num)):
            if num[el] == 'e' or num[el] == 'E':
                nx = True
                break
            else:
                res = res + int(num[el])
        sum_res = sum_res + res
        print(f'Текущая сумма {sum_res}')
    print(f'Итог {sum_res}')

my_sum()
