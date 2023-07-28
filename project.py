person1 = {
    'name':'ali',
    'family':'alave',
    'age':20,
    'number':9114445678,
    'reshte':'computer',
    }
person2 = {
    'name':'saeed',
    'family':'alave',
    'age':19,
    'number':9115545678,
    'reshte':'bargh',
    }
person3 = {
    'name':'jafar',
    'family':'alave',
    'age':11,
    'number':9113345678,
    'reshte':'parastari',
    }
person4 = {
    'name':'ajdar',
    'family':'alave',
    'age':19,
    'number':9111145678,
    'reshte':'computer',
    }
person5 = {}
#1
print(person2)

print("-"*80)
#2
print( person2 == person3)
person2 = person3
print( person2 is person3)

print("-"*80)

#3
person4.pop('reshte')
print("New Dict :",person4)

values = list(person4.values())
print("Values:",values)

keys = (person4.keys())
print("Keys :",keys)

print("-"*80)

#4
person1['number'] = 9114440000

person1['family'] = 'Akhavan'

print(person1)

print("-"*80)

#5
print("Enter the inputs :")
person5 = {"name":(input("name:")),"family":input("family:"),"age":int(input("age:")),"number":int(input("number:")),"reshte":(input("reshte:"))}
print("person5:",person5)