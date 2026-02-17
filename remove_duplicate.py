def removeDuplicate(input_list):
    exists = set()
    result = []
    for item in input_list:
        if item not in exists:
            result.append(item)
            exists.add(item)
    return result

num = [1,1,1,'a','a',4,5,6,'b','b','c',2,2,2,3,4,4,4,5]
print(removeDuplicate(num))

            
