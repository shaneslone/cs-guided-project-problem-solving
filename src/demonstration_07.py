"""
Challenge #7:

Given a string of lowercase and uppercase alpha characters, write a function
that returns a string where each character repeats in an increasing pattern,
starting at 1. Each character repetition starts with a capital letter and the
rest of the repeated characters are lowercase. Each repetition segment is
separated by a `-` character.

Examples:
- repeat_it("abcd") -> "A-Bb-Ccc-Dddd"
- repeat_it("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
- repeat_it("cwAt") -> "C-Ww-Aaa-Tttt"
"""
def repeat_it(input_str):
    if len(input_str) == 0:
        return ""
    input_list = list(input_str)
    result_list = []
    for reps, char in enumerate(input_list):
        # repeated_char = ""
        # for _ in range(reps + 1):
        #     repeated_char += char
        repeated_char = char * (reps + 1)
        repeated_char = repeated_char.capitalize()
        result_list.append(repeated_char)
    return "-".join(result_list)

print(repeat_it("RqaEzty"))



