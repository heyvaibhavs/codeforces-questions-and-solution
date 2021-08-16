def strange_sum(numbers):
    sum=0
    for i in numbers:
        if i%3!=0:
            sum=sum+i
    return sum
print(strange_sum(list(range(123))+list(range(77))))