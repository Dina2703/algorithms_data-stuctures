'''
Returns the index position of the target if found, else returns None
'''
def linear_search(list, target):
  #len(list) is a constant time operation, because it assigns intex to each value inthe list
  for i in range(0, len(list)):
    #the if statement is also a constant time operation, because it checks each value if it matches the target.
    if list[i] == target:
      #if the value mathces the target, we return the index value, beacuse we  need its position
      return i
    #if the entire for loop is executed and we don't hit this return statement, then the target does not exists in the list, so we say None.  
  return None

# even though all our operations run in constant time, in the words case sceanrion this for loop here will have to go through the entire range of values and read every single element in the list, therefore giving the algoritms a Big O value of n ( O(n)or running in linear time )


def verify(index):
  if index is not None:
    print("Target found at index: ", index)
  else:
    print("Target not found in list")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = linear_search(numbers, 12)
verify(result)

result = linear_search(numbers, 3)
verify(result)