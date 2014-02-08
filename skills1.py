# Things you should be able to do.

# Write a function that takes a list and returns a new list with only the odd numbers.
def all_odd(some_list):
  # Check for valid input.

  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  # If you're deleting stuff from a list, be careful! 
  # Iterate backwards so that you don't mess up the index.

  # Don't forget the craziness with memory. 
  # list.reverse() doesn't return anything!

  # reversed_list_index = range(len(some_list))
  # reversed_list_index.reverse()
  # The one below is shorter/nicer -- we recreated this in Exercise 4! :D
  reversed_list_index = range(len(some_list))[::-1]

  for element_index in reversed_list_index:
    # print "\n"
    # If element is not of type int, remove element. 
        # print "element index: ", element_index
        # print "element: ", some_list[element_index]

    if type(some_list[element_index]) == int:
      # print some_list[element_index], type(element_index)
      if some_list[element_index] % 2 == 0:
        del some_list[element_index]
      
    # Deletes strings that are numbers. Hm...prompt is a bit vague. 
    elif type(some_list[element_index]) != int:
      del some_list[element_index]

    else:  
      # For each char in the element
      for char in some_list[element_index]:
        # If element is not a number, remove element.
        if char not in numbers:
              # print "deleting %r" % some_list[element_index]
          del some_list[element_index]
          break 

  return some_list

# print all_odd([17, 21, "ha", 7, "yo", 2, 48, "two4you", 9, ' ', "8", "#"])

# Write a function that takes a list and returns a new list with only the even numbers.
def all_even(some_list):
  reversed_list_index = range(len(some_list))[::-1]
  for element_index in reversed_list_index:

    if type(some_list[element_index]) == int:
      if some_list[element_index] % 2 != 0:
        del some_list[element_index]
    else:  
      del some_list[element_index]

  return some_list

# Well shit, I totally overcomplicated the previous...things that happen when I don't pair program. 
# print all_even([17, 21, "ha", 7, "yo", 2, 48, "two4you", 9, ' ', "8", "#"])

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.

# Oh, whaaat. I totally was not creating new lists in the prior problems because 
# that's not memory efficient. 
def long_words(word_list):
  new_word_list = []

  for i in word_list:
    if type(i) == str:
      if len(i) >= 4:
        new_word_list.append(i)
  return new_word_list

# print long_words(["yo", 'ka', 'noooooooooo', 'this is long', 'sho', 8, 3])

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(some_list):
  smallest_element = some_list[0]

  for i in some_list:
    if type(i) == int: 
      if i < smallest_element:
        smallest_element = i
  return smallest_element

# print smallest([4, 7, 3985, 2, 9, 1, 1, 98])

# Write a function that finds the largest element in a list of integers and returns it.
def largest(some_list):
  largest_element = some_list[0]

  for i in some_list:
    if type(i) == int: 
      if i > largest_element:
        largest_element = i
  return largest_element

# print largest([4, 7, 3985, 2, 9, 1, 1, 98])

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(some_list):
  new_list = []

  for i in some_list:
    if type(i) == int or type(i) == float:
      new_list.append(float(i)/2)
  return new_list

# print halvesies([1, 2, 3.0, 4, 9.0, 8])

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    length_list = []

    for word in word_list:
      if type(word) == str:
        length_list.append(len(word))
      else: 
        print "%r is not a string!" % word
        break

    return length_list

# print word_lengths(["yo", 'ka', 'noooooooooo', 'this is long', 'sho', 8, 3])

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(numbers):
    summed_numbers = 0

    for num in numbers: 
      summed_numbers += num
    return summed_numbers

# print sum_numbers([2, 2, 10])

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(numbers):
    multiplied_numbers = 1

    for num in numbers: 
      multiplied_numbers *= num
    return multiplied_numbers

# print mult_numbers([2,2,10])

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(string_list):
    joined_string = ''
    for string in string_list:
      if type(string) != str:
        print "%r is not a string!" % string
        break
      else:
        joined_string += string 
          # for char in string: 
          #   joined_string += char
    return joined_string

# print join_strings(['yo', 'ha', 'he', 'ho', 'no'])

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(numbers):
    return None
