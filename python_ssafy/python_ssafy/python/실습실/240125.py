# # 1
# class Car:
#     def __init__(self, model):
#         self.model = model

# class Hyundai(Car):
#     color = 'white'
#     def speed(self):
#         return '30km/h'

# class Kia(Car):
#     color = 'black'
#     def engine(self):
#         return '1.6turbo'

# class CarDrive(Hyundai, Kia):
#     def speed(self):
#         return '50km/h'
    
#     def power(self):
#         return '1,999cc'

# car = CarDrive('Sonata')    
# print(car.speed())
# print(car.color)   
# # CarDrive에 color가 없음 -> Hyundai : 'white' (없다면 -> Kia -> Car)
# # 메서드는 마지막에 정의된 매서드가 호출된다.
# # 클래스 변수는 클래스가 정의된 순간의 값이 유지된다.

# class A:
#     def __init__(self):
#         print('AAA')
# class B(A):
#     def __init__(self):
#         super().__init__()
#         print('BBB')
# class C(A):
#     def __init__(self):
#         super().__init__()
#         print('CCC')
# class D(A):
#     def __init__(self):
#         super().__init__()
#         print('DDD')
# class E(C, B, D):
#     def __init__(self):
#         super().__init__()
#         print('EEE')

# obj = E()
# print(obj)
# # print(E.__mro__)
# # print(E.mro())


###ERROR
def calculate_sum(a,b):
    return a + b

numbers = [1, 2, 3, 4, 5]
result = []
for i in range(len(numbers)):
    result = calculate_sum(result, numbers[i])

print(result)
