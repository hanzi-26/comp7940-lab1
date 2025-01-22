def main():
        print("Hello World")
def ex1():
        factors = []
        x = 52633
        for i in range(1, x + 1):
                if x % i == 0:
                        factors.append(i)
        return factors
def print_factor(x):
        factors = []
        for i in range(1, x + 1):
                if x % i == 0:
                        factors.append(i)
        print(factors)
if __name__=='__main__':
        main()
        print(ex1())
        print_factor(52633)
        l = [52633, 8137, 1024, 999]
        for i in range(len(l)):
                print_factor(int(l[i]))
