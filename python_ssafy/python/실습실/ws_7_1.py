# main.py


# 아래 클래스를 수정하시오.
class Shape:
    def __init__(self,name1,name2):
        self.name1 = name1
        self.name2 = name2
    def width(self):
        return self.name1
    def height(self):
        return self.name2


shape1 = Shape(5, 3)
print(shape1.width(), shape1.height())
