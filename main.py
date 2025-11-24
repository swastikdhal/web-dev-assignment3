# class student:
#     name = None
#     roll = None
#     marks= None
#     def _init_(self,namex,rollx,marksx):
#         self.name = namex
#         self.roll = rollx
#         self.marks= marksx

# s1 = student('nigger', 2, 19)
# s2 = student('nighater', 3, 18)

# print(s1.marks)
# print(s2.marks)

# x = input   

#Create a class student with attributes: 1.Name 2.Roll no. 3.Marks
# class student:
#     name = None
#     Rollno = None
#     Marks = None
#     def _init_(self,namex,rollx,marksx):
#         self.name = namex
#         self.Rollno = rollx
#         self.Marks = marksx
#     def grade(self):
#         if self.Marks >= 95:
#             return 'You have got grade = A'
#         elif self.Marks >= 75:
#             return 'Grade = B'
#         else:
#             return 'Grade = C'

# S1 = student('nolu' , '2' , '95')
# print(S1.grade)

#Create a class rectangle with length and width with method = perimeter
class rectangle:
    def __init__(self,l,w):
        self.length = l
        self.width  = w
    def area(self):
        area = self.length * self.width
        return area
    def perimeter(self):
        perimeter = 2 * (self.length + self.width)
        return perimeter
shape = rectangle(3,5)
print(shape.area())
print(shape.perimeter())