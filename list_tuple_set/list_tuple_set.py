#list
l=["nara","simha","balagolla"] #-- we can add and delete values
#tuple
t=("nara","simha","balagolla") # -- we can't add and delete values
#set
s={"nara","simha","balagolla"} # -- we can add and dlete elements but we cannot put duplicates in this
# list and tuple will keep the insertion order, but set will not keep insertion order

print(l)
print(t)
print(s)

print(l[0])
print(t[0])
#getting the set value with set is not possible, becuase they will not keep the insertion order

#update an index value
l[0]="new value"

#t[0]="new value" -- this is not allowed in tuple
#s[0]="new value" -- this is not allowed in set becuase index/subscirpt notation is not supported by set

l.append("rao") # this will be used to add eleemnt to list at the ends
#t.append("rao") -- this is not possible becuase tuple will not allow to change its element in between
print(l)
print(t)
print(s)

l.remove("simha") #-- to relmove from list

s.add("rao") # to added element to set
s.remove("nara")

print(l)
print(t)
print(s)