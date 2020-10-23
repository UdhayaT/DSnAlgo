
def smallestMissingPositiveInteger(arr):
    dict1 = {}

    for i in range (len(inparr)):
        if arr[i] > 0:
            if arr[i] in dict1.keys():
                dict1[arr[i]] += 1
            else:
                dict1[arr[i]] = 1

    print(dict1)
    for i in range (1,200000):
        if i not in dict1.keys():
            return i
    
inparr = [-4,3,6,-1,7,1,2,-9,4,8]

print (smallestMissingPositiveInteger(inparr))


