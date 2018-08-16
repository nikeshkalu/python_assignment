from pathlib import Path

import markdown

inpPath = Path(input("enter the input path with file name: "))
out = Path(input("enter the output path only: "))
outFile = input("enter the output file name: ")
outPath = str(out) + "/" + outFile

if inpPath.exists() == True and out.exists() == True:
    markdown.markdownFromFile(str(inpPath), outPath)
else:
    print("path wrong")
