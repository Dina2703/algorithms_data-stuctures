#Iterative Binary Search example

def binary_search(list, target):
  first = 0
  last = len(list) - 1

#if we have an empty list the first is greater that last(), and the loop would never execute and we return None(at the bottom, line 17)
  while first <= last:
    midpoint = (first + last)//2 # the // is the floor operator
    
    if list[midpoint] == target:
      return midpoint
    elif list[midpoint] < target:
      first = midpoint + 1
    else:
      last = midpoint -1
  return None



def verify(index):
  if index is not None:
    print("Target found at index: ", index)
  else:
    print("Target not found in list")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = binary_search(numbers, 12)
verify(result)

result = binary_search(numbers, 3)
verify(result)
