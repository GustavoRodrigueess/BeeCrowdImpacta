N = int(input())
numbers = list()

if N >= 1 and N <= 100:
    for x in range(1, N+1):
        if N % x == 0:
            numbers.append(x)

if len(numbers) > 2:
    print(f'{N} nao eh primo')
elif N == 2:
    print(f'{N} eh primo')
elif N == 1:
    print(f'{N} nao eh primo')
else:
    print(f'{N} eh primo')  
