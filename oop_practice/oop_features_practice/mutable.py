import copy

o = [5, 2, 7, 9, 0]
p = o[:]

print(o)
print(p)
print(p is o) #False

o[0] = 9
print(o)
print(p)

a = {"Nora": ["055-452-322", "Washington Ave."], "Gino": ["006-545", "5th Avenue"]}
b = a.copy()
c = copy.deepcopy(a)

print(a) # a before changing b

b["Nora"][0] = "56" # b's first element changed

print(a) #it affects a to (shallow copy)
print(b)
print(c) #it doesn't affect c (deep copy)

print("\n \n")



a = [7, 3, 6, 8, 2, 3, 7, 2, 6, 3, 6]
b = a
c = b
b = c
     
def remove_elem(data, target):
	for item in data:
		if item == target:
			data.remove(target)
	return data
     
def get_product(data):
	total = 1
	for i in range(len(data)):
		total *= data.pop()

	return total


remove_elem(c, 3)
print(get_product(b))
print(a)