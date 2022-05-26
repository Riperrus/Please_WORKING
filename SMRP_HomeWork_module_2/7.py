lst='''Ехал Грека через реку.
Видит Грека в реке рак.
Сунул в реку руку Грека.
Рак за руку Греку цап.
'''
lib="ЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ"
def listmerge(lstlst):
    all=[]
    for lst in lstlst:
      all.extend(lst)
    return all
lst=[i.split() for i in lst.replace(".","").split()]
lst=listmerge(lst)
for i in list(enumerate(lst)):
    if i[1][0] in lib:print(f'{i[0]} - {i[1]}')
