str=input()
list=[]
for i in str:
  if(i!=" "):
    list.append(i)
a=list[0]
b=list[1]
c=list[2]

if((a>>b)and(a>>c)):
  print(a)
else:
  if((b>>c)and(b>>a)):
    print(b)
  else:
    print(c)
    
  
