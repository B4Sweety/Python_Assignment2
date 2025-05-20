def AddDigits(iNo):
    iSum = 0
    iDigit = 0

    while(iNo != 0):
        iDigit = iNo % 10
        iNo = iNo // 10
        iSum = iSum + iDigit

    return iSum    

def main():
    print("Enter number")
    iValue = int(input())

    iRet = AddDigits(iValue)

    print("Addition of digits are : ",iRet)

if __name__ == "__main__":
    main()

'''

C:\Users\SWEETY\OneDrive\Desktop\Python_Assignments\Assignment_2>python 2_10.py
Enter number
5187934
Addition of digits are :  37

C:\Users\SWEETY\OneDrive\Desktop\Python_Assignments\Assignment_2>

'''