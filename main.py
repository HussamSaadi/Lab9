


def encode(password):
    new_pass = []
    for item in password:
        item += 3
        new_pass.append(item)
    return new_pass


def main():


    print(encode([1, 2, 3, 4, 5, 6, 7, 8, 9]))


if __name__ == '__main__':
    main()