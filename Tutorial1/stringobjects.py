
info ="My name is Sam"
data ="I live in Mumbai"
print(info)
print(data)

#rswstring
rawstring=r" I have info  \n of Peter \t who lives in Pune."
print(rawstring)

rawstring=r" I have info of Peter who lives in Pune."
print(rawstring.upper())
print(rawstring.count("i"))
print(rawstring.replace("Peter","James"))
print(rawstring.index("Peter"))
print(len(rawstring))
print(rawstring.split(" "))
print("Peter" in rawstring)
print(rawstring[0:5])
print(rawstring[0:])
print(rawstring[:])

for eachdata in rawstring:
	print(eachdata)




