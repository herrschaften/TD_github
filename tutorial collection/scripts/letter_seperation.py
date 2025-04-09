op('seperator_table').clear()
myText = str(op('null1')[0,0])

x = list(myText)
for char in x:
    op('seperator_table').appendRow([char])  # Note the square brackets to make each character a single-item list

op('single_char').clear()
myText = list(dict.fromkeys(myText))
for i in myText:
    op('single_char').appendRow(i)