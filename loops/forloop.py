friends=["nara","simha","rao","balagolla"]

for frnd in friends:
    print(f"{frnd} is your friend")


for frnd in range(5):
    print(f"{frnd} is your friend")

for frnd in range(10,20,2):
    print(f"{frnd} is your friend")

#using for loop

grades=[35,45,23,100,23]
total=0
count=len(grades)


for grade in grades:
    total += grade

print(total/count)

#using sum funciton
grades=[35,45,23,100,23]
total=sum(grades)
count=len(grades)
    
print(total/count)