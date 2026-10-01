py = int(input("Enter your python marks: "))
jv = int(input("Enter your java marks: "))
sq = int(input("Enter your sql marks: "))
c = int(input("Enter your c++ marks: "))
dsa = int(input("Enter your data structure marks: "))
if py < 0 or jv < 0 or sq < 0 or c < 0 or dsa < 0 or py > 100 or jv > 100 or sq > 100 or c > 100 or dsa > 100 :
    print("Warning: Marks should be between 0 to 100 ")
else:
    total_marks = py+jv+sq+c+dsa
    print("Total Marks: ",total_marks,"/500")
    per = (total_marks / 500) * 100
    print("Percentage: ",per)
    if per >= 90:
        print("Grade: A")
        print("Result: Pass")
    elif per >= 70:
        print("Grade: B")
        print("Result: Pass")
    elif per >= 50:
        print("Grade: C")
        print("Result: Pass")
    elif per >= 40:
        print("Grade: D")
        print("Result: Pass")
    else:
        print("Grade: E")
        print("Result: Fail")