list1=[]
for x in range(5):
    num = int(input("Enter a number of your choice: "))
    list1.append(num)

s = sum(list1)
m = max(list1)
n = min(list1)
v = (s) / 5
print("Sum: ",s)
print("Largest: ",m)
print("Smallest: ",n)
print("sAverage: ",v)