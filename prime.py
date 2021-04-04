import time
import tracemalloc

def prime(n):
    tracemalloc.start()
    t0 = time.perf_counter()
    data = [True] * (n//2)
    for i in range(3, int(n**0.5), 2):
        if data[i//2]:
            x = i*i
            while x < n:
                data[x//2] = False
                x += i*2
    #print(2, end="")
    count = 1
    for i in range(1, n//2):
        if data[i]:
            count += 1
            #print(", ", i*2+1, end="")
    t = time.perf_counter()
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('filename')
    print("%d primes found under %d." %(count, n))
    print("Using %f seconds." %t)
    print(top_stats)

def prime2(n):
    tracemalloc.start()
    t0 = time.perf_counter()
    none_prime = {2}
    for i in range(3, int(n**0.5), 2):
        if not i in none_prime:
            for x in range(i*i, n+1, i+i):
                none_prime.add(x)
    count = 1
    for i in range(3, n+1, 2):
        if not i in none_prime:
            count += 1
    t = time.perf_counter() - t0
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('filename')
    print("%d primes found under %d." %(count, n))
    print("Using %f seconds." %t)
    print(top_stats)
    

prime2(1000000)