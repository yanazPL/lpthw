i = 0
numbers = []
n = 6


while i < n:
    print(f"At the top i is {i}")
    numbers.append(i)

    i +=1 
    print(f"Numbers now {numbers}")

    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)

def while_loop(i, n):

    while i < n:

        print(f"At the top i is {i}")
        numbers.append(i)

        i +=1 
        print(f"Numbers now {numbers}")

        print(f"At the bottom i is {i}")
    
while_loop(0,10)
numbers = []

def for_loop(i, n):
    for i in range (i, n):
        print(f"At the top i is {i}")
        numbers.append(i)

        print(f"Numbers now {numbers}")

        print(f"At the bottom i is {i}")

for_loop(0, 10)
numbers = []