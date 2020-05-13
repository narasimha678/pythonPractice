numbers = [3,2,6,5,8,7]
double=[x*2 for x in numbers]

print(double)


friends=["Rolf","Sam","Samantha","Saurabh","Jen"]
starts_s=[ x for x in friends if x.startswith("S")]
starts_s1=[ x.startswith("S") for x in friends]

print(starts_s)
print(starts_s1)
