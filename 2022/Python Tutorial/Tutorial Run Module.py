Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:\Users\HP\Desktop\PythonTut\Tut1\Tutorial1.py
>>> print(i fori in range(1,11))
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print(i for i in range(1,11))
<generator object <genexpr> at 0x000001700580FAC0>
>>> arr = [i for i in range(1,11)]
>>> print arr
SyntaxError: incomplete input
>>> print(arr)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
