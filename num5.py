str=input()
list=[]
for i in str:
  if(i!=" "):
    list.append(i)
a=int(list[0])
b=int(list[1])
c=int(list[2])

if((a>>b)and(a>>c)):
  print(a)
else:
  if((b>>c)and(b>>a)):
    print(b)
  else:
    print(c)
    
  
