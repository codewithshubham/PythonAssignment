# Strings
# Vowel Count

v=['a','e','i','o','u']
c=0
str=input("Enter a string : ")
for i in str:
    for j in v:
        if i==j:
            c+=1

print(c)

