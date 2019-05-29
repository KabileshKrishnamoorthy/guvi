a,b,c= input().split()
if(a>=b):
  if(a>c):
    print(a)
  else:
    print(c)
elif(b>=a):
  if(b>c):
    print(b)
  else:
    print(c)
elif(a>=c):
  if(a>b):
    print(a)
  else:
    print(b)  
else:
  print("invalid")
