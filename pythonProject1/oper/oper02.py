# 비교연산자
# ==, !=, >=, >, <=, <
# 스트링도 비교연산자로 비교 가능

import tkinter.messagebox as box # as: alias

save_id = 'root' # 할당연산자
data_id = input('당신의 id는 >> ')
result = save_id == data_id # 비교의 결과는 무조건 bool!
print(result)
if(result) :
    print('login 성공')
    box.showinfo('result','로그인 성공!') # box.showinfo('a','b') : b를 messagebox로 보여준다.