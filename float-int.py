from colorama import init, Fore, Style, Back

init()


number = 19
a = 4
b = 3
# c will return a integer
c = number // a
d = number / a
e = number % a
print(f'c is {c} and of type {type(c)}')
print(Fore.GREEN)
print(f'some green text{c}')
print(Style.RESET_ALL)
print(Style.DIM + f'd is {d} and of type {type(d)}')
print(Style.RESET_ALL)
print(f'e is {e} and of type {type(e)}')
