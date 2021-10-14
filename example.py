from random import randint

# Looking for element in array here;
def binary_search(arr,ele):
# here we're initializing our array/list to 0
    first = 0
# we subtract one to make sure we get the last indices
    last = len(arr) - 1 
    found = False
# We start looping here
    while first <= last and not found:
# if not found, we calculate midpoint 
        mid = int((first+last)/2)
        print("first: %s; last: %s; mid: %s" % (first, last, mid))
# this is where we compare the midpoint to the element; if true, done
        if arr[mid] == ele:
            found = True
# if the midpoint != element, we compare again
        else:
            if ele<arr[mid]:
# this updates the value of last
                last = mid -1
            else: 
                first = mid + 1
    return found

# if youre going to run this file as a script, do this:
if __name__ == "__main__":
# if you're going to run this value, do this:
    mylist = [randint(0, 100) for _ in range(100)]
    mylist.sort()
    search_value = 50
    out = binary_search(mylist, 50)
    print("The value was found: %s" % out)
