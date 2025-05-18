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
