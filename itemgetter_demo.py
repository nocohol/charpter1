from operator import itemgetter
items: dict[str, int] = {'a':1,'b':2,'c':3}
a_and_c: itemgetter =  itemgetter('a', 'c')
print(a_and_c(items))
