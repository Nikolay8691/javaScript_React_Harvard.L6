import ctypes

kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

# ANSI colors
c = (
    "\033[0m",   # End of color
    "\033[36m",  # Cyan
    "\033[91m",  # Red
    "\033[35m",  # Magenta
    "\033[33m",  # Yellow
    "\033[32m",  # Green
    "\033[34m",  # Blue
)

print(c[1] + '\n hello! colors come from module 7 level 1,' + c[5] + ' tervetuloa hyvät ystävät! \n'+ c[0])

s = input(c[2] + '\n hello, what is your name? '+ c[0])

print(c[3] + '------ it is nice to see you,' + c[2] + f' {s.capitalize()}! ' + c[4] + '------ welcome to L6_projects! '+ c[0])
print(c[6] + ' see you soon! '+ c[0])
# print(c[6] + ' goodbye! '+ c[0])