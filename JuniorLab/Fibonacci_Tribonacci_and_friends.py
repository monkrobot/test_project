'''
Нужно вычислить функцию xbonacci. Для получения следующего числа последовательности нужно сложить предыдущие
числа в количестве, равным первоночальному размеру массива.
Количество значений в итоговой последовательности должно быть равно n. Метод должен вернуть массив.
'''


signature = [1,1,1,1]
n = 10

#a = [1,2,3,4,5,6]
#print(sum(a[-len(signature):]))

def xbonacci( signature, n):
    answer = signature
    len_sig = len(signature)
    if len(signature) >= n:
      return signature[:n]
    for i in range(n-len_sig):
        answer.append(sum(answer[-len_sig:]))
    return answer

print('answer:', xbonacci(signature,n))
