def main():
    print ("Binary Search")
    elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 7
    print(binary_search(elements, target))


def binary_search(elements, target):
    # binary search set the start and end of the list
    step = 0 # to count the number of steps
    start = 0
    end = len(elements) - 1
    print ('looking for ', target, ' in ', elements)
    while start <= end:
        step += 1
        mid = (start + end) // 2
        print ('start:', start, 'end:', end, 'mid:', mid, 'step:', step, 'elements[mid]:', elements[mid], 'elemenst[start:end]', elements[start:end+1])
        if elements[mid] == target:
            return True
        elif elements[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return False


if __name__ == "__main__":
    main()