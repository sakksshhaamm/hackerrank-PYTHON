name=[]
marks=[]
p=[]
l=[]
q=int(input())
for i in range(0,q):
    n=input()
    name.append(n)
    m=float(input())
    marks.append(m)
    p.append(m)

marks.sort()
ll=len(marks)
for k in range(0,ll-1):
    if marks[0]!=marks[k+1]:
        a=marks[k+1]
        break;
length=len(p)
for pp in range(0,length):
    if p[pp]==a:
        l.append(name[pp])
l.sort()
for i in l:
    print(i)
