x = 1
while x < 100:
    print(x)
    x+=1

words = ["this","is","an","en","parrot"]

for word in words:
    print(word)

numbers = [1,2,3,4,5,6,7,8,9,0]
for number in numbers:
    print(number)

d = {"x":1,"y":3}

for key in d:
    print(key+"は"+str(d[key])+"に対応")

for key,v in d.items():
    print(key+"は"+str(v).format(key,v))


names = ["渋谷","恵比寿","上野"]
ages = [12,34,54]
for name,age in zip(names,ages):
    print(name,"さんは",age,"歳です")









































    
















