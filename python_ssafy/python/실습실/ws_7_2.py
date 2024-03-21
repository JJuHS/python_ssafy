# 아래 클래스를 수정하시오.
class Shape:
    def __init__(self, name1, name2):
        self.name1 = name1
        self.name2 = name2
    def calculate_area(self):
        return self.name1 * self.name2


shape1 = Shape(5, 3)
area1 = shape1.calculate_area()
print(area1)
