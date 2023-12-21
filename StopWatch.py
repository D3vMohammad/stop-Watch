# made by https://github.com/D3vMohammad
import time

print("enter number of seconds")
a=int(input())
while a!=0:
  print(str(a) + "  seconds remaining")
  time.sleep(1)
  a=a-1
print ("the time is up ")
time.sleep(1)