import textwrap

def wrap(string, max_width):
    newstring = []
    newstring = string.split(" ",max_width)
    print( newstring )


wrap('ABCDEFGHIJKLIMNOQRSTUVWXYZ', 4)

# if __name__ == '__main__':
#     string, max_width = raw_input(), int(raw_input())
#     result = wrap(string, max_width)
#     print(result)