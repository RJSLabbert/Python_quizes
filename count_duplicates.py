input_list = ['Apple','Apple','Apple','Banana','Banana','Pear','Pear','Pear']
dup_count = 0
for item in range(len(input_list)-1):
    if input_list[item] == input_list[item+1]:
        dup_count += 1

print(dup_count)        
