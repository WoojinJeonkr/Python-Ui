# space
s1 = ' samsung'
s2 = '    samsung'
s3 = 'samsung        '
s4 = '    samsung    '
s5 = '    samsung\n\n'

print(s1.lstrip()) # remove left space
print(s2.lstrip()) # remove left space
print(s5.strip()) # remove all space
print(s1.strip() == 'samsung')
# name = input('name >> ')

num_str = ['10','20','30','  40']
for one in num_str:
    # if one == '40':   # 실행되지 않음
    #   print('40이 있음') # 실행되지 않음
    if one.strip() == '40':
        print('40이 있음')