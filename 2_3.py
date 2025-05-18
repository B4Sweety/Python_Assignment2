def Factorial(iNo):
    iFact = 1

    while(iNo >= 1):
        iFact = iFact * iNo
        iNo = iNo -1
        
    return iFact   

def main():
    iValue = int(input())
    iRet = Factorial(iValue)
    print(iRet)

if __name__ == "__main__":
    main()