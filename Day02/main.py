
def find_passwords(password_line):
    """
    1. split the line into its parts:
    - number of occurances
    - character to count
    - password string

    """

    occurances, char, pass_str = password_line.split()
    char =  char.strip(':')
    # split occurances into min and max
    c_min, c_max = occurances.split('-')

    if (int(c_min) <= pass_str.count(char) <= int(c_max)):
        status = "Valid"
    else: 
        status = "Invalid"
    return status


def find_passwords_by_position(password_line):
    """
    Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. 
    (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) 
    Exactly one of these positions must contain the given letter. 
    Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

    Given the same example list from above:

    1-3 a: abcde is valid: position 1 contains a and position 3 does not.
    1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
    2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c. 

    ----

    1. split the line into its parts:
    - positions of occurances
    - character to find at positions
    - password string     

    use str.find(char), compare to positions
    adjust for no "index zero":
    str.find(char) + 1 == pos_min or == pos_max
    find(), rfind()
    index(), rindex()

    go the other way:
    str[pos_min-1] == char and str[pos_max-1] == char: Invalid
    char not in str: Invalid
    str[pos_min-1] == char or str[pos_max-1] == char: Valid
    """

    positions, char, pass_str = password_line.split()
    char =  char.strip(':')
    # split positions into min and max
    p_min, p_max = positions.split('-')
    p_min = int(p_min)
    p_max = int(p_max)
    if char not in pass_str: status = "Invalid"
    elif pass_str[p_min-1] == char and pass_str[p_max-1] == char: status = "Invalid"
    elif pass_str[p_min-1] == char or pass_str[p_max-1] == char: status =  "Valid"
    else: status = "Invalid"

    return status



if __name__ == "__main__":
    # test
    assert find_passwords_by_position("1-3 a: abcde") == "Valid"
    assert find_passwords_by_position("1-3 b: cdefg") == "Invalid"
    assert find_passwords_by_position("2-9 c: ccccccccc") == "Invalid"

    valid = []
    invalid = []
    with open("input.txt") as f:
        for line in f.readlines():
            if find_passwords_by_position(line) == "Valid": 
                valid.append(line)
            else:
                invalid.append(line)
    print("Count of VALID passwords (by char position): ", len(valid))


    assert find_passwords("3-4 k: kxkk") == "Valid"
    assert find_passwords("2-4 z: czzmzz") == "Valid"
    assert find_passwords("7-8 p: wpppppsp") == "Invalid"

    valid = []
    invalid = []
    with open("input.txt") as f:
        for line in f.readlines():
            if find_passwords(line) == "Valid": 
                valid.append(line)
            else:
                invalid.append(line)
    print("Count of VALID passwords (by char count): ", len(valid))