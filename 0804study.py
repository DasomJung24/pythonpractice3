# 사이트별로 비밀번호를 만들어주는 프로그램작성.
site = input('사이트명을입력하세요:')
rule_1 = site[7:]
rule_2 = list(rule_1)
rule_3 = []
for i in range(len(rule_2)):
    if rule_2[i] == '.':
        break
    rule_3.append(rule_2[i])
rule_3 = ''.join(rule_3)
print(rule_3[:3]+str(len(rule_3))+str(rule_3.count('e'))+'!')