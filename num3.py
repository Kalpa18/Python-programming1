char=input()
vows="aeiou"
for i in vows:
  if(i==char):
    print("Vowel")
    break
conss="bcdfghjklmnpqrstvwxyz"
for j in conss:
  if(j==char):
    print("Consonant")
  else:
    print("invalid")
