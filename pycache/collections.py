
#list-ordered,mutable,allow duplicates,[]
'''
person=["ramu", "latha", "hema", "neha", "apple"]
#person.append("prakruthi")
#person.remove("ramu")
#person.insert(2,"adwi")
#person.pop(1)
#person.extend(["hemesh", "swarna"])
#person.sort()    -descending order
#person.reverse()
#person.clear()
r=person.count("apple")
print(r)
r=person.index("neha")
print(r)
'''
#tuple-ordered,immutable,allow duplicates,() 
'''
fruits=("apple", "kiwi", "sapota", "mango")
#r=fruits.index("kiwi")
r=fruits.count("mango")
print(r)
'''
#dictionary-ordered, mutable, allow duplicates in values only,{}.
'''
dict={"name":"prakruthi", "id":90, "month":"oct", "salary":90}
r=dict.keys()
r=dict.get("name")
r=dict.values()
r=dict.items()
dict.update({"country":"india"})
r=dict.pop("name")
dict.clear()
dict.setdefault("country","india")
print(dict)
'''
#set- unordered, mutable, no duplicates allowed,{}

'''
set={1, 2, 4, 5}
set1={1, 2, 4, 9}
#set.add(9)
#set.remove(2)
#set.discard(2)
#r=set.issuperset(set1)
print(r)
'''