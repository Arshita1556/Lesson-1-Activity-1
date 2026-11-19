# 1) Ask the user to enter marks for 4 subjects: math, english, science, and hindi.
#    Store each mark in its own variable.
maths=48
english=84
science=64
hindi=7
# 2) Add all 4 subject marks and store the total in `sum`.
sum=maths+english+science+hindi

# 3) Print the total marks stored in `sum`.
print("total marks =",sum)
# 4) Calculate the percentage:
#    - Divide `sum` by 400 (total maximum marks for 4 subjects, assuming each is out of 100)
#    - Multiply the result by 100
#    Store the final value in `perc`.
perc=sum/400
perc=perc*100
# 5) Print the percentage stored in `perc`.
print("perc=",perc)