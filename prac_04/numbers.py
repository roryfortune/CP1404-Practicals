numbers = [3, 1, 4, 1, 5, 9, 2]

for i in range(5):
    number = int(input("Please enter number: "))
    numbers.append(number)
    print("First number is: ", numbers[0])
    print("Last number is: ", numbers[-1])
    print("Smallest number is: ", min(numbers))
    print("Largest number is: ", max(numbers))
    print("The average of the numbers is: ", sum(numbers) / len(numbers))