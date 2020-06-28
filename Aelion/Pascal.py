#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

def pascal_triangle(rang):
    for n in range(rang+1): # On explore les lignes
        if n == 0:
            print(1)
        else:
            for k in range(rang+1): # On explore les colonnes
                 if k == 0:
                     print(1, 1)
                 else:
                     print(n+1, n-1)

print(pascal_triangle(6))
