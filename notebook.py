import time
import math
nums = []
seconds = time.localtime().tm_sec


def pseudo_random(x0):
    '''
    Функция берет на вход одно натуральное число
    x0 - натуральное число, берется из списка nums
    nums - список со всеми уже достигнутыми значениями рандомайзера, изначально содержит только seed
    seed - начальное число, с которого начинается генерация
    a, c, m - натуральные числа, задаются пользователем самостоятельно
    Функция добавляет в nums следующий сгенерированный элемент

    '''
    a, c, m = 3, 7, 7877

    x = (x0 * a + c) % m
    nums.append(x)
    return x


seed = 1
nums.append(seed)


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
        while k > 1:
            temp_it = str(k % 2) + temp_it
            k = k//2
        temp_it = str(k % 2) + temp_it
        it2 += temp_it
        # print(it2)
    return it2


def encoding(stroka):
    '''
    Функция берет на вход строку stroka
    letters - список из ascii-номеров каждого элемента строки stroka, к которому прибавили 128, чтобы в двоичной системе длина была 8
    bit_stroka - двоичная строка из letters, созданная при помощи twobit
    helper_encode - строка ключа
    encoded_stroka - зашифрованная строка
    temp_pseudo - временный элемент рандомной последовательности для расчета ключа. Берется как символ в последовательности nums,
        чей индекс равняется секунде, в которую запустили программу.
    bit_pseudo - temp_pseudo в двоичной системе счисления, дополненный нулями до четырех знаков (если их еще не было)
    helper_encode ключ состоит из кучи строк bit_pseudo
    Затем каждый элемент bit_stroka я xor-ю с helper_encode дабы получить зашифрованную строку encoded_stroka
    '''
    letters = []
    for i in range(len(stroka)):
        letters.append(ord(stroka[i])+128)

    bit_stroka = twobit(letters)
    # print(bit_stroka)
    helper_encode = ''
    encoded_stroka = ''
    for i in range(len(bit_stroka)//4):

        temp_pseudo = nums[seconds] % 16
        bit_pseudo = ''
        while temp_pseudo > 1:
            bit_pseudo = str(temp_pseudo % 2) + bit_pseudo
            temp_pseudo = temp_pseudo//2
        bit_pseudo = str(temp_pseudo % 2) + bit_pseudo
        while len(bit_pseudo) < 4:
            bit_pseudo = '0' + bit_pseudo
        helper_encode += bit_pseudo
    for i in range(len(helper_encode)):
        if bit_stroka[i] == helper_encode[i]:
            encoded_stroka += '0'
        else:
            encoded_stroka += '1'

    return encoded_stroka, helper_encode


def decoder(key, lock):
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
            decoded_stroka += '0'
        else:
            decoded_stroka += '1'
    decoded_letters = ''
    for i in range(len(decoded_stroka)//8):
        temp_stroka = ''
        for j in range(8):
            temp_stroka += decoded_stroka[8*i+j]
        num_letter = 0
        for j in range(len(temp_stroka)):
            if temp_stroka[j] == '1':
                num_letter += 2**(7-j)
        decoded_letters += chr(num_letter - 128)

    return (decoded_letters)


stroka = "aip"
for i in range(seconds):
    pseudo_random(nums[i])

key = encoding(stroka)
key = key[1]
crypted = encoding(stroka)
crypted = crypted[0]
# print(nums)
print(encoding(stroka))
otvet = decoder(key, crypted)
proverka_na_pravilnost = ''
if stroka == otvet:
    proverka_na_pravilnost = 'совпадает'
else:
    proverka_na_pravilnost = 'не совпадает'
print(
    f"Расшифрованная строка получилась {otvet}, с оригинальной строкой {proverka_na_pravilnost}")


def force_attack_16(code):
    '''
    Данная функция берет на вход зашифрованную строку (code)
    На выход подается список attack16, состоящий из натуральных чисел
    Для каждого i от 0 до 15 генерируется четырехзначное двоичное число, далее из него уже генерируется пробный ключ, который запускается в 
        функцию attack_rashivrovka
    Если результат оттуда не пустой, то в список attack16 добавляется новое значение
    '''
    attack16 = []
    for i in range(16):
        bit = ''
        temp_peremennaya = i
        while temp_peremennaya > 1:
            bit = str(temp_peremennaya % 2) + bit
            temp_peremennaya = temp_peremennaya//2
        bit = str(temp_peremennaya) + bit
        while len(bit) < 4:
            bit = '0' + bit
        trykey = ''
        for j in range(len(code)//4):
            trykey += bit
        temporary = attack_rashivrovka(code, trykey)
        if temporary:
            attack16.append(temporary)
    return (attack16)


def attack_rashivrovka(stroka, key):
    '''
    Функция работает почти так же, как и decoder, за исключением проверки на "легитимность"
    Потому что невозможно существовать num_letter<128 или >256
    '''
    decoded_stroka = ''
    for i in range(len(key)):
        if key[i] == stroka[i]:
            decoded_stroka += '0'
        else:
            decoded_stroka += '1'
    decoded_letters = ''
    for i in range(len(decoded_stroka)//8):
        temp_stroka = ''
        for j in range(8):
            temp_stroka += decoded_stroka[8*i+j]
        num_letter = 0
        for j in range(len(temp_stroka)):
            if temp_stroka[j] == '1':
                num_letter += 2**(7-j)
        if num_letter > 128 and num_letter < 256:

            decoded_letters += chr(num_letter - 128)

    return (decoded_letters)


seed1 = nums[-1]
nums = []
nums.append(seed1)
for i in range(20):
    pseudo_random(nums[i])

modnums = []
for i in range(len(nums)-1):
    modnums.append(nums[i+1] - nums[i])
umodnums = []
for i in range(len(modnums)-2):
    umodnums.append(abs(modnums[i+2]*modnums[i] - modnums[i+1]*modnums[i+1]))

potential_m = math.gcd(*umodnums)
# print(potential_m)


def calc_a_c():
    '''
    Функция выдает коэффиценты ГПСЧ имея только информацию о модуле и нескольких числах последовательности
    nums - массив сгенерированных генератором чисел
    a, c - коэффиценты
    '''
    x0 = nums[-1]
    pseudo_random(x0)
    x1 = nums[-1]
    pseudo_random(x1)
    x2 = nums[-1]
    pseudo_random(x2)
    y1 = x2 - x1
    y0 = x1 - x0
    counter = 0
    a = 1
    m = potential_m
    # while counter!=-1:
    #     if (y1- m*counter)%y0 == 0:
    #         counter=-1
    #         a = (y1- m*counter)//y0
    #     else:
    #         counter+=1
    #     if counter>m:
    #         break
    for i in range(len(nums)-2):
        if nums[i] < nums[i+1] and nums[i+1] < nums[i+2]:
            a = (nums[i+2]-nums[i+1])//(nums[i+1]-nums[i])
            break
    k = (a * x0)//m
    c = x1 + m*k - x0*a
    return (a, c)


potential = (0, 0)
potential = calc_a_c()
if potential[0] == 0:
    print("Сгенерировать коэффиценты ГПСЧ не получилось. Попробуйте заново запустить программу.")

else:
    potential_a = potential[0]
    potential_c = potential[1]

    # print(potential)
    # print(potential_a)


attacked_num = [1]


def attacked_pseudo_random(x0, a, c, m):
    '''
    Функция берет на вход четыре целых числа
    x0 - целое число, берется из списка nums
    nums - список со всеми уже достигнутыми значениями рандомайзера, изначально содержит только seed
    seed - начальное число, с которого начинается генерация
    a, c, m - целые числа, задаются пользователем самостоятельно
    Функция добавляет в nums следующий сгенерированный элемент

    '''

    x = (x0 * a + c) % m
    attacked_num.append(x)
    return 0


attack16 = force_attack_16(crypted)
attack60 = []
if potential[0] != 0:
    for i in range(60):
        attacked_pseudo_random(
            attacked_num[i], potential_a, potential_c, potential_m)

    code = crypted
    for i in range(len(attacked_num)):
        temp_rand = attacked_num[i] % 60
        temp_rand = temp_rand % 16
        bit = ''
        while temp_rand > 1:
            bit = str(temp_rand % 2) + bit
            temp_rand = temp_rand//2
        bit = str(temp_rand) + bit
        while len(bit) < 4:
            bit = '0' + bit
        trykey = ''
        for j in range(len(code)//4):
            trykey += bit
        temporary = attack_rashivrovka(code, trykey)
        if temporary:
            attack60.append(temporary)

print(f"Для метода атаки брутфорс получились ответы{attack16}")
if potential[0] != 0:
    print(f"Для метода атаки через взлом ГПСЧ получились ответы{attack60}")
