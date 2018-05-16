'''
Вы должны извлечь часть имени файла по следующим правилам:
Предположим, что имя начинается с даты, представленной в виде длинного числа
После даты следует знак подчеркивания.
Далее имя файла с расширением.
В самом конце всегда есть дополнительное расширение файла.
'''

a = "1231231_FILE_NAME.EXTENSION.OTHEREXTENSION"

def func(text):
    line_pos = text.find('_')
    dot1_pos = text.find('.')
    dot2_pos = text.find('.', dot1_pos+1)
    return text[line_pos+1:dot2_pos]
    print(dot1_pos)
    print(dot2_pos)

print(func(a))