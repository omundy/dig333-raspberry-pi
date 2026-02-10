← [Raspberry Pi](../../README.md)

<a href="../../README.md"><img width="150" src="../../assets/img/RPi-Logo-Reg-SCREEN.webp"></a>

# Python


## Install Thonny

Thonny for Pico
```
brew install thonny
```



## Install Python


How to [Install Python with UV](https://mac.install.guide/python/install-uv) on Mac. UV for Python version, environment, and package management. UV, an extremely fast all-in-one tool for Python development.

1. Check for [Xcode dev environment ](https://mac.install.guide/commandlinetools/2)
```
xcode-select -p
```

2. Install UV with [Homebrew](https://brew.sh/)
```
brew install uv
```

3. Set the `$PATH` for UV, and the close (VS Code trash can) and open a new shell
```
uv tool update-shell
```

4. Verify UV installation
```
uv --version
# uv 0.8.0 (Homebrew 2025-07-17)
```

5. Install Python with UV
```
uv python install --preview
```

6. Verify Python installation
```
uv python find
```

## Python UV to manage project

```
# Create a new project
uv init dig333-raspberri-pi

# Add dependencies
$ uv add requests

# Sync dependencies with the environment
$ uv sync

# Lock dependencies
$ uv lock

# Run commands in the project environment
$ uv run python script.py

```









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
