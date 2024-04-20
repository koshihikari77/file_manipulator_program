from random import randint

def main():
    min_number = int(input('input min number: '))
    max_number = int(input('input max number: '))

    answer = randint(min_number, max_number)

    while True:
        n = int(input('guess number: '))
        if n == answer:
            print('collect number')
            break
        else:
            print('wrong number')

if __name__ == '__main__':
    main()