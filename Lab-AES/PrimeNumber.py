from random import randint
def Prime_seq(num):
    prime_list = []
    for i in range(2,num):
        if prime(i) == True:
            prime_list.append(i)
        else:
            pass

    return prime_list

num = int(input("Enter the range: "))
prime = lambda num: all( num%x != 0 for x in range(2, int(num**.5)+1) )
print_list = Prime_seq(num)

print(print_list[randint(0,len(print_list))])