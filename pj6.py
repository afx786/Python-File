#create a list of names
names = ['Anil','Anmol','Aditya','Avi','Alka']
print(names)
# insert a name "Anuj" before "aditya"
names.insert(2,'Anuj')
print(names)
#append a name'Zulu'
names.append('Zulu')
print(names)
#delete 'avi' from the list
names.remove('Avi')
print(names)
#replace 'Anil with 'AnilKumar'
i=names.index('Anil')
names[i]='AnilKumar'
print(names)
#sort all the names in the list
names.sort()
print(names)
#print reversed sorted list
print(names.reverse())
