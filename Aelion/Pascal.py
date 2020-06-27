#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

def pascal_triangle(n):
    for n in range(n+1):
        if n == 0:
            print(1)
        else:
            for k in range(n+1):
                 if k == 0:
                     print(1, 1)
                 else:
                     print(n+1, n-1)

print(pascal_triangle(6))
