def dirReduc(arr):
    n = len(arr)
    # for x, y in zip(arr, arr[1:]):
    #     print(x, y)
    for i in range(0, n-2):
        if arr[i] == 'NORTH' and arr[i+1] == 'SOUTH':
            print(arr[i:i+2])
            #arr.pop(i:i+1)
            next = arr.splice(i, i+2)
            print(next)
            #arr.pop(i+1) indices would change so i = 2 becomes i = 1 and removes third instead of second
            #arr.remove(arr[i:i+1])
            #arr.remove(arr[i+1])
            # i = i-2
            # n = n-2
            #print(arr)
    return arr

a = ["NORTH", "SOUTH", "NORTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print(dirReduc(a))
