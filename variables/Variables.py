x = 5
price = 9.99
discount = 0.8
res=price*discount
print(price*discount)
print(round(res,2))

fname="narasimha"
lname="balagolla"
print(f"myname first name is {fname} and last name is {lname}")

a=1259
b=a
print(a==b)

x,y,z=4,2,3
print(x,y,z)
x=y=z=7
print(x,y,z)
print(f"x values is",x)
print(f"x values is {x}")
x="3"
print(type(x))
print(type(int(x)))
nara="""dhfkhsfk
fdsfhdsfk
dfhdshfkhdsa"""

print(nara)

name="narasimha        "
print(name[:])
print(name[-6:-4])
print(len(name))
print(name.strip())
print(name.strip().lower())
print(name.strip().upper())
print(name.strip().zfill(1))
print(name.replace("a","b"))
print(name.replace("a","b"))

txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)

# first string
firstString = "abc"
secondString = "ghi"
thirdString = "ab"

string = "abcdef"
print("Original string:", string)

translation = string.maketrans(firstString, secondString, thirdString)

# translate string
print("Translated string:", string.translate(translation))