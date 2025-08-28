#Task1 :read a file and handled errors

try:
    # try to open the file
    with open("sample.txt", "r") as file:
         print("reading file content:/n")
         # print each line with line numbers
         for idx, line in enumerate(file, start=1):
             print(f"line{idx}: {line.strip()}")

except FileNotFoundError:
     #handle case if file does not exist
    print("error: the file 'sample.txt' was not found")

# Task 2: Write and Append Data to a File

# Step 1: Write user input to the file
text_to_write = input("Enter text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(text_to_write + "\n")
print("Data successfully written to output.txt.")

# Step 2: Append additional data to the file
text_to_append = input("Enter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(text_to_append + "\n")
print("Data successfully appended.")

# Step 3: Read and display final content
print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    content = file.read()
    print(content)


