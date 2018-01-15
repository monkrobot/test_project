import pandas as pd
frame = pd.DataFrame({'numbers':range(10), 'chars':['a']*10})

new_line = {'numbers': 'Perov', 'chars': '11.11.11'}
print('new\n', frame.append(new_line, ignore_index="True"))

print(frame)
print(frame.columns) #columns names
print(frame.shape)   #number of rows and columns

#frame = pd.read_csv('dataset.tsv', header=0, sep='\t') #header - заголовки; \t - tabulation

frame['NewColumn'] = ["Nan"]*10    #add column
print("NewColumn Frame:\n", frame)

print("Frame with del:\n", frame.drop([7,8], axis=0))  # del raw

frame.drop([8,9], axis=0, inplace=True)          #del raw from frame
print("frame:", frame)

frame.drop('NewColumn', axis=1, inplace=True)     #del column
print("again frame:\n", frame)

frame.to_csv('save_to_csv.csv', sep=',', header=True, index=None)