# read and  thenwrite  in one prgm means same file(r+)
file1 = open("sample filehandilng.py", "r+")

result1 = file1.read()
result2 = file1.write("/n hello my dear") # o/p: in sample filehandilng.py this file
print(result1)
file1.close()

#===============================================================================================
# write and then read in one prgm means same file(w+)
file1 = open("sample filehandilng.py", "w+")

result2 = file1.write("/n hello my dear") # o/p: in sample filehandilng.py this file
file1.seek(0) # Move cursor to the beginning
result1 = file1.read()
print(result1)
file1.close()

"""
How does it work?
- r+ → Opens an existing file for both reading and writing.
- read() → Reads the existing content.
- write() → Writes new content.
- close() → Closes the file.
Important: When you open a file using r+, the cursor initially stays at position 0 (beginning of the file).

After read(), the cursor moves to the end of the file. Therefore, write() adds the new content at the end.

==================================================================================================================
How does it work?
- w+ → Opens a file for both writing and reading.
- Existing content will be deleted when opening the file.
- write() → Writes new content.
- seek(0) → Moves the cursor to the beginning.
- read() → Reads the newly written content.
- close() → Closes the file.
"""
