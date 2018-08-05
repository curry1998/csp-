class crush_ball():
    point=0
    def __init__(self,point1):
        self.point=point1
        self.left = True
    def change_wall(self):
        if self.left:
            self.left=False
        else :
            self.left=True
    def pwall(self,l):
        if self.point==0 or self.point==l:
            self.change_wall()


if __name__=="__main__":
    str1=input()
    str2=input()

    n,L,t=tuple(str1.split(" "))
    list2=str2.split(" ")
    n=(int)(n)
    t=(int)(t)
    L=(int)(L)
    list3=[]
    for i in range(n):
        list3.append(crush_ball((int)(list2[i])))
    #print(list3[1].point)
    while t!=0:
        for j in list3:
            if j.left:
                j.point+=1
            else :
                j.point-=1
            j.pwall(L)


        for k in range(0,n):
            for s in range(k,n):
                if(list3[k].point==list3[s].point):
                    list3[k].change_wall()
                    list3[s].change_wall()
        #print(list3[1].point)
        t-=1
    for i in list3:
        print(i.point,end=" ")



