#Test project for job vacancy "Python programmer" by Alexander Denisov

import pandas as pd
import json

users = ['user1', 'user2', 'user3']
file_json = {'commands': []}

#for each file user
for i in users:
    user = pd.read_csv(i+'.csv', sep=',')
    raws = user.shape[0]

    #for each raw in user
    for j in range(raws):
        if file_json["commands"] == []:
            file_json['commands'].append({'param': [{'user': i}], 'function': user.loc[j]['func'], 'name': user.loc[j][
                'test'], 'module': user.loc[j]['module']})


        else:
            flag = 0

            #Comparison of
            for i_command in range(len(file_json["commands"])):

                #Comparison of raw in user file with modules in file_json
                if (user.loc[j]['module'] == file_json['commands'][i_command]['module']) and (user.loc[j]['test'] ==
                        file_json['commands'][i_command]['name']) and (user.loc[j]['func'] ==
                        file_json['commands'][i_command]['function']):
                    file_json['commands'][i_command]['param'].append({'user': i})
                    flag = 0
                    break

                else:
                    flag = 1

            if flag == 1:
                file_json['commands'].append(
                    {'param': [{'user': i}], 'function': user.loc[j]['func'], 'name': user.loc[j][
                        'test'], 'module': user.loc[j]['module']})

with open('file.json', 'w') as file:
    json.dump(file_json, file)