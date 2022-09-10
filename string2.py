Python 3.4.4 (v3.4.4:737efcadf5a6, Dec 20 2015, 19:28:18) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print("hello everyone.\n","my name is lps")
hello everyone.
 my name is lps
>>> print("hello everyone.\t","my name is lps")
hello everyone.	 my name is lps
>>> print("hello everyone","myself lps", sep=',')
hello everyone,myself lps
>>> print("hello everyone","myself lps","how are you" sep=',')
SyntaxError: invalid syntax
>>> print("hello everyone","myself lps","how are you", sep=',')
hello everyone,myself lps,how are you
>>> print("hello everyone","myself lps","how are you", end='     ')
hello everyone myself lps how are you     
>>> print("hello everyone","myself lps","how are you", end='\n')
hello everyone myself lps how are you
>>> 
