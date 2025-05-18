def Add(iNo1, iNo2):
    return iNo1+ iNo2

def Sub(iNo1, iNo2):
    return iNo1 - iNo2

def Mult(iNo1, iNo2):
    return iNo1 * iNo2

def Div(iNo1, iNo2):
    if iNo2 != 0:
        return iNo1 / iNo2
    else:
        return "Error: Division by zero"
