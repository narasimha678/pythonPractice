x,y=2,4

print(x)
print(y)


#if we want to read frist value in to head and remaining to tail
l=[1,2,3,4,5]

head,*tail=l
print(head)
print(tail)


#if we want to read all except alst to haed and last one to tail
l=[1,2,3,4,5]

*head,tail=l
print(head)
print(tail)

l=[1,2,3,4,5]

head=l
print(head)
