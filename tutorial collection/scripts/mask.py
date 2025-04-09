op('mask').clear()
list_from_dat = []
for i in op('select1').col(0):
    list_from_dat.append(i.val)

for x in list_from_dat:
    if x == 'DIGIT':
        op('mask').appendRow(1)
    else:
        op('mask').appendRow(0)

