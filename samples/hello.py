def choose(sequence):
    assert len(sequence) > 0, "empty sequence"
    return sequence[0], sequence[1:]


def sort(l):
    if len(l) < 2:
        return l
    
    pivot, rest = choose(l)
    smaller = [x for x in rest if x <= pivot]
    larger = [x for x in rest if x > pivot]
    return sort(smaller) + [pivot] + sort(larger)


def main():
    print(sort([5, 1, 4, 2, 3]))


if __name__ == '__main__':
    main()

