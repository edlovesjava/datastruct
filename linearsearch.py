def main():
    print ("Linear Search")
    elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 5
    print(linear_search(elements, target))


def linear_search(elements, target):
    for element in elements:
        if element == target:
            return True
    return False


if __name__ == "__main__":
    main()