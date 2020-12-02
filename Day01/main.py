import os, sys

def two_numbers():
    with open('input.txt') as f:
        items = [s.strip() for s in f.readlines()]
        for item in items:
            difference = 2020 - int(item)
            # print(diffs)
            # print(items)
            if str(difference) in items:
                print(f"{item} + {difference} = ", int(item) + int(difference))
                print(f"{item} * {difference} = ", int(item) * int(difference))
                break


def three_numbers():
    with open('input.txt') as f:
        items = [int(s.strip()) for s in f.readlines()]
        items.sort()
        
        for i in range(0, len(items) - 2):

            l = i + 1
            r = len(items) - 1
            while(l < r):
                if items[i] + items[l] + items[r] == 2020:
                    print(f"Triplet is: {items[i]} + {items[l]} + {items[r]}")
                    print(f"Product is: ", items[i] * items[l] * items[r])
                    return True
                elif items[i] + items[l] + items[r] < 2020:
                    l += 1
                else:
                    r -= 1


if __name__ == "__main__":
    three_numbers()