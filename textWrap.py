import textwrap

# https://www.hackerrank.com/challenges/text-wrap/problem


def wrap(string, max_width):
    mylist = []
    mystring = ""
    for x in range(0, len(string), max_width):
        variable = string[x:x+max_width]
        mylist.append(variable)

    mystring = "\n".join(mylist)
    return mystring       


if __name__ == '__main__':
    string, max_width = raw_input(), int(raw_input())
    result = wrap(string, max_width)
    print(result)