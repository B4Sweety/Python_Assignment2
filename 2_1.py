import Arithmatic

def main():
    try:
        iValue1 = float(input("Enter first number: "))
        iValue2 = float(input("Enter second number: "))
        
        print("Addition : ", Arithmatic.Add(iValue1, iValue2))
        print("Subtraction : ", Arithmatic.Sub(iValue1, iValue2))
        print("Multiplication : ", Arithmatic.Mult(iValue1, iValue2))
        print("Division : ", Arithmatic.Div(iValue1, iValue2))
        
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()

'''

C:\Users\SWEETY\OneDrive\Desktop\Python_Assignments\Assignment_2>python 2_1.py
Enter first number: 10
Enter second number: 11
Addition :  21.0
Subtraction :  -1.0
Multiplication :  110.0
Division :  0.9090909090909091

C:\Users\SWEETY\OneDrive\Desktop\Python_Assignments\Assignment_2>

'''