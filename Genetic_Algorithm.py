import random

def pick_rand(num):
    
    list2=['0','0','0','0','0']
    list= bin(num).replace("b", "")
    x=4
    w=len(list)-1
    for i in range(len(list)):
        list2[x]=list[w]
        w-=1
        x-=1
    return list2
def fitness_of_num(num):
    w=round((pow(-num,2)/10))
    w=w*-1
    w=w+3*num
    return w
def cross_over(list):
    w=random.randint(1,4)
    x=random.randint(1,4)
    
    if w>x:
        temp=w
        w=x
        x=temp
    for i in range(0,len(list),2):
        for j in range(w,x):
            temp=list[i][j]
            list[i][j]=list[i+1][j]
            list[i+1][j]=temp
        
            
    return list
def convert(list):
    w=str(list)
    x=''
    for i in w:
        if i=='0'or i=='1':
            x+=i
    return x

def binaryToDecimal(binary): 

    binary1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    return decimal
def check_fitness(fitness):
    for i in range(len(fitness)):
        if fitness[i]>=23:
            return i
    return -1
def mutate(list):
    w=random.randint(0,4)
    x=random.randint(0,4)
    for i in range(len(list)):
        temp=list[i][w]
        list[i][w]=list[i][x]
        list[i][x]=temp
    return list
def askfitness(number):
    fitness=[]
    for i in range(len(number)):
        fitness.append(fitness_of_num(number[i]))
    return fitness
    
def convertonumbers(list):
    number=[]
    for i in range(len(list)):
        w=convert(list[i])
        number.append(binaryToDecimal(int(w)))

    return number
    
    
def main_function():
    list=[]
    number=[]
    fitness=[]
    
    for x in range(10):
        num=random.randint(0,31)
        number.append(num)
        list.append(pick_rand(num))
        fitness.append(fitness_of_num(num))
    w=check_fitness(fitness)   
    if w!=-1:
        print(list[w],"   ",fitness[w],"   ",number[w])
    else:
        num=1
        while True:
            list=cross_over(list)
            number=convertonumbers(list)
            fitness=askfitness(number)
            w=check_fitness(fitness)
            if w!=-1:
                print(list[w]," The fitness of binary number is   ",fitness[w]," and the number is   ",number[w])
                break
            if num%3==0:
                list=mutate(list)
            num+=1
main_function()

    