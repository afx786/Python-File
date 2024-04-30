tpl=('F','I','a','b','b','e','r','g','a','s','t','e','d')
print(tpl)
#extract('b','b') from the tuple
t=tpl[3:5]
print(t)
#count number of 'e' in the tuple
count = tpl.count('e')
print('count=',count)
#check wether 'r' exists in the tuple
print('r' in tpl)
#convert the tuple to a list 
lst = list(tpl)
print(lst)
tpl = tpl[:3] + tpl[7:]
print(tpl)
