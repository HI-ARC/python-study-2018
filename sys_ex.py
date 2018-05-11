import sys

if(len(sys.argv) > 1):
    f = open(sys.argv[1], 'r')
    content = f.read()
    print(content)
    f.close()
else:
    print("Hello World")
