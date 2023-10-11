print("HELLO WORLD ")

count=0
c=0
lst=(input("Enter the numbers separated with space: \n"))
print(lst)

l=lst.split()

for N in l:
    if N=="100":
        count=count+1
print(count)

if count==2:print("TRUE, number 100 is two times")
elif count<2:print("False, number 100 is less than two times")
elif count>2: print("False, number 100 is more than two times")

for n in l:
    if n=="90":
        c=c+1
print(c)
if c==2:print("TRUE, number 90 is two times")
elif c<2:print("False, number 90 is less than two times")
elif c>2: print("False, number 90 is more than two times")
