# Title: My Document #

This is my document. It is a good document. I love this document for the following reasons (in no particular order):

* It uses Markdown
* It has examples of basic Markdown
* There is no third bullet point

## Header Level 2 ## 

A subsection: subservient to the main section. Less than equal. Aspects of a subsection include (in this particular order):

1. It's beneath its parent
2. That's about it

And that needs some *emphasis*! Maybe even some **BOLDING**!

# A Table #

Here's a table:

| Column 1  | Column 2  |
|-----------|-----------|
| 1         | A         |
| 2         | B         |
| 3         | C         |

# Conversion #

If you save this as example.md, you can turn this file into a DOCX by typing this in the command line:

> pandoc -f markdown -t docx -o test.docx example.md