# 공격방어 캐릭터싸움클래스. 나,상대방 이름및직업생성.초기hp값 100.
# 공격시 hp -10, 방어시 hp -5.

class chr_fight():
    def __init__(self,name,job,hp):
        self.name = name
        self.job = job
        self.hp = hp

    def attack(self,name):
        name.hp -= 10
        print(self.name,'이(가)','상대',name.job,'에게',
              10,'피해를','입혔습니다','남은피:',name.hp)

    def defence(self,name):
        name.hp -= 5
        print(self.job,self.name,'는(은)',name.job,'의','공격을 방어해',
              5,'피해를 입었습니다','남은피',name.hp)

dasom = chr_fight('dasom','wizard',100)
doggy = chr_fight('doggy','tanker',100)

dasom.attack(doggy)
doggy.attack(dasom)
dasom.defence(doggy)
doggy.defence(dasom)
