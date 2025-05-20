def Display(iNo):
    for i in range(1, iNo+1):
        
        for j in range(1, iNo+1):
            if(i >= j):
                print(j, end=" ")
        print()    

def main():
    print("Enter number : ")
    iValue = int(input())

    Display(iValue)

if __name__ == "__main__":
    main()

'''

C:\Users\SWEETY\OneDrive\Desktop\Python_Assignments\Assignment_2>python 2_8.py
Enter number :
5
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

C:\Users\SWEETY\OneDrive\Desktop\Python_Assignments\Assignment_2>

'''