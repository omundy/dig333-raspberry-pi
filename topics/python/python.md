← [Raspberry Pi](../../README.md)

<a href="../../README.md"><img width="150" src="../../assets/img/RPi-Logo-Reg-SCREEN.webp"></a>

# Python





## Python + Command Line

At the prompt, just type `python3` to enter the interpreter. Then type commands and enter to run them

```python
>>> sum = 1+1
>>> print(sum)
>>> # -> 2
```

To exit, just type `exit()`


Or, run a file from the command line:

```bash
python file.py
```




## Modularity


Anytime you find yourself rewriting the same code consider using a function to make it reusable:

```python
# define the function
def say_hello():
	return "hello world!"
# print the data return from the function
print(say_hello())
# -> hello world!
```

Functions can provide different results depending on parameters:

```python
def odd_even(num):
	if (num % 2) == 0:
		return "The number is even"
	else:
		return "The number is odd"

print(odd_even(2000))
# -> "The number is even"
print(odd_even(79))
# -> "The number is odd"
```


Consider also storing functions in separate files to keep your code clean:

```python
# functions.py
# contains the above two functions

# main.py
import functions as f
print(f.say_hello())
print(f.odd_even(201))
# -> hello world!
# -> "The number is odd"
```
