class Rectangle:
    def __init__(self,long,width,color):
        self.long = long
        self.width = width
        self.color = str(color).upper()[:1] +str(color).lower()[1:]
    def perimeter(self):
        return 2*(self.long+self.width)
    def area(self):
        return self.long*self.width

arr = input().split()
if int(arr[0]) <= 0 or int(arr[1])<=0:
    print('INVALID')
else:
    r = Rectangle(int(arr[0]),int(arr[1]),arr[2])
    print(str(r.perimeter())+" "+str(r.area())+" "+r.color)

