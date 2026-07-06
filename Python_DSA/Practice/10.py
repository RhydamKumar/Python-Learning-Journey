# Create a dictionary of three friends and their phone numbers. Use:

# keys() to get all names
# values() to get all numbers
# items() to loop over key-value pairs and print them
mydict = {
    "Harry": 9090909090,
    "John Doe": 99889988,
    "Donald Trump": 454545
}

print(mydict.keys())
print(mydict.values())

for key, value in mydict.items():
    print(key, value)