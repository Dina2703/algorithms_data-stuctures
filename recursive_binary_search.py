#recursive binary search example. A recursive function the one that calls itself.
# in this case our algorithm won't return the index of the target, it will return True if exist or False if does't.

def recursive_binary_search(list, target):
  #if the list is empty, return False. The first stopping condition (to return  False ) is empty list.
  if len(list) == 0:
    return False
  #if the list is not empty, calculate the midpoint and start comparision operation. Since we don't return an index of target, we don't need to use first and last var as we did in Iterative Binary Search example
  else:
    midpoint = (len(list))//2 #the floor division operator
    #if the value at the midpoint.The second stopping condition (to return True), when the target found.
    if list[midpoint] == target:
      return True
    else:
      if list[midpoint] < target:
        #create a sublist starting the midpoint and +1 all the way to the end using slice method, like 'list[midpoint+1:]'
        return recursive_binary_search(list[midpoint+1:], target)
      # else if list[midpoint] greater that tge target
      else:
        return recursive_binary_search(list[:midpoint], target)


def verify(result):
    print("Target found: ", result)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = recursive_binary_search(numbers, 12)
verify(result)

result = recursive_binary_search(numbers, 3)
verify(result)
