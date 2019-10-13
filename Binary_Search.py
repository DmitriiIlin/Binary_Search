
class BinarySearch:
    def __init__(self,input_array):
        #Конструктор класса
        self.array=input_array
        self.array_len=len(self.array)
        self.right=self.array_len-1
        self.left=0
        self.Stop_Search=False
        self.Success=False

    def Step(self,N):
        #выполняет один шаг поиска: делит текущий диапазон на два, продолжает сокращение рабочего диапазона,
        #корректируя Left и Right, при необходимости фиксирует завершение поиска
        for i in range(0,self.array_len):
            if type(self.array[i])!= int:
                return -1
        if self.array_len==0:
            return None
        middle_index=(self.left+self.right+1)//2
        middle_value=self.array[middle_index]
        if N>middle_value:
            self.left=middle_index
        elif N<middle_value:
            self.right=middle_index
        else:
            self.Success=True
        if self.left==self.right:
            self.Stop_Search=True
        else:
            pass 

    def GetResult(self):
        for i in range(0,self.array_len):
            if type(self.array[i])!= int:
                return -1
        if self.array_len==0:
            return -1
        if self.Success==True:
            return 1
        else:
            if self.Stop_Search==False:
                return 0
            elif self.Stop_Search==True:
                return -1

"""

arr=[1,23,"e","e"]
A=BinarySearch(arr)
for _ in range(0,4):
    A.Step("e")
    print(A.left,A.right)
    print(A.GetResult())
"""




