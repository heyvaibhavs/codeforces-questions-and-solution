IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.
      Returns IDENTICAL if the two lines are the same.
    """
    if len(line1) == len(line2):
        for num in range(len(line1)):
            if line1[num] != line2[num]:
                return num
        
        return IDENTICAL
    elif len(line1) < len(line2):
        min_len = len(line1)
    else:
        min_len = len(line2)

    num = 0
    while num < min_len:
        if line1[num] != line2[num]:
            return num
        else:
            num += 1
    return num
print(singleline_diff('', ''))         #-1
print(singleline_diff('abc', 'abcd')) #3
print(singleline_diff('a', 'b'))      #0    

    

def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.
      If either input line contains a newline or carriage return,
      then returns an empty string.
      If idx is not a valid index, then returns an empty string.
    """
    if line1.find("\n") >= 0 or line2.find("\n") >=0 or line2.find("\r") >=0 or \
       line1.find("\r") >= 0:
        return ""
    if (len(line1) <= len(line2) and len(line1) != 0):
        line_len = len(line1)
    elif (len(line1) > len(line2) and len(line2) != 0):
        line_len = len(line2)
    else:
        line_len = 1
    if (idx < 0 or idx > line_len):
        return ''
    elif (idx > 0):
        return(line1 + '\n' + '=' * idx + '^' + '\n' + line2 + '\n')
    else:
        return (line1 + '\n' + '^' + '\n' + line2 + '\n')


def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.
      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    if len(lines1) <= len(lines2):
        min_len = len(lines1)
    else:
        min_len = len(lines2)

    for index in range(min_len):
        line1 = lines1[index]
        line2 = lines2[index]
        diff = singleline_diff(line1, line2)
        if diff >= 0:
            return (index, diff)
    if len(lines1) != len(lines2):
        return (min_len, 0)
    
    return (IDENTICAL, IDENTICAL)


def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.
      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
   
    fileopen = open(filename, "rt")
    read_text = fileopen.readlines()
    data = []
    for line in read_text:
        line = line.rstrip()
        if len(line) == 0:
            continue
        data.append(line)
    fileopen.close()
    return data


def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.
      If the files are identical, the function instead returns the
      string "No differences\n".
      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    lines1 = get_file_lines(filename1)
    lines2 = get_file_lines(filename2)
    diff = multiline_diff(lines1, lines2)
    if diff[0] != -1 and diff[1] != -1:
        if lines2 == []:
            lines2 = ['']
        if lines1 == []:
            lines1 = ['']
        return "Line " + str(diff[0]) + ':\n' + \
               singleline_diff_format(lines1[diff[0]], lines2[diff[0]], diff[1])
    return "No differences\n"