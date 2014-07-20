# Literate Python sample

We'll implement the _quicksort_ algorithm. It's a *fast* sorting algorithm,
with `O(N*log(N))` average time complexity.

Let's start by writing a function to choose the pivot, called `choose`.

```python
def choose(sequence):
    assert len(sequence) > 0, "empty sequence"
    return sequence[0], sequence[1:]
```

Once we have a pivot, we can sort the smaller elements, the larger ones and
finally place the pivot in place.

```python
def sort(l):
    if len(l) < 2:
        return l
    
    pivot, rest = choose(l)
    smaller = [x for x in rest if x <= pivot]
    larger = [x for x in rest if x > pivot]
    return sort(smaller) + [pivot] + sort(larger)
```

And that's it. We can finally test it:

```python
def main():
    print(sort([5, 1, 4, 2, 3]))


if __name__ == '__main__':
    main()
```