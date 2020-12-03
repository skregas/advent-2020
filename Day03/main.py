# input: a map of the slope, complete with trees!
# map repeats to the right
# slope: right 3, down 1
# output: how many trees do yoi encounter on your way down the mountain?

# each row on the map is 32 characters
# each row repeats itself if needed
# if reach the end of the row while going right, continue counting from the beginning of the same row
# if reach the end of the row while going down, . . would you? Just go the next row

# read from the file two rows
# to start, read row 0 and row 1
# then go right 3 in row 0, and down 1 into row 1 at the same position
# to continue, read the NEXT ROW (not the next two)
# then go right 3 in row 1 (current row) and down 1 into row 2 (the new row)

# at the end of each movement, (right 3, down 1), investigate the character at that position
# if ".": safe
# elif "#": hit a tree! add it to the tree count
# in both cases, continue on

# continue reading, moving and counting trees until input is exhausted

def traverse(input, dx, dy):
    trees_count = 0
    
    with open(input) as f:
        l = [line.strip() for line in f.readlines()]
        toboggan_x, toboggan_y = dx, dy
        while toboggan_y < len(l):
            if toboggan_x >= len(l[0]):
                toboggan_x = toboggan_x % len(l[0])
            if l[toboggan_y][toboggan_x] == '#':
                trees_count += 1
            toboggan_y += dy
            toboggan_x += dx
    return trees_count


if __name__ == "__main__":
    print("Number of trees encountered: ", traverse("input.txt", 3, 1))

    print("Total number of trees hit on all slopes: ", traverse("input.txt", 1, 1) * 
            traverse("input.txt", 3, 1) * 
            traverse("input.txt", 5, 1) * 
            traverse("input.txt", 7, 1) * 
            traverse("input.txt", 1, 2))