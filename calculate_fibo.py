#this program is written by Amir Hosein ghoroghi
f1 = 1
f2 = 1
n = int(input("Enter a number"))
if n == 1:
  print(f1)
elif n == 2:
  print(f2)
else :
  print(f1)
  print(f2)
  i = 3 
  while i <=n :
  f3 = f1 + f2
  print(f3," ")
  f1 =f2 
  f2 = f3
  i = i +1
  
#fibonachi function in one line
fib4 = lambda x: x if x < 2 else fib4(x-1) + fib4(x-2) 
# print(list(map(fib4,range(1,10))))

