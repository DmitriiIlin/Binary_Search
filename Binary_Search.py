
class BinarySearch:
    def __init__(self,input_array):
        #Конструктор класса
        self.array=input_array
        self.array_len=len(self.array)
        self.Right=self.array_len-1
        self.Left=0
        self.Stop_Search=False
        self.Success=False

    def Step(self,N):
        #выполняет один шаг поиска: делит текущий диапазон на два, продолжает сокращение рабочего диапазона,
        #корректируя Left и Right, при необходимости фиксирует завершение поиска
        last_right=self.Right
        last_left=self.Left
        for i in range(0,self.array_len):
            if type(self.array[i])!= int:
                return -1
        if self.array_len==0:
            return None
        middle_index=(self.Left+self.Right+1)//2
        middle_value=self.array[middle_index]
        if N>middle_value:
            self.Left=middle_index
        elif N<middle_value:
            self.Right=middle_index
        else:
            self.Success=True
        if self.Left==self.Right or (last_left==self.Left and last_right==self.Right):
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


#12 Занятие

def GallopingSearch(array,N):
    #Блок 1 : Поиск диапазона нахождения искомого элемента
    i=1
    max_index=len(array)-1
    right=len(array)-1
    left=0
    index=2**i-2
    while True:
        if array[index]==N:
            return True
        elif array[index]<N:
            i+=1
            index=2**i-2
            if index>max_index:
                index=max_index
                right=max_index
                if array[index]==N:
                    return True
                else:
                    return False
            else:
                pass
        else:
            right=index
            left=2**(i-1)-1
            break
    #Блок 2 : Создание массива и поиск позиции с помошью метода Step класса BinarySearch 
    res_arr=[]
    for j in range(left,right+1):
        res_arr.append(array[j])
    Output=BinarySearch(res_arr)
    while Output.Success!=True:
        Output.Step(N)
        if Output.Stop_Search==True and Output.Success!=True:
            return False
        else:
            pass
    return True



"""
arr=[1,23,90,97,101,104,567]
print(GallopingSearch(arr,7))
"""    
    





