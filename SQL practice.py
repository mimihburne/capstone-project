import math

def comp(array1, array2):
    array1.sort()
    array2.sort()
    for i in range(0, len(array1)-1):
        if (array1[i])**2 == array2[i]:
            continue
        else:
            return False
    return True
    # if (array1[3])**2 == array2[3]:
    #     return True
    # else:
    #     return False

a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]

a3 = [121, 144, 19, 161, 19, 144, 19, 11]
a4 = [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]

a5 = [121, 144, 19, 161, 19, 144, 19, 11]
a6 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]

print(comp(a5, a6))

