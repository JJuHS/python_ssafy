
class Dog():
    sound = '멍멍'

class Cat():
    sound = '야옹'

### Dog class 우선 상속
# class Pet(Dog, Cat):
#     def __init__(self):
#         super().__init__()
#         self.sound = super().sound
#     def __str__(self):
#         return f'애완동물은 {self.sound}소리를 냅니다.'
    

# my_pet = Pet()
# print(my_pet)

### Cat class 우선 상속

class Pet(Cat, Dog):
    def __init__(self):
        super().__init__()
        self.sound = super().sound
    def __str__(self):
        return f'애완동물은 {self.sound}소리를 냅니다.'
    

my_pet = Pet()
print(my_pet)