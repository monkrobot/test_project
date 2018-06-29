data = [['P', 'w', 'o', 'o'],
        ['K', 'h', 'a', 'a'],
        ['s', 'm', 'r', 's'],
        ['o', 'd', 'b', 'k']]

password_data = [['.', '.', '.', '.'],
                 ['x', '.', '.', 'x'],
                 ['.', 'x', '.', '.'],
                 ['.', '.', '.', 'x']]

result_password = ''

def transform_password_data(local_password_data):
    global password_data
    transform_password = []
    raw_transform_password = []
    for i in range(0, len(local_password_data)):
        for j in range(len(local_password_data)-1, -1, -1):
            raw_transform_password.append(local_password_data[j][i])
        transform_password.append(raw_transform_password)
        raw_transform_password = []
    password_data = transform_password
    return(password_data)

def read_password(password_data, data):
    password = ''
    for i in range(0, len(password_data)):
        for j in range(0, len(password_data)):
            if password_data[i][j] == 'x':
                password += data[i][j]
            else:
                continue
    return(password)

for i in range(0, 4):
    result_password += read_password(password_data, data)
    transform_password_data(password_data)

print(result_password)