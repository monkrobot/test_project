'''Test project for job vacancy "Python programmer" by Alexander Denisov'''

import json
import pandas as pd

users_list = ['user1', 'user2', 'user3']
file_commands = {'commands': []}

#for each file user
for i in users_list:
    user = pd.read_csv(i+'.csv', sep=',')
    rows = user.shape[0]

    #for each raw in user
    for j in range(rows):
        if file_commands["commands"] == []:
            file_commands['commands'].append({'param': [{'user': i}], 'function': user.loc[j][
                'func'], 'name': user.loc[j]['test'], 'module': user.loc[j]['module']})

        else:
            flag = 0

            # Comparison of raw in user file with each "command" in file_json
            for i_command in range(len(file_commands["commands"])):

                if user.loc[j]['module'] == file_commands['commands'][i_command][
                        'module'] and user.loc[j]['test'] == \
                        file_commands['commands'][i_command]['name'] and user.loc[j]['func'] == \
                        file_commands['commands'][i_command]['function']:
                    file_commands['commands'][i_command]['param'].append({'user': i})
                    flag = 0
                    break

                else:
                    flag = 1

            if flag == 1:
                file_commands['commands'].append(
                    {'param': [{'user': i}], 'function': user.loc[j]['func'], 'name': user.loc[j][
                        'test'], 'module': user.loc[j]['module']})

print(file_commands)

#Adding file_commands to file.json(rewriting)
with open('file.json', 'w') as file:
    json.dump(file_commands, file)
