
def exe1():
    a= float(input('nhap a= '))
    b= float(input('nhap b= '))
    c=float(input('nhap c= '))
    max=a
    if b>max :
        max=b
    if c>max :
        max =c
    print(max)
def exe():
    n=10
    while n<=0:
        if n%2==0:
            continue
        n-=1
def exe2(a):
    b=list(a)
    for i in range(len(a)):
        if a[i]==11:
            b[i]=11
        else: 
         b[i]='.'
    for  i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if(a[i]>a[j]):
                temp=a[i]
                a[i]=a[j]
                a[j]=temp
    temp=a.count(11)
    for i in range(temp):
        a.remove(11)
    for i in range(len(b)):
        if b[i]==11:
            a.insert(i,11)
    print(a)
#exe2([56,14,11,756,34,90,11,11,65,0,11,35])
import random
def lucky():
    cout=0
    max=int(input("enter max number: "))
    min=int(input('enter min number: '))
    number= random.randint(min,max)
    Useguess=int(input('enter number guess: '))
    cout+=1
    while Useguess!=number and cout!=5:
        print("you guess wrong!")
        if Useguess>number:
            print("My number guess hight then number!")
        else:
            print("My number guess lower then number!")

        Useguess=int(input('enter number guess: '))
        cout+=1
    if Useguess==number:
     print('my number is luckey')
    else:
       print('ban qua ngu')
def matrix():
    size=int(input("enter matrix: "))
    A=[[None for i in range(size)] for j in range(size)]
    col=0
    row=0
    d=size-1
    cout=0
    if size%2!=0:
        A[int(size/2)][int(size/2)]=size*size
    while d>=size/2:
        for i in range(col,d,1):
            cout=cout+1
            A[col][i]=cout
        for i in range (row,d,1):
            cout+=1
            A[i][d]=cout
        for i in range(d,col,-1):
            cout+=1
            A[d][i]=cout
        for i in range(d,row,-1):
            cout+=1
            A[i][row]=cout
        col+=1
        row+=1
        d-=1
    for i in A:
     print(i)
#matrix()
def xu_ly_file():
    f=open('D:/th.txt','r')
    print(f.read())

xu_ly_file()
print('h')
