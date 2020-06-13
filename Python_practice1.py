print("Hello world of Fizzbuzz leek! ")

""" for fizzbuzz in range(31):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print(fizzbuzz, "fizzbuzz")
    elif fizzbuzz % 3 == 0:
        print(fizzbuzz, "fizz")
    elif fizzbuzz % 5 == 0:
        print(fizzbuzz, "buzz")
    print(fizzbuzz)
 """

#fizzbuzz = ''
fizzbuzzArray = []

start = int(input("Start Value:"))
end = int(input("End Value:"))

for i in range(start,end+1):
    if i%3 == 0 and i%5 == 0:
        #fizzbuzz += "\nfizzbuzz"
        fizzbuzzArray.append("fizzbuzz")
    elif i%3 == 0:
        #fizzbuzz += "\nfizz"
        fizzbuzzArray.append("fizz")
    elif i%5 == 0:
        #fizzbuzz += "\nbuzz"
        fizzbuzzArray.append("buzz")
    # elif i%3 != 0 and i%5 != 0:
    else:
        #fizzbuzz += "\n"+str(i)
        fizzbuzzArray.append(str(i))
    #fizzbuzz += ' '
    #fizzbuzzArray.append( ' ' )

#print(fizzbuzz)
for i in fizzbuzzArray:
    print(i)