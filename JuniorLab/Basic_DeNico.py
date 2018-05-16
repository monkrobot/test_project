'''
Завершите функцию, которая принимает два параметра:
key - строка из уникальных букв и цифр
message - строка с закодированным сообщением

Ваша задача восстановить сообщение, используя ключ
Сперва создайте ключ на основе предоставленного ключа путем сортировки ключа в алфавитном порядке
и устаноквки позиции элементов в отсортированном ключе.

Например, для ключа crazy мы получим 23154, потому что отсортированный ключ выглядит так: acryz.
"C" в отсортированном варианте стоит на второй позиции, значит ключ начинается с 2 и тд.
Расшифруем наше сообщение cseerntiofarmit on используя ключ crazy'''

key = "6gr5"
message = "e pfjgut 1uv"

def deNico(key, message):
    sort_key = sorted(list(key))
    num_key = []
    for i in key:
        num_key.append(sort_key.index(i) + 1)
    print(num_key)
    print(sort_key)

    new_word = []
    len_key = len(num_key)
    for j in range(0, len(message), len_key):
        word = message[j:j+len_key]
        if len(word) < len_key:
            word += ' '*(len_key-len(word))
        for i in range(len_key):
            new_word.append(word[num_key[i] - 1])
    return ''.join(new_word).rstrip()

print(deNico(key,message))
