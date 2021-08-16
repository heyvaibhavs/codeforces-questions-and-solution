IDENTICAL = -1
def single_line_diff(line1, line2):
    if len(line1) == len(line2):
        for i in range(len(line1)):
            if line1[i] != line2[i]:
                return i
        return IDENTICAL
    if len(line1)<len(line2):
        max_line = line2
        min_line = line1
    else:
        min_line = line2
        max_line = line1
    i=0
    for i in range(len(min_line)):
        if min_line[i] != max_line[i]:
            return i
    return len(min_line)
print(single_line_diff('', ''))         #-1
print(single_line_diff('abc', 'abcd')) #3
print(single_line_diff('abd', 'abcdf'))      #0