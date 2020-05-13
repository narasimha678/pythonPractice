friends={"nara":20,"simha":"rao","balagolla":True}

print(friends["nara"])

friends["deekshi"]="girl"

print(friends)

family = {
    "narasimha" : {
                 "age": 36,
                 "sex": "male",
                 "dob": {
                     "original": "25/05/1983",
                     "records" : "01/07/1983"
                 }
                },
    "radhika" : {
                 "age": 32,
                 "sex": "female"
                },
    "deekshitha" : {
                 "age": 10,
                 "sex": "female"
                },
    "honey" : {
                 "age": 3,
                 "sex": "female"
                }
}

def printJsonValue(family,jsonpath):
    tempdict=family
    try:
        for x in jsonpath.split("."):
            tempdict=tempdict[x]
    except:
        print (f"given path '{jsonpath}' is invlaid")
    print (tempdict)

printJsonValue(family,"narasimha1.dob.original")
print(family["narasimha"]["dob"]["original"])
print(family["radhika"])
print(family["deekshitha"])
print(family["honey"])