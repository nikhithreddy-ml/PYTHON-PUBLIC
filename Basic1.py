n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
print("The least number is",min(l))
print("The highest number is",max(l))
x=sum(l)/len(l)
print("The average is",x)
