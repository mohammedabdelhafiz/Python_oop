class maths:
    def __init__(self):
        self.result = 0


    def add(self, num, *nums):
        self.result = self.result + num
        for x in range (len(nums)):
            self.result=self.result+x
        return self

    def subtract(self,num,*nums):
        self.result = self.result - num
        for i in range (len(nums)):
            self.result=self.result-i
        return self
       

md = maths()
x=md.subtract(2,4,5,6,7,8,9,0).add(100,300,12,4).subtract(2,1,2,3,4,5,6,6)
print(x.result)