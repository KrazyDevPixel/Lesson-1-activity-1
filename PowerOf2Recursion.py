# Read input
x=int(input("enter a number of animals: "))
y=int(input("enter number of legs: "))
X, Y = map(int, input().split())

# Check if solution is possible
if Y % 2 != 0 or Y < 2 * X or Y > 4 * X:
    print("No")
else:
    # Calculate number of horses
    H = (Y - 2 * X) // 2
    # Calculate number of kangaroos
    K = X - H

    # Extra safety check
    if H < 0 or K < 0:
        print("No")
    else:
        print("Yes")
        print(H, K)
