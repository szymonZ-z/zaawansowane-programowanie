def zlacz(list1: list, list2: list):
    result = list(set(list1+list2))
    return [i**3 for i in result]
print(zlacz([2,3,4,4],[4,3,6]))