# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

list_1 = [1,-3,6,-2,-5]

def biggie(arr):
    for i in range(len(arr)):
        if arr[i]>=0:
            arr[i] = "big"
        elif arr[i]<0:
            arr[i] = arr[i]
    return arr
print(biggie(list_1))

# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values.
# (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

nums = [0,7,-4,9,2,-2,-3,4,2,1]

def count(arr):
    sum = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            sum +=1
    arr[len(arr)-1] = sum
    return arr

print(count(nums))

# Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

the_list = [1,3,5,16]

def sum_total(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum
print(sum_total(the_list))

# Average - Create a function that takes a list and returns the average of all the values.x
# Example: average([1,2,3,4]) should return 2.5

the_list = [1,3,5,16]

def sum_total(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    avg = sum/len(arr)
    return avg
print(sum_total(the_list))

# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

my_list = [1,2,3,5]

def length(arr):
    return len(arr)

print(length(my_list))

# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. 
# If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False
my_list = [-1,3,-6,9,2]

def mini(arr):
    if len(arr)>0:
        minimum = arr[0]
        for i in range(len(arr)):
            if minimum > arr[i]:
                minimum = arr[i]
        return minimum
    else:
        return False
print(mini(my_list))

# Maximum - Create a function that takes a list and returns the maximum value in the list. 
# If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

my_list = [-4,17,6,9,12]

def maxi(arr):
    if len(arr)>0:
        maximum = arr[0]
        for i in range(len(arr)):
            if maximum < arr[i]:
                maximum = arr[i]
        return maximum
    else:
        return False
print(maxi(my_list))

# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal,
#  average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return
#  {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

this_list = [1,3,6,9,3,7]
def ultimate(arr):
    maximum = arr[0]
    for i in range(len(arr)):
        if maximum < arr[i]:
            maximum = arr[i]
    minimum = arr[0]
    for i in range(len(arr)):
        if minimum > arr[i]:
            minimum = arr[i]
    sum = 0
    for i in range(len(arr)):
                sum += arr[i]
    avg = sum/len(arr)
    return {"sumTotal":sum,"average":avg,"minimum":minimum,"maximum":maximum,"length of the list":len(arr)}

print(ultimate(this_list))

# Reverse List - Create a function that takes a list and return that list with values reversed.
#  Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

the_list = [1,3,6,8,9,10,15]

def reverse(arr):
    for i in range(int(len(arr)/2)):
        arr[i],arr[len(arr)-1-i] = arr[len(arr)-1-i], arr[i]
        print(arr)

reverse(the_list)