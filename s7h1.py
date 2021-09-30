#ATEFE-JELVE__THURSDAY14-18
#FACTORIEL-WHIT-RECURSIVE-DEFINE

def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

print(fact(6))
