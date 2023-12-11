nums = []

def pseudo_random(x0, a, c, m):
    '''
    Функция берет на вход четыре целых числа
    x0 - целое число, берется из списка nums
    nums - список со всеми уже достигнутыми значениями рандомайзера, изначально содержит только seed
    seed - начальное число, с которого начинается генерация
    a, c, m - целые числа, задаются пользователем самостоятельно
    Функция добавляет в nums следующий сгенерированный элемент

    '''
    x= (x0 * a + c) % m
    nums.append(x)
    return 0

seed = 1
nums.append(seed)
a, c, m = 3, 7, 7877



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

def encoding(stroka):
    '''
    Функция берет на вход строку stroka
    letters - список из ascii-номеров каждого элемента строки stroka, к которому прибавили 128, чтобы в двоичной системе длина была 8
    bit_stroka - двоичная строка из letters, созданная при помощи twobit
    helper_encode - строка ключа
    encoded_stroka - зашифрованная строка
    temp_pseudo - временный элемент рандомной последовтельности для расчета ключа для i-ой четверки bit_stroka, сам temp_pseudo берется 
                как i-й элемент nums
    bit_pseudo - четырехзначный ключ для i-ой четверки bit_stroka
    helper_encode состоит из кучи строк bit_pseudo
    Затем каждый элемент bit_stroka я xor-ю с helper_encode дабы получить зашифрованную строку encoded_stroka
    '''
    letters = []
    for i in range(len(stroka)):
        letters.append(ord(stroka[i])+128)

    bit_stroka = twobit(letters)
    # print(bit_stroka)
    helper_encode=''
    encoded_stroka = ''
    for i in range(len(bit_stroka)//4):
       
        temp_pseudo = nums[i]%16
        bit_pseudo = ''
        while temp_pseudo>1:
            bit_pseudo = str(temp_pseudo%2) + bit_pseudo
            temp_pseudo= temp_pseudo//2
        bit_pseudo = str(temp_pseudo%2) + bit_pseudo
        while len(bit_pseudo)<4:
            bit_pseudo = '0' + bit_pseudo
        helper_encode+=bit_pseudo
    for i in range(len(helper_encode)):
        if bit_stroka[i]==helper_encode[i]:
            encoded_stroka+='0'
        else:
            encoded_stroka+='1'

    return encoded_stroka, helper_encode


def decoder (key, lock):
    '''
    Функция декодер получает на вход две строки key, lock
    key - строка ключа, с помощью которого расшифровывается строка lock
    decoder сначала xor-ит эти две строки, чтобы получить двоичную строку, которая одинакова с двоичной строкой от изначального сообщения
    Затем он разбивает эту строку (decoded_stroka) на подстроки длинной 8, чтобы расшифровать каждый символ
    decoded_letters - строка изначальных символов
    '''
    decoded_stroka = ''
    for i in range(len(key)):
        if key[i] == lock[i]:
            decoded_stroka+='0'
        else:
            decoded_stroka+='1'
    decoded_letters=''
    for i in range(len(decoded_stroka)//8):
        temp_stroka=''
        for j in range(8):
            temp_stroka+=decoded_stroka[8*i+j]
        num_letter=0
        for j in range(len(temp_stroka)):
            if temp_stroka[j]=='1':
                num_letter+= 2**(7-j)
        decoded_letters += chr(num_letter - 128)
    

    return(decoded_letters)
    



stroka = input()
for i in range(len(stroka)*2 - 1):
    pseudo_random(nums[i], a, c, m)

key = encoding(stroka)
key = key[1]
crypted = encoding(stroka)
crypted = crypted[0]
# print(nums)
# print(encoding(stroka))
print(decoder(key, crypted))

