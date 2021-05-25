import sys, base64

# print help
def print_help():
    print("\n\nBaseConverter Documentation")
    print("\nUsed to convert a given number from a given base to any base under 36 and also 64\n")
    print("Usage: python baseConverter [-h] [number for conversion] [current base of number] [base to be converter]")
    print("\nOptional Arguments:\n-h or --help: prints documentation")
    print("Required Arguments:\n[number to for conversion], [current base of number], [base to be converted]")
    print("Sample Usage: python baseConverter.py 5A857D8E89C 16 10")
    print("Output: 6220586477724")
    print("** A note on base 64. This tool encodes to base 64 as an integer. Most tools encode to base 64 as a string in utf-8 or ascii. If you have problems, that should be the first place to check.**")

def deci_to_base(num, base):
    new_num = ""
    while num > 0:
        digit = int(num%base)

        if digit < 10:
            # add digit to new number
            new_num += str(digit)
        else:
            # convert digits > 10 to letters
            new_num += chr(ord('A') + digit - 10)

        # floor divide num by base
        num //= base
    # reverse string
    
    new_num = new_num[::-1]
    return new_num

def to_base_64(num):
    return base64.b64encode(bytes([num]))

args = sys.argv

# arg1 is number, arg2 is current base of number, arg3 is base of the number to be converted to


# check for -h or --help
if args[1] == "-h" or args[1] == "--help":
    print_help()

# if not, go into main body of code
else:
    # check number of arguments
    if (len(args) != 4):
        print("Incorrect number of arguments!\nCheck documentation with python baseConverter.py -h [or] --help")
        sys.exit()

    # convert number to decimal for ease of use
    length = len(args[1])
    num = int(args[1], int(args[2]))
    new_base = int(args[3])

    # just print the number if we wanted to convert to decimal
    if new_base == 10:
        print(num)
        sys.exit()
    elif new_base == 64:
        print(to_base_64(num))
        sys.exit()

    # print conversion to whatever base we wanted
print(deci_to_base(num, new_base))
sys.exit()