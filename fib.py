def singleline_diff(line1, line2):
    if len(line1) != len(line2):
        if len(line1) > len(line2):
            return line1.find(line2[-1])+2
        else:
            return line2.find(line1[-1])+2
    else:
        if line1 == line2:
            return -1
        else:
            return line1.find(line2)
print(singleline_diff("abcde","abchy"))            