title = ['영어','수학','국어','컴퓨터']
term1 = [100, 99, 88, 77]
# 2학기 점수는 1학기와 거의 동일하다]
term2 = term1.copy()
#      국어 점수만 66점으로 됨
term2[2] = 66
print(term2)
# 1학기보다 성적이 떨어진 과목은?
# for x in term1: # 2개 이상의 list를 비교할 때 for-each문 사용 불가
for i in range(len(term1)):
    if term1[i] > term2[i]:
        print(title[i])
# 1, 2학기 점수가 동일한 과목은?
for i in range(len(term1)):
    if term1[i] == term2[i]:
        print(title[i], end=' ')
