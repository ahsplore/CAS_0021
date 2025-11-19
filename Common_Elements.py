def common_elements(a,b):
    c = []
    for x in a:
        if x in b and x not in c:
            c.append(x)
    return c

list_1 = [1, 2, 3, 4]
list_2 = [3, 4, 5, 6]
result = common_elements(list_1, list_2)

print(f"List 1: {list_1} \nList 2: {list_2}")
print(f"Common elements: {result}")