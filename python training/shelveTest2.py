import shelve

file_db = shelve.open('persondb')
rec = file_db['Tom Hardi']
rec1 = file_db['Sue Jones']
print(rec.name)
print(rec1.job)

print("dict: ", rec1.__dict__)