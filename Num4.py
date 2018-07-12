char=input()
alphs="abcdefghijklmnopqrstuvwxyz"
alphc="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in alphs:
  if(i==char):
    break;
for j in alphc:
  if(j==char):
    break;
if((i==char)or(j==char)):
  print("Alphabet")
else:
  print("No")
 
