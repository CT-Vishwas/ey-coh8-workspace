# Lab: Take n numbers from the user, until he/she enters -999.
# Find the total and average of n numbers excluding -999

total = 0
avg = 0
count = 0
while True:
    num = int(input("Enter the number: "))
    if num == -999:
        break

    total += num
    count += 1


print(f"The sum of numbers is: {total}")
if count != 0:
    avg = total / count
print(f"The average of numbers is: {avg}")