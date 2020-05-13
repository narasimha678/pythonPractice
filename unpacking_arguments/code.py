def mutiargs(*args):
    print(args)


mutiargs(1,2,3)


def named(**keyargs):
    print(keyargs)

named(name="nara",age=25)

details = {"name":"nara","age":25}
named(**details)

mutiargs(*details)

def infinite(*args,**kwargs):
    print(args)
    print(kwargs)


infinite(1,4,3,name="nara",age=25)