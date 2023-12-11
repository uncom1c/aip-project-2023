# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# def twobit(it):
#     '''
#     Функция берет на вход список целых чисел it
#     it2 - строка
#     затем для каждого целого числа вычисляет его двоичное значение и добавляет это значение к строке it2
#     по итогу из всех чисел списка it будет составлена последовательность двоичных чисел
#     '''
#     it2 = ''
#     for i in range((len(it))):
#         temp_it = ''
#         k = it[i]
#         while k>1:
#             temp_it = str(k%2) + temp_it
#             k = k//2
#         temp_it = str(k%2) + temp_it
#         it2+= temp_it
#         # print(it2)
#     return it2

# def encoding(stroka):
#     '''
#     Функция берет на вход строку stroka
#     letters - список из ascii-номеров каждого элемента строки stroka, к которому прибавили 128, чтобы в двоичной системе длина была 8
#     bit_stroka - двоичная строка из letters, созданная при помощи twobit
#     helper_encode - строка ключа
#     encoded_stroka - зашифрованная строка
#     temp_pseudo - временный элемент рандомной последовтельности для расчета ключа для i-ой четверки bit_stroka, сам temp_pseudo берется 
#                 как i-й элемент nums
#     bit_pseudo - четырехзначный ключ для i-ой четверки bit_stroka
#     helper_encode состоит из кучи строк bit_pseudo
#     Затем каждый элемент bit_stroka я xor-ю с helper_encode дабы получить зашифрованную строку encoded_stroka
#     '''
#     letters = []
#     for i in range(len(stroka)):
#         letters.append(ord(stroka[i])+128)

#     bit_stroka = twobit(letters)
#     # print(bit_stroka)
#     helper_encode=''
#     encoded_stroka = ''
#     for i in range(len(bit_stroka)//4):
       
#         temp_pseudo = nums[i]%16
#         bit_pseudo = ''
#         while temp_pseudo>1:
#             bit_pseudo = str(temp_pseudo%2) + bit_pseudo
#             temp_pseudo= temp_pseudo//2
#         bit_pseudo = str(temp_pseudo%2) + bit_pseudo
#         while len(bit_pseudo)<4:
#             bit_pseudo = '0' + bit_pseudo
#         helper_encode+=bit_pseudo
#     for i in range(len(helper_encode)):
#         if bit_stroka[i]==helper_encode[i]:
#             encoded_stroka+='0'
#         else:
#             encoded_stroka+='1'

#     return encoded_stroka, helper_encode

# def xor(key, lock):
#     k = ''
#     for i in range(len(key)):
#         if key[i]==lock[i]:
#             k+='0'
#         else:
#             k+='1'
#     return k

# def unbit(bitted):
#     k = ''
#     for i in range(len(bitted)//8):
#         temp_stroka = ''
#         for j in range(8):
#             temp_stroka+=bitted[8*i+j]
#         print(temp_stroka)
#         numlet = 0
#         for j in range(len(temp_stroka)):
#             if temp_stroka[i]=='1':
#                 numlet+= 2**(7-j)
#         k+=chr(numlet-128)

# x = encoding('ab')[0]
# y = encoding('ab')[1]

# # print(x,y)

# # print(xor(x, y))

# print(unbit(xor(x,y)))