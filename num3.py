char=input()
vows="aeiou"
for i in vows:
  if(i==char):
    break
conss="bcdfghjklmnpqrstvwxyz"
for j in conss:
  if(j==char):
    break
if(i==char):
  print("Vowel")
elif(j==char):
  print("Consonant")
else:
  print("invalid")

