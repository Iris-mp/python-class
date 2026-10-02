#=====================Review overall questions=====================

#Ex. 1
def factorial(n):
    result=1
    for number in range(1,n+1):
        result*= number
    return result
n=int(input("Enter the number:"))
factorial(n)
print(str(n)+"! =",factorial(n))

#Ex.2
def analyze_numbers(n):
    even_counter=0
    sum_even=0
    div_3=0
    for number in range (1,n+1):
        if number%2==0:
            even_counter+=1
            sum_even+=number

        if number%3==0:
            div_3+=1

    print(even_counter,"numbers are even")
    print("All even numbers have a sum of",sum_even)
    print(div_3,"numbers are divisible by 3")

n=int(input("Enter the number to be analyzed: "))
analyze_numbers(n)

#Ex. 3
def number_pattern(n):
    for row in range(1,n+1):
        for number in range(1,n-row+2):
            print(number,end="")
        print()
n=int(input("Enter the number to be analyzed: "))
number_pattern(n)

def number_pattern(n):
    for row in range(n,0,-1):
        for number in range(1,row+1):
            print(number,end="")
        print()
n=int(input("Enter the number to be analyzed: "))
number_pattern(n)

#================Nested loops=====================

#For each iteration of the outer loop, the inner loop completes all of its iterations
# #Ex. 1
for row in range(1,4): #outer loop
    for column in range (1,3): #inner loop
        print("Row:",row,"Column:",column)


#EX. 2

def draw_rectangle(rows, columns):
    for row in range(rows):
        for column in range(columns):
            print("*",end="")
        print()
draw_rectangle(5,5)

#Ex. 3

def triangle(n):
    for row in range(1,n+1):
        for space in range(n-row):
            print(" ",end="")
        for star in range(row):
            print("*",end="")
        print()

num=int(input("Enter a number: "))
triangle(num)

#=================End loops stats=================

#python adds nothing, but output is on the same line
print("X",end="")
print("X",end="")
print("X",end="")

#python adds a space between Xs (end="  ") and output is on the same line
print("X",end=" ")
print("X",end=" ")
print("X",end=" ")
