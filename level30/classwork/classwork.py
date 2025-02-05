
def add_numbers(a, b):
  return a + b

print(add_numbers(2,4))




def is_even(number):
  if number % 2 == 0:
    return "Even"
  else:
    return "False"
  
print(is_even(16))








def reverse_string(text):
  return text[::-1]

print(reverse_string("Hello, World!"))


def count_vowels(text):
  vowels = "aeiou"
  count = 0
  for i in text:
    if i in vowels:
      count += 1
  return count

print(count_vowels("dachi"))


def is_divisible(a, b):
  if b == 0:
    return False
  else:
    return True
  
print(is_divisible(2, 0))