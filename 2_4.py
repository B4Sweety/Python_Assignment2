def Add(iNo):
    iSum = 0

    for i in range(1,iNo+1):
        iSum = iSum + i
    return iSum    

def main():
    iValue = int(input())
    iRet = Add(iValue)
    print(iRet)

if __name__ == "__main__":
    main()