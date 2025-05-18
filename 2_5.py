def DisplayPrime(iNo):

    if iNo > 1 :
        for iCnt in range (2,iNo):
            if ((iNo % iCnt) == 0) :
                print("Not a prime number")
                break
        else:
            print("Prime number")
    else:
        print("Not a prime number")     

def main():
    print("Enter a number: ")
    iValue = int(input())

    DisplayPrime(iValue)

if __name__ == "__main__":
    main()