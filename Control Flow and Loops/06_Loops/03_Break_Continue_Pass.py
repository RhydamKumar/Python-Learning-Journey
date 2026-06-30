# Break
for i in range (1, 10):
    print(i)
    if i == 5:
        break   # This will break the loop when i is equal to 5
    

# Continue
for i in range (1, 10):
    if i == 5:
        continue # This will skip the rest of the loop when i is equal to 5
    print(i) # This will skip printing the number 5
    

# Pass
for i in range(1,5):
    if i == 3:
        pass  # Pass does nothing, just a placeholder
    print(i)  # This will print all numbers from 1 to 4, including 3