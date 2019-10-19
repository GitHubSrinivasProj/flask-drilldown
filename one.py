# #one.py
#
#
# def func():
#     print("func() in one.py")
#
# print("top level in one.py")
#
#
#
# if __name__ == '__main__':
#     print('one.py is being run directly')
# else:
#     print('one.py is being imported!')

def latin_name(name):
    name = list(name)
    if(name[len(name)-1]!='y'):
        name = ''.join(name)
        print(name+'y')
    else:
        name[len(name)-1:] = ['i','f','u','l']
        name = ''.join(name)
        print(name)

latin_name('sporty')
