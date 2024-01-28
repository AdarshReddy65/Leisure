char_key = { 1:'_', 2:'_',\
    3:'|',4:'\\',5:'|',6:'/',7:'|',\
    8:'_',9:'_',\
    10:'|',11:'/',12:'|',13:'\\',14:'|',\
    15:chr(8254),16:chr(8254)}

num_key = {0:[1,2,3,6,7,10,11,14,15,16],\
    1:[6,7,14],\
    2:[1,2,7,8,9,10,15,16],\
    3:[1,2,7,9,14,15,16],\
    4:[3,7,8,9,14],\
    5:[1,2,3,8,9,14,15,16],\
    6:[1,2,3,8,9,10,14,15,16],\
    7:[1,2,7,14],\
    8:[1,2,3,7,8,9,10,14,15,16],\
    9:[1,2,3,7,8,9,14,15,16]}

num = input()

line1 = ''
for i in num:
    line1 += ' '
    for j in range(1,3):
        if j in num_key[int(i)]:
            line1 += char_key[j]+' '
        else:
            line1 += '  '

line2 = ''
for i in num:
    if 3 in num_key[int(i)]:
        line2+=char_key[3]
    else:
        line2+=' '
    if 4 in num_key[int(i)]:
        line2+=char_key[4]
    elif 8 in num_key[int(i)]:
        line2+=char_key[8]
    else:
        line2+=' '
    if 5 in num_key[int(i)]:
        line2+=char_key[5]
    else:
        line2+=' '
    if 6 in num_key[int(i)]:
        line2+=char_key[6]
    elif 9 in num_key[int(i)]:
        line2+=char_key[9]
    else:
        line2+=' '
    if 7 in num_key[int(i)]:
        line2+=char_key[7]
    else:
        line2+=' '

line3=''
for i in num:
    for j in range(10,15):
        if j in num_key[int(i)]:
            line3+=char_key[j]
        else:
            line3+=' '

line4=''
for i in num:
    line4+=' '
    for j in range(15,17):
        if j in num_key[int(i)]:
            line4+=char_key[j]+' '
        else:
            line4+='  '

print(line1)
print(line2)
print(line3)
print(line4)