a=int(input())
b=int(input())
c=int(input())
if((a>>b)and(a>>c)):
  print(a)
else:
  if((b>>c)and(b>>a)):
    print(b)
  else:
    print(c)
    
  
