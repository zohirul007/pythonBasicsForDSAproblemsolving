# If the student receives over 40% on her test, report that her grade passes; 
# if not, report that her grade fails
# with if statement. What if we want to have more than three possibilities, though? 
# We can do this by writing more than one elif statement into our code.
#find out A to F grade with using elif statement
# 90 or above is equivalent to an A grade, 80-89 is equivalent to a B grade,
# 70-79 is equivalent to a C grade, 65-69 is equivalent to a D grade
# 64 or below is equivalent to an F grade

grade = 89
if grade >= 90:
    print("A grade")
 
elif grade >=80:
    print("B grade")
 
elif grade >=70:
    print("C grade")
 
elif grade >= 65:
    print("D grade")
 
else:
    print("Failing grade")