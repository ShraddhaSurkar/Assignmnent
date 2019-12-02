t=int(input( ))#No. of test case
#l=[]
for i in range(0,t): #loop will occure as per the number of cases
    l=[]
    a=int(input( ))#number of people
    b=input()
    b=b.split()
    for each in b:
        l.append(int(each))
    #print(l)
    l.sort()
    #print(l)
    c=-1
    d=0
    for k in range(0,a-1):
        d=d+l[0]+l[c]
        #print(d)
        c=c-1
    #print(d)
    d=d-l[0]
    print(d)

