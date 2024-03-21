# HW_7_2
# 아래 클래스를 수정하시오.

class StringRepeater:
    def __init__(self, time_, string_):
        self.time_ = time_
        self.string_ = string_

    def repeat_string(self):
        for i in range(self.time_):
            print(self.string_)


repeater1 = StringRepeater(3, "Hello")
repeater1.repeat_string()

# HW_7_4
# 아래 클래스를 수정하시오.
class Person:
    number_of_people = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Person.number_of_people += 1

    def introduce(self):
        print(f'제 이름은 {self.name} 이고, 저는 {self.age} 살 입니다.')


person1 = Person("Alice", 25)
person1.introduce()
print(Person.number_of_people)
