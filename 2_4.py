def Add(iNo):
    iSum = 0

    for i in range(1, (iNo // 2)+ 1):
        if((iNo % i) == 0): 
            iSum = iSum + i
    return iSum    

def main():
    print("Enter number : ")
    iValue = int(input())
    iRet = Add(iValue)
    print(iRet)

if __name__ == "__main__":
    main()

'''

C:\Users\SWEETY\OneDrive\Desktop\Python_Assignments\Assignment_2>python 2_4.py
Enter number :
12
16

C:\Users\SWEETY\OneDrive\Desktop\Python_Assignments\Assignment_2>

'''