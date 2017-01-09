n = 5
string1 = [1, 3, 6, 10, 0]
string2 = [2, 5, 9, 13, 0]
string3 = [4, 8, 12, 15, 0]
string4 = [7, 11, 14, 16, 0]
string5 = [100, 101, 102, 103, 104]
string = []

string.append(string1)
string.append(string2)
string.append(string3)
string.append(string4)
string.append(string5)

diag = (n*2)-1
iteration = 1
last_iteration = 1
print("this is" + str(7/4))
while iteration <= diag:
    #for i in range(0, iteration):
    print("Step" + str(iteration))
    if iteration <= diag/2 + 1:
        if iteration <= 1:
            print(string[iteration-1][0])
        else:
            j = iteration
            k = 0
            while j >= 0 and k < iteration:
                print(string[j - 1][k])
                j -= 1
                k += 1
            last_iteration += 1
            #for j in range(iteration, 0-1):
            #    print(string[j][i + 1])
    else:
        print("this is else")
        j = last_iteration
        k = iteration - diag/2 - 1
        print("j"+str(j))
        print("k" + str(k))
        print("iteration " + str(iteration))
        if iteration == diag:
            print("Hello")
            print(string[j - 1][k])
        else:
            while j > 1 and k < n:
                print(string[j - 1][k])
                j -= 1
                k += 1


    iteration += 1

#for i in range(1, diag):


#for i in range(0, 4):
#    for j in range(0, i):
#        print("Step" + str(i))
#        print(string[i][j])
#        print(string[i-1][j+1])