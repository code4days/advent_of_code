examples = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen",
]


digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

lines = open("1.in").readlines()
# lines = examples
total = 0
for line in lines:
    found_digits = []
    for left, char in enumerate(line):
        if char.isdigit():
            found_digits.append(char)
            continue
        for digit in digits:
            right = left + len(digit)
            if line[left:right] == digit:
                found_digits.append(digits[digit])
                break
    # print(found_digits[0] + found_digits[-1])
    total += int(found_digits[0] + found_digits[-1])

print(total)
