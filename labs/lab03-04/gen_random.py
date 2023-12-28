import random

def gen_random(c, a, b):
    return [random.randint(a, b) for c in range(0, c)]

def main():
    print(str(gen_random(5, 1, 3))[1:-1])

if __name__ == '__main__' :
    main()