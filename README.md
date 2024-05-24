# Introduction:

This is a formatter that splits paragraphs in the Project Gutenberg texts. It is minimalistic, and outputs the paragraphs to the `formatting.json` file.

# Instructions:

1. Create a `secrets_list.py` file, and put the following code in it. Add as many files as you want, and replace <FILE_NAME> with your filename without the <>:

```python
files = [
    "<FILE_NAME>.txt",
    "<FILE_NAME>.txt"
]
```

2. Create a directory called `texts` and put the files in that directory

3. Create an empty file called `formatting.json`

4. Run the python file `paragraph_formatter.py`

5. Enjoy.

# License

MIT License

Copyright (c) [2024] [Robert Sun]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.