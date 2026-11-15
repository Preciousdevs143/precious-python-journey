print("My GPA Calculator - by Precious")

score1 = int(input("Enter score 1: "))
score2 = int(input("Enter score 2: "))
score3 = int(input("Enter score 3: "))

totalscore = score1 + score2 + score3
average = totalscore/3

print("Your total score is: ",totalscore)
print("Your average is: ",average)
for score in [score1,score2,score3]:
    if score >= 70:
     print(score,"A")
    elif score >= 60:
        print(score,"B")
    elif score >= 50:
        print(score,"C")
    elif score >= 40:
        print(score,"D")
    else:
        print(score,"Carry over")
       

if average >= 70:
    print("Grade: A")
elif average >= 60:
    print("Grade: B")
elif average >= 50: 
    print("Grade: C")
elif average >= 40:
    print("Grade: D")
else:
    print("Grade: Carry over - try again")

