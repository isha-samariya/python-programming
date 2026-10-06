s = {}
s["name"]= str(input("Enter your name: "))
s["age"]= int(input("Enter your age: "))
s["course"]= str(input("Enter your course: "))
s["percentage"]= float(input("Enter your percentage: "))

for key,value in s.items():
    print(key, ":" ,value)

search = str(input("Enter any key value to search: "))
print(s.get(search))

s.update({"city":"Jaipur"})

if "city" in s:
    print("city : ",s["city"])
