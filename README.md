# Lines merger

## What for?

An OCR program such as FineReader recognizes the text in the image and creates a pdf file where the line breaks correspond to the line breaks in the original image. In the hyphenation places, which are located inside the word, the program puts a special character called "soft hyphen". 

The program in this repository takes the text extracted from the pdf and stitches the lines together when it sees an intra-word hyphenation. 

In addition, since this program is designed to work on a project to digitize a Russian novel, the program removes improbable characters for 19th century Russian text.

## How to?

1. You must extract the text from the pdf file. One way you can do this:

```python

import pdftotext

# Load your PDF
with open("file.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)

# Save all text to a txt file.
with open('file.txt', 'w') as f:
    f.write("\n====page====\n".join(pdf))
```

2. You have to run the script on the command line and set the folder where the txt files are located as a parameter:

`python merge.py plain_text`

3. The script will create the same folder with the processed files and add a suffix `_merged`.

## Examples

See [source](examples/plain_text) and [target](examples/plain_text_merged).
