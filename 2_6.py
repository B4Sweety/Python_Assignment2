def Display(iNo):
    for i in range(1, iNo+1):
        for j in range(1, iNo+1):
            if(i <= j):
                print("*", end=" ")
        print()    

def main():
    print("Enter number : ")
    iValue = int(input())

    Display(iValue)

if __name__ == "__main__":
    main()

'''
C:\Users\SWEETY\OneDrive\Desktop\Python_Assignments\Assignment_2>python 2_6.py
Enter number :
5
* * * * *
* * * *
* * *
* *
*

C:\Users\SWEETY\OneDrive\Desktop\Python_Assignments\Assignment_2>

'''