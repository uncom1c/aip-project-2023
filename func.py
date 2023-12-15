def twobit(it):
    '''
    Функция берет на вход список целых чисел it
    it2 - строка
    затем для каждого целого числа вычисляет его двоичное значение и добавляет это значение к строке it2
    по итогу из всех чисел списка it будет составлена последовательность двоичных чисел
    '''
    it2 = ''
    for i in range((len(it))):
        temp_it = ''
        k = it[i]
        while k>1:
            temp_it = str(k%2) + temp_it
            k = k//2
        temp_it = str(k%2) + temp_it
        it2+= temp_it
        # print(it2)
    return it2


stroka = [1, 2, 3, 4]
print(twobit(stroka))