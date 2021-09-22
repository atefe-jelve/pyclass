#ATEFE-JELVE__THURSDAY14-18
#SAY-PERSON-WHAT-NUMBER-EVEN
print('list of even person in class:\n')
name = ['atefe' , 'mehdi' , 'ashkan' , 'nusha' , 'tahere', 'ali']
i = 0
while i <=len(name):
    if (i+1) % 2 == 0:
        print(f' {name[i]}  is person  {i+1} in class list ')
    i = i + 1
