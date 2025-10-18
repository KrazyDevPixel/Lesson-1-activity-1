filename = "sigma.txt"

with open(filename, "r") as file:
    original_content = file.read()
print("Original content:")
print(original_content)

with open(filename, "a") as file:
    file.write("\nThis is a newly appended line.")

with open(filename, "r") as file:
    updated_content = file.read()
print("\nUpdated content:")
print(updated_content)

words = updated_content.split()
print("\nWords in the file:")
print(words)

with open(filename, "r") as file:
    content = file.read()
print("=== Exact File Content ===")
print(content)
