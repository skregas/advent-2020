

rows = [*range(0, 128)]
columns = [*range(0, 8)]

seat_IDs = []

ret_val = 0
def traverse(l, s):
    if len(l) == 1:
        global ret_val 
        ret_val = l[0]
        return
    i = next(s)
    if i in ["F", "L"]:
        traverse(l[:len(l) //2 ], s)
    if i  in ["B", "R"]:
        traverse(l[len(l) //2: ], s)

with open("input.txt") as f:
    for line in f.readlines():
        line = line.strip()
        seat_row = line[:-3]
        seat_col = line[-3:]
        search_row = (d for d in seat_row)
        searh_columns = (d for d in seat_col)
        
        traverse(rows, search_row)
        print("Row: ", ret_val)
        row = ret_val
        traverse(columns, searh_columns)
        print("Column: ", ret_val)
        col = ret_val
        seat_ID = row * 8 + col
        seat_IDs.append(seat_ID)
        print("Seat_ID: ",seat_ID)

print(max(seat_IDs))
seat_IDs.sort()
# part 2
for n in seat_IDs:
   if n-2 in seat_IDs and n-1 not in seat_IDs:
       print("your seat is: ", n-1)
       break
# print(seat_IDs)
# seat_IDs_minus_front_back = seat_IDs[1:-1]
# print(max(seat_IDs_minus_front_back))