def Display(iNo):
    for i in range(iNo):
        print("* " * iNo)

def main():
    print("Enter a number: ")
    iValue = int(input())

    Display(iValue)

if __name__ == "__main__":
    main()

