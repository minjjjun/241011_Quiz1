class User:
    def __init__(self,name,age,num):
        self.name=name
        self.age=age
        self.num=num

    def info(self):
        print(f"가입하신 계정의 이름은{self.name}이며, 나이는 {self.age}, 그리고 연락처는 {self.num}입니다.")

name=input(print("이름을 입력하세요:"))
age=input(print("나이를 입력하세요:"))
num=input(print("연락처를 입력하세요:"))

user=User(name,age,num)
user.info()