def run(input, output):
    f = open(input, 'r')
    wr = open(output, 'w')
    try:
        input_string = int(f.readline())
        print(input_string)
    except ValueError:
        return print('Bad String')

if __name__ == '__main__':
    run('input.txt', 'output.txt')
