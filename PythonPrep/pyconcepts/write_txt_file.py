data = ["First, open the text file for writing (or append) using the open() function.",
        "Second, write to the text file using the write() or writelines() method.",
        "Third, close the file using the close() method."]
with open("doc.txt", "w") as f:
        for line in data:
                f.write(line)
                f.write("\n")

with open("doc.txt") as f:
        for line in f:
                print(line)