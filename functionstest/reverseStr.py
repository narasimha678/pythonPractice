def rever(name):
    if len(name)==1:
        return name
    return rever(name[1:])+name[0]


print(rever("narasimha is working in symplr"))


def passfunction():
    pass
    print(5)

passfunction()



sequence = [1,2,3,4]
print(list(map(lambda x:x*2,sequence)))