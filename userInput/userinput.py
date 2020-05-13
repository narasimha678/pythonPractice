# name=input("what is your name: ")
# print(name)

size_input = input("what is your hourse square feet: ")

square_feet=int(size_input)
square_meters=square_feet/10.8

print(f"{square_meters:.2f}")
template="value is :{:.2f}"
print(template.format(square_meters))