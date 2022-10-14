age=36
txt="my name is john,i'm {}"
print(txt.format(age))
quantity=2
itemno=561
price=65
myorder="i want {} pieces of item {} for{} dollars"
print(myorder.format(quantity,itemno,price))
a='apple'
print(a.lower())
a="pineapple"
print(len(a))
txt="iam happy"
print("happy" in txt)
txt="i'm a goodgirl"
if "good" in txt:
    print("yes good is present")
txt="dulquer is pwoli"
if "dulquer" in txt:
    print("dulquer is abu kurishingal")
b="hello world"
print(b[2:4])


for x in "apple":
    print(x)