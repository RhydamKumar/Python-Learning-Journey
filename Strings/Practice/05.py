#Take the string "  i love python programming  " and:

# Remove extra spaces from both ends
# Convert it to title case
# Count how many times "o" appears

text = "  i love python programming  "
text1 = text.strip() # Remove extra spaces from both ends
text2 = text.title() # Convert it to title case
count_o = text.count("o") # Count how many times "o" appears
print (text1)
print (text2)
print (count_o)
