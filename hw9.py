# 연습문제 11.1의 Point 객체
class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
        
    def show(self):
        return f'({self.__x},{self.__y})'
        
    def set(self, x, y):
        if x and y :
            self.__x = x
            self.__y = y
        else :
            return False
    
    def get(self):
        tuple = (self.__x, self.__y)
        return tuple
    
class Rectangle:
    def __init__(self, x1, y1, x2, y2):
       self.__lt = Point(x1, y1)
       self.__rb = Point(x2, y2)
       
    def show(self):
       print(f'좌측 상단 꼭짓점이 {self.__lt.show()}이고 우측 하단 꼭짓점이 {self.__rb.show()}인 사각형입니다.', end='') 
       
    def getWidth(self):
        width = self.__rb.get()[0] - self.__lt.get()[0]
        return width
        
    def getHeight(self):
        height = self.__rb.get()[1] - self.__lt.get()[1]
        return height
    
    def getArea(self):
        area = self.getWidth() * self.getHeight()
        return area
    
    def getPerimeter(self):
        perimeter = 2*(self.getHeight() + self.getWidth())
        return perimeter
    
# 주 프로그램부
r1 = Rectangle(5, 5, 20, 10)
a = r1.getArea()
p = r1.getPerimeter()

r1.show()
print(f'\n넓이는 {a}, 둘레는 {p}')