'''
Функция chooseBestSum принимает три параметра: t - максимальная дистанция, k - число городов,
которое надо посетить и ls - массив дистанций между городами.
Функция возвращает максимальное расстояние, если такое существует, иначе null
'''

t = 100
k = 2
ls = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]

def choose_best_sum( t, k, ls):
    answer = 0
    new_ls = sorted(ls)
    items = [None]*k    #list of change items of size k
    for num in range(k):
        if num == 0:
            items[num] = new_ls[num]
        else:
            items[num] = new_ls[-num]
    print(new_ls)
    print(items)

   for last_item in range(items[1:]): #enumerate    #for last items in list 'items', which go
       for item in new_ls[-k + 1, 0, -1]:           #from right to left in new_ls if sum > t
           last_item = item #item in list 'items'
           if sum(items) > t:
       elif sum(items) < t:
           for item in new_ls[1:]:
               items[0] = item





    #for item in new_ls[-k+1,0,-1]:
    #    items[-k + 1]
    #    if sum(items) > t:



    #i = True
    #while i:
    #    if sum(items) > t:
    #        for last_item in items[1:]:
    #
    #        for item in new_ls[-k + 1, 0, -1]:
#
    #    elif sum(items) < t:
    #        for item in new_ls[1:]:
    #            items[0] = item



#def choose_best_sum( t, k, ls):
#    answer = 0
#    item = []
#    for num in range(k):
#        item.append(ls[num])
#    new_ls = sorted(ls)
#    for i in range(k-1,-1,-1):
#        for j in ls[i:]:
#            item[i] = j
#            item_sum = sum(item)
#            if item_sum > t:
#                continue
#            elif item_sum > answer:
#                answer = item_sum
#            else:
#                continue
#    return answer

print(choose_best_sum( t, k, ls))


