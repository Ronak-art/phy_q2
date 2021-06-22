def binary_search(to_src, array, ind1, indL):
    if ind1 <= indL:
        mid = int((ind1+indL)/2)
        if to_src == array[mid]:
            return mid
        elif to_src > array[mid]:
            return binary_search(to_src, array, mid, indL)
        else:
            return binary_search(to_src,array,ind1, mid)
    else:
        return "fff"

inside = input("Give Your Word: ")
array = []
array2 = []
array[:0] = inside
array2[:0] = inside
print(array)
array.sort()
print(array)
to_src = input("Give a letter you want to search: ")
output = binary_search(to_src, array, 0, len(array)-1)

if output != "fff":
    print(array2)
    letter = (array[output])
    print(array2.index(letter))
else :
    print("Not present in word!")








#x = input("give for x ")
#if(x>'e'):
#    print(x + " is greater than e")
#elif(x<'e'):
#    print('can be a b c and d')
#else:
#    print("it is e")