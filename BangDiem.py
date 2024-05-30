class Student:
    def __init__(self,name,avg,id):
        self.name = name
        self.avg = avg
        self.id = 'HS%02d' % id
    def classification(self):
        if self.avg>=9 : self.status  = 'XUAT SAC'
        elif self.avg>=8: self.status ='GIOI'
        elif self.avg>=7: self.status ='KHA'
        elif self.avg>=5: self.status ='TB'
        else: self.status='YEU'
    def __gt__(self, other):
        if self.avg == other.avg: return self.id > other.id
        return self.avg < other.avg
if __name__ =='__main__':
    t = int(input())
    ds = []
    for loop in range(t):
        t-=1
        name = input()
        arr = [float(x) for x in input().split()]
        sum = arr[0]*2 + arr[1]*2
        for i in range(2,len(arr)): sum+= arr[i]
        avg = round((sum/12)*10.0/10.0,1)
        st = Student(name,avg,loop+1)
        st.classification()
        ds.append(st)
    for st in sorted(ds):
        print('{} {} {} {}'.format(st.id, st.name, st.avg, st.status))
