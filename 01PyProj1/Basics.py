import math

def circle_stats(radius):
    area = 2*math.pi*radius*radius
    circumfrence = 2*math.pi * radius

    return area,circumfrence

cube = lambda x: x*3

def sum_all(*params):
    return sum(params)

def product_price(**kwargs):
     for key, value in kwargs.items():
            print(key,value)

def even_generator(limit):
     for i in range(2,limit+1,2):
          yield i   

def recursive_ex(num):
    if num == 0 or num ==1: 
        return 1          
    else:
        return num * recursive_ex(num -1)
    
def non_rep_character(inputString):           
        for character in  inputString:
                if inputString.count(character) > 1:
                    continue;  
                else: 
                    return character
                
def fact_using_while(number):
    inputNum = number
    fact = number
    while inputNum > 1:
        fact = fact * (inputNum -1)
        inputNum = inputNum - 1
    return fact
               
            
a,c = circle_stats(5)

print("area in format 1 = {0} Circumfrence = {1}".format(a,c))
print("area in format 2  = %s Circumfrence = %s" % (a,c))
print(f"area in format 3 = {a}, circumfrence = {c}")
print("Cube of 3 Lamda ex= {0}".format(cube(3)))
print("sum of multiple function parameters (1,2,3) = {0}".format(sum_all(1,2,3)))
print("sum of multiple function parameters (4,5,6) = {0}".format(sum_all(4,5,6)))
#Named parameters
print(product_price(phone="Phone", price = 1000))  

for j in even_generator(10):
    print(j)

print(f"Recursive function Example with factorial of 5 ={recursive_ex(5)}")   

print(f"first non-repetive character = {non_rep_character("sandeep")}")

print(f"factorial of 5 is {fact_using_while(6)}")

