from pathlib import Path
# -- Constant with the new of the file to open
FILENAME = "sequences/ADA_sequence.fa"
# -- Open and read the file
file_contents = Path(FILENAME).read_text()

list_contents = file_contents.split("\n")
list_contents.pop(0) # remove header

print(len(''.join(list_contents)))

#other option
index = file_contents.find('\n')
file_content2 = (file_contents[index:]).replace('\n', '')
print(len(file_content2))