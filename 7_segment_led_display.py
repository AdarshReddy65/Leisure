char_key = { 1:' _ ', 2:'|',3:'_',4:'|',5:'|',6:'_',7:'|'}
num_key = {0:[1,2,4,5,6,7],1:[4,7],2:[1,3,4,5,6],3:[1,3,4,6,7],4:[2,3,4,7],5:[1,2,3,6,7],6:[1,2,3,5,6,7],7:[1,4,7],8:[1,2,3,4,5,6,7],9:[1,2,3,4,6,7]}
num = input()

for i in num:
    if 1 in num_key[int(i)]:
        print(char_key[1],end = '')
    else:
        print('   ',end='')
print()

for i in num:
    for j in [2,3,4]:
        if j in num_key[int(i)]:
            print(char_key[j],end = '')
        else:
            print(' ',end='')
print()

for i in num:
    for j in [5,6,7]:
        if j in num_key[int(i)]:
            print(char_key[j],end = '')
        else:
            print(' ',end='')
print('.')