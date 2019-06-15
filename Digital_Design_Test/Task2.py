'''
Compare JSONs (40 points). Write a program that takes two strings in JSON format
and compares them. The program should output the difference between those JSON strings.
For example:
Input:
{"a": 2, "b": 3}
{"a": 2, "b": 4}
Output:
"b": 3
"b": 4
Input:
{"a": "hello", "b": {"c": 3}}
{"a": "hello", "b": {"c": 11}}
Output:
"b": {"c": 3}
"b": {"c": 11}
'''


def compare_json(str1, str2):
    '''
    Compares 2 json strings
    :param str1: json string 1
    :param str2: json string 2
    :return: print differences between json strings by each element
    '''
    for val1, val2 in zip(str1.items(), str2.items()):
        if val1 == val2:
            continue
        else:
            print(str(val1[0]) + ":", val1[1])
            print(str(val2[0]) + ":", val2[1])
    if len(str1) < len(str2):
        i = 1
        for val in str2.items():
            if i > len(str1):
                print('-')
                print(str(val[0]) + ":", val[1])
            i += 1
    elif len(str2) < len(str1):
        i = 1
        for val in str1.items():
            if i > len(str2):
                print(str(val[0]) + ":", val[1])
                print('-')
            i += 1



if __name__ == "__main__":
    a = {"a": 2, "b": ["3", 3], "m": {"k": 4}, "c": [{"a": 89}]}
    b = {"a": 2, "b": 4, "m": {"k": 4}, "c": [{"a": 89, "b": 87}], "f": 12}

    compare_json(a, b)

