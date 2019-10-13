
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
        if self.Success==True:
            return 1
        else:
            if self.Stop_Search==False:
                return 0
            elif self.Stop_Search==True:
                return -1
"""
arr=[6,7,8,9,14,32,34,56]
A=BinarySearch(arr)
for _ in range(0,5):
    A.Step(10)
    print(A.left,A.right)
    print(A.GetResult())
"""





