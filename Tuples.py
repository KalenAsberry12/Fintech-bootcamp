# Tuples
t = (1,2,3)

print(t[0])
print()

# consistant number that can not be changed
#credit_card = (123456781234, 'Kalen Asberry', '12/20', 123)

#credit_card2 = (123456781234, 'Kalen Asberry', '12/20', 123)
# stuck in a list
#credit_cards = [credit_card,credit_card2]

#print(credit_cards)

person = ('Nancy-Pants', 25, 'Pizza')
person2 = ('Kalen_shirt', 25, 'Pasta')

people = [person,person2]


#(name, age, favfood) = person
#print(name)
#print(age)
#print(favfood)


#bring in people name age and favfood
for name, age, favfood in people:
  print (name)
  print(age)
  print(favfood)
  print()