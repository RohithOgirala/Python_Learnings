# program 1

item=(input("Enter item "))
quantity=int(input("Enter quantity"))
strtxt="I Want {},I want {} pieces of items"
print(strtxt.format(item,quantity)) 
print("I want {1} pieces of {0}".format(item,quantity))
print("I Want {} pieces of {} by {}AM".format(item,quantity,2))

#OutPut
#Enter item  eggs
#Enter quantity 12
#I Want  eggs,I want 12 pieces of items
#I want 12 pieces of  eggs
#I Want eggs pieces of 12 by 2AM