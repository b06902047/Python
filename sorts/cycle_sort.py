"""
Code contributed by Honey Sharma
Source: https://en.wikipedia.org/wiki/Cycle_sort
"""

branch_reached = set()

def cycle_sort(array: list) -> list:
    """
    >>> cycle_sort([4, 3, 2, 1])
    [1, 2, 3, 4]

    >>> cycle_sort([-4, 20, 0, -50, 100, -1])
    [-50, -4, -1, 0, 20, 100]

    >>> cycle_sort([-.1, -.2, 1.3, -.8])
    [-0.8, -0.2, -0.1, 1.3]

    >>> cycle_sort([])
    []
    """
    global branch_reached

    array_len = len(array)
    for cycle_start in range(0, array_len - 1):
        branch_reached.add(0)
        item = array[cycle_start]

        pos = cycle_start
        for i in range(cycle_start + 1, array_len):
            branch_reached.add(2)
            if array[i] < item:
                branch_reached.add(3)
                pos += 1
            branch_reached.add(16)
            
        branch_reached.add(4)
        
        if pos == cycle_start:
            branch_reached.add(5)
            continue
        
        branch_reached.add(6)
        
        while item == array[pos]:
            branch_reached.add(7)
            pos += 1
        branch_reached.add(8)

        array[pos], item = item, array[pos]
        while pos != cycle_start:
            branch_reached.add(9)
            pos = cycle_start
            for i in range(cycle_start + 1, array_len):
                branch_reached.add(10)
                if array[i] < item:
                    branch_reached.add(11)
                    pos += 1
                branch_reached.add(12)
            branch_reached.add(13)

            while item == array[pos]:
                branch_reached.add(14)
                pos += 1
            branch_reached.add(15)
            array[pos], item = item, array[pos]
        branch_reached.add(17)
    branch_reached.add(1)
    return array


if __name__ == "__main__":
    assert cycle_sort([4, 5, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert cycle_sort([0, 1, -10, 15, 2, -2]) == [-10, -2, 0, 1, 2, 15]
    print(sorted(branch_reached))
    print(len(branch_reached)/18)
