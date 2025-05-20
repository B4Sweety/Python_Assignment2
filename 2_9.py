def AddDigits(iNo):
    iCnt = 0

    while(iNo != 0):
        iNo = iNo // 10
        iCnt = iCnt + 1
    return iCnt 

def main():
    print("Enter number")
    iValue = int(input())

    iRet = AddDigits(iValue)

    print("Addition of digits are : ",iRet)

if __name__ == "__main__":
    main()

'''

C:\Users\SWEETY\OneDrive\Desktop\Python_Assignments\Assignment_2>python 2_9.py
Enter number
5187934
Addition of digits are :  7

C:\Users\SWEETY\OneDrive\Desktop\Python_Assignments\Assignment_2>

'''