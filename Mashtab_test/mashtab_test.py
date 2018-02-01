import pandas as pd
import json

users = ['user1', 'user2', 'user3']

#file_json = {'commands': [{'param': [], 'function': '', 'name': '', 'module': ''}]}
file_json = {'commands': []}

for i in users:
    user = pd.read_csv(i+'.csv', sep=',')
    raws = user.shape[0]

    for j in range(raws):
        if file_json["commands"] == []:
            file_json['commands'].append({'param': [{'user': i}], 'function': user.loc[j]['func'], 'name': user.loc[j][
                'test'], 'module': user.loc[j]['module']})
        #else:
        #    for i_command in range(len(file_json["commands"])):
        #        #if (user.loc[j]['module'] == file_json['commands'][i_command]['module']): #and (user.loc[j]['test'] ==
        #                #file_json['commands'][i_command]['name']) and (user.loc[j]['func'] ==
        #                #file_json['commands'][i_command]['function']):
        #            file_json['commands'].append(
        #                {'param': [{'user': i}], 'function': user.loc[j]['func'], 'name': user.loc[j][
        #                    'test'], 'module': user.loc[j]['module']})

print(file_json)
#for i in file_json["commands"]:
#    print(i)







#file_json = {'commands': [{'param': [], 'function': '', 'name': '', 'module': ''}]}
#
##file_json = json.dumps({'commands': [{'param': [], 'function': '', 'name': '', 'module': ''}]})
#file_json['commands'][0]['param'].append({'user': users[0]})
#if file_json['commands'][0]['param'] != {'user': users[1]}:
#    file_json['commands'][0]['param'].append({'user': users[1]})
#print('file_json:', file_json)


#with open('file.json', 'r') as f:
#    #for i in f:
#    #    print(i)
#    #data_read = f.read()
#    data = json.load(f)
#    print('data: ', data)
#
#    #print("data['commands']['param']: ", data['commands'][0]['param'])
#
#    for i in data['commands'][0]['param']:
#        if i['user'] == 'user1':
#            print(i['user'])