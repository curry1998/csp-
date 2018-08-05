import math


def add(list1):
    sum1=0
    flag=False
    sep=0
    for i in list1:
        if i==0:
            break
        elif i==1:
            sum1+=1
            sep=0
        elif i==2 and flag==False:
            sum1+=2
            sep=1
            flag=True
        elif i==2 and flag==True:
            sep+=1
            sum1+=2*sep
            
            flag=True
    return sum1
if __name__=="__main__":
    str1=input()
    list2=str1.split(" ")
    list3=[]
    for i in list2:
        list3.append((int)(i))
    result=add(list3)
    print (result)
        
            
