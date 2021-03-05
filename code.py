Coding:
  
def Cumulative(lists): 
    cu_list = [] 
    length = len(lists) 
    cu_list = [sum(lists[0:x:1]) for x in range(0, length+1)] 
    return cu_list[1:]
a=int(input())
lists = list(map(int,input().split()))
b=int(len(lists))
c=Cumulative(lists)
for i in range(0,b-1):
  print(c[i],end=" ")
print(c[b-1])
