def Factorial(iNo):
    iFact = 1

    while(iNo >= 1):
        iFact = iFact * iNo
        iNo = iNo -1
        
    return iFact   

def main():
    print("Enter number : ")
    iValue = int(input())
    iRet = Factorial(iValue)
    print(iRet)

if __name__ == "__main__":
    main()

'''

C:\Users\SWEETY\OneDrive\Desktop\Python_Assignments\Assignment_2>python 2_3.py
Enter number :
5
120

C:\Users\SWEETY\OneDrive\Desktop\Python_Assignments\Assignment_2>

'''