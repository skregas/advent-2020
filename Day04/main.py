
# Guesses:
# 189 (too low)
# 215 (too high)
# 203 (too high)
# 195 (not right)
# 188 !!!
# """
import re
def test_pid(x):

    return True if re.match(r"^\d{9}$", x) else False

def test_ecl(x):

    return True if re.match(r"amb|blu|brn|gry|grn|hzl|oth", x) else False

def test_hcl(x):
    return True if re.match(r"\#[0-9a-f]{6}", x) else False

def test_hgt(x):
    if "cm" in x:
        x = x.strip('cm')
        return True if int(x) >= 150 and int(x) <= 194 else False
    elif "in" in x:
        x = x.strip('in')
        return True if int(x) >= 59 and int(x) <= 77 else False

def validate():
    valid = 0
    invalid = 0
    total_invalid = 0
    req_fields = {
        "byr": lambda x: True if int(x) >= 1920 and int(x) <= 2003 else False, 
        "iyr": lambda x: True if int(x) >= 2010 and int(x) <= 2020 else False, 
        "eyr": lambda x: True if int(x) >= 2020 and int(x) <= 2030 else False, 
        "hgt": test_hgt, 
        "hcl": test_hcl, 
        "ecl": test_ecl, 
        "pid": test_pid}

    opt_fields = ["cid"]

    pass_fields = {}
    does_it_pass = []
    with open("input.txt") as f:
        passports = f.read().split('\n\n')
        for passport in passports[:-1]:
            for f_ in passport.split():
                k, v = f_.split(':')
                pass_fields.update({k: v.strip()})
            for field in req_fields.keys():
                if field not in pass_fields.keys():
                    invalid += 1
                    break
                else:
                    # for field in pass_fields, call the corresponding function in req_fields
                    does_it_pass.append(req_fields[field](pass_fields[field]))
            if False in does_it_pass:
                invalid += 1
            if not invalid:
                valid += 1
        
            pass_fields = {}
            does_it_pass = []
            print("Vaild: ", valid)
            total_invalid += invalid
            print("Invalid", total_invalid)
            invalid = 0

    return valid




if __name__ == "__main__":
    # assert validate() == 2
    print(validate())

##### Below is inspiration. NOT MY CODE!! Used to verify the solution above
##### Taken from https://www.reddit.com/r/adventofcode/comments/k74niy/2020_day04python_part_2_solution/

# import typing
# import textwrap
# import re

# Passport = typing.Dict[str, str]
# required_fields: typing.Final[typing.Set[str]] = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
# allowed_eye_colors: typing.Final[typing.Set[str]] = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
# passport_id_pattern: typing.Final = re.compile(r"^\d{9}$")
# height_pattern: typing.Final = re.compile(r"^(\d{3})(cm)$|^(\d{2})(in)$")
# hair_color_pattern: typing.Final = re.compile(r"^#[0-9a-f]{6}$")


# def is_valid_year(value: str, min_allowed: int, max_allowed: int) -> bool:
#     try:
#         return min_allowed <= int(value) <= max_allowed
#     except ValueError:
#         return False


# def is_valid_height(value: str) -> bool:
#     match = height_pattern.match(value)
#     if match is None:
#         return False

#     height, unit = (match for match in match.groups() if match is not None)
#     min_allowed, max_allowed = (150, 193) if unit == "cm" else (59, 76)

#     return min_allowed <= int(height) <= max_allowed


# def is_valid_passport(passport: Passport) -> bool:
#     return (
#         len(required_fields.difference(passport.keys())) == 0
#         and passport["ecl"] in allowed_eye_colors
#         and passport_id_pattern.match(passport["pid"])
#         and hair_color_pattern.match(passport["hcl"])
#         and is_valid_year(passport["byr"], 1920, 2002)
#         and is_valid_year(passport["iyr"], 2010, 2020)
#         and is_valid_year(passport["eyr"], 2020, 2030)
#         and is_valid_height(passport["hgt"])
#     )


# def filter_valid_passports(passports: typing.List[Passport]) -> typing.List[Passport]:
#     return [passport for passport in passports if is_valid_passport(passport)]


# def parse_input(input_str: str) -> typing.List[Passport]:
#     def parse_passport_data(entry_str: str) -> Passport:
#         pairs = entry_str.replace("\n", " ").strip().split(" ")
#         return dict([pair.split(":") for pair in pairs])

#     return [parse_passport_data(passport_raw_data) for passport_raw_data in input_str.split("\n\n")]


# if __name__ == "__main__":
#     with open("input.txt", "r") as f:
#         input_str = f.read()

#     passports = parse_input(input_str)
#     print(f"result = {len(filter_valid_passports(passports))}")