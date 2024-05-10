a = 3
b = 5

# Store the value of 'a' in a temporary variable
temp = a

# Assign the value of 'b' to 'a'
a = b

# Assign the value stored in the temporary variable to 'b'
b = temp

print(a)  # This will print the value of 'b'
print(b)  # This will print the value of 'a'