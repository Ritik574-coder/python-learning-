# set methon 
# set.add(el) adds an element
collecation = set()
collecation.add(1)
collecation.add("ritik")
collecation.add("riya")
collecation.add(2.4)
collecation.add(2)
# collecation.add(["ritik"]) TypeError: unhashable type: 'list'
print(collecation)
print(len(collecation))
# set.remeve(el) remove the elemant
collecation.remove(2)
print(collecation)
# set.claer(el) empties the set 
collecation.clear()
print(len(collecation))
# set.pop() removes a random value
set_pop = {"ritik","riya","divya","muskan","ai","python","space","fussion reactor","quantom cumputer"}
set_pop.pop()
print(set_pop)
set_pop.pop()
print(set_pop)
print(set_pop.pop())
print(set_pop.pop())
print(set_pop.pop())
# set.union(set2)  comdines both set values & returns new 
set1 = {"ritik","ritik","riya",65,46,65,45,87}
set2 = {65.65,87,"riya","ritik"}
print(set1.union(set2))
# set.intersection(set2) combine common values & returns new 
print(set1.intersection(set2))