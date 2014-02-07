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
    print "\n"
    # If element is not of type int, remove element. 
        # print "element index: ", element_index
        # print "element: ", some_list[element_index]

    if type(some_list[element_index]) == int:
      print some_list[element_index], type(element_index)
      if some_list[element_index] % 2 == 0:
        del some_list[element_index]
      
    else:  
      # For each char in the element
      for char in some_list[element_index]:
        # If element is not a number, remove element.
        if char not in numbers:
              # print "deleting %r" % some_list[element_index]
          del some_list[element_index]
          break 

  # If element is a number, remove if even number.
  # Must create a new reversed_list_index, since we altered some_list. 
  # reversed_list_index = range(len(some_list))[::-1]

  # for element_index in 

  print some_list





all_odd([17, 21, "ha", 7, "yo", 2, 48, "two4you", 9])

# Write a function that takes a list and returns a new list with only the even numbers.
def all_even(some_list):
    return []

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):
    return []

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(some_list):
    return None

# Write a function that finds the largest element in a list of integers and returns it.
def largest(some_list):
    return None

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(some_list):
    return []

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    return []

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(numbers):
    return []

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(numbers):
    return []

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(string_list):
    return ""

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(numbers):
    return None
