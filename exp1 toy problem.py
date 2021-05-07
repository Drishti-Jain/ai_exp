x=int(input("No. of bananas at the beginning: "))
y=int(input("Distance to be covered: "))
z=int(input("Max capacity of camel: "))
lost=0
start=x
for i in range(y):
  while start>0:
    start=start-z
    if start==1:
      lost=lost-1
    lost=lost+2
  lost=lost-1
  start=x-lost
  if start==0:
    break
print(start)
