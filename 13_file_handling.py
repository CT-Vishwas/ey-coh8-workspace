

# with open(r'C:\Users\VishwasKSingh\Workspace\ey-coh8-workspace\01-modes.py', 'r') as fh:
#     data = fh.readlines()

# print(data)

try:
    with open('01-modes.py','x') as fh:
        fh.write("print('This is a Test')")
except FileExistsError:
    print("The file you are trying to write exists")
finally:
    # This will run even if no error occured
    pass