nums = {
        1: "WBO",
        2: "WO",
        3: "WGO",
        4: "WB",
        5: "W",
        6: "WG",
        7: "WBR",
        8: "WR",
        9: "WGR",
        10: "BO",
        11: "O",
        12: "GO",
        13: "B",
        14: "G",
        15: "BR",
        16:"R",
        17:"GR",
        18:"YBO",
        19:"YO",
        20:"YGO",
        21:"YB",
        22:"Y",
        23:"YG",
        24:"YBR",
        25:"YR",
        26:"YGR",
}

print(nums)
roman_to_integer = {
            'W': 1,
            'B': 5,
            'G': 2,
            'Y': 6,
            'O': 4,
            'R': 3,
            
        }
x = 1
d = ""
while x < 27:
    i = 0

    a = nums[x]
    c = list(a)
    b = []
    for i in range(len(c)):
        b.append(roman_to_integer[c[(i)]])
        print(sum(tuple(b)))
    x = x + 1
    