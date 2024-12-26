#example 1
  
# strip() is used to remove before and after sapces or other elements of string
name = "& Hello Rohit hari preetham &"  
print(name)  # Output: & Hello Rohit hari preetham &
print(len(name))  # Output: 31 (length of the original string, including all characters)
print(len(name.strip()))  # Output: 29 (before and afterspaces are removed)
print(len(name.rstrip()))  # Output: 31 (only before spaces are removed, but none exist in this case)
print(len(name.lstrip()))  # Output: 31 (only after spaces are removed, but none exist in this case)
changed = name.strip("&")  # Removes '&' characters from both ends
print(changed)             # Output:  Hello Rohit hari preetham 

#example 2
sample="    BansidharKandula   "
print(len(sample))
modified=sample.strip()
print(modified)
print(sample.strip(" ").lower()) # first removes the spaces and converts to lower case
print(sample.strip().upper()) # first removes the spaces and conversts to uppercase

#Example 3

sample1="alpple&mango&orange&grapes "
changed1=sample1.split("&")#Splits the string into a list wherever the character & appears.
print(changed1)
