def print_A():
    pattern = []
    for i in range(5):
        line = ""
        for j in range(5):
            if ((j == 0 or j == 4) and i != 0) or ((i == 0 or i == 2) and j > 0 and j < 4):
                line += "*"
            else:
                line += " "
        pattern.append(line)
    return pattern

def print_B():
    pattern = []
    for i in range(5):
        line = ""
        for j in range(5):
            if j == 0 or (j == 4 and (i != 0 and i != 2 and i != 4)) or ((i == 0 or i == 2 or i == 4) and j < 4):
                line += "*"
            else:
                line += " "
        pattern.append(line)
    return pattern

def print_C():
    pattern = []
    for i in range(5):
        line = ""
        for j in range(5):
            if i == 0 or i == 4 or j == 0:
                line += "*"
            else:
                line += " "
        pattern.append(line)
    return pattern

def print_D():
    pattern = []
    for i in range(5):
        line = ""
        for j in range(5):
            if j == 0 or (j == 4 and i != 0 and i != 4) or ((i == 0 or i == 4) and j < 4):
                line += "*"
            else:
                line += " "
        pattern.append(line)
    return pattern

def print_E():
    pattern = []
    for i in range(5):
        line = ""
        for j in range(5):
            if i == 0 or i == 2 or i == 4 or j == 0:
                line += "*"
            else:
                line += " "
        pattern.append(line)
    return pattern

def print_F():
    pattern = []
    for i in range(5):
        line = ""
        for j in range(5):
            if i == 0 or i == 2 or j == 0:
                line += "*"
            else:
                line += " "
        pattern.append(line)
    return pattern

def print_G():
    pattern = []
    for i in range(5):
        line = ""
        for j in range(5):
            if (i == 0 or i == 4) and j > 0 or j == 0 or (i == 2 and j >= 2) or (j == 4 and i >= 2 and i < 4):
                line += "*"
            else:
                line += " "
        pattern.append(line)
    return pattern

def print_H():
    pattern = []
    for i in range(5):
        line = ""
        for j in range(5):
            if j == 0 or j == 4 or i == 2:
                line += "*"
            else:
                line += " "
        pattern.append(line)
    return pattern

def print_I():
    pattern = []
    for i in range(5):
        line = ""
        for j in range(5):
            if i == 0 or i == 4 or j == 2:
                line += "*"
            else:
                line += " "
        pattern.append(line)
    return pattern

def print_J():
    pattern = []
    for i in range(5):
        line = ""
        for j in range(5):
            if i == 0 or (j == 2 and i != 4) or (i == 4 and j == 1):
                line += "*"
            else:
                line += " "
        pattern.append(line)
    return pattern

def print_K():
    pattern = []
    for i in range(5):
        line = ""
        for j in range(5):
            if j == 0 or (i + j == 4 and i < 3) or (i - j == 1 and i > 2):
                line += "*"
            else:
                line += " "
        pattern.append(line)
    return pattern

def print_L():
    pattern = []
    for i in range(5):
        line = ""
        for j in range(5):
            if j == 0 or i == 4:
                line += "*"
            else:
                line += " "
        pattern.append(line)
    return pattern

def print_M():
    pattern = []
    for i in range(5):
        line = ""
        for j in range(5):
            if j == 0 or j == 4 or (i == j and i <= 2) or (i + j == 4 and i <= 2):
                line += "*"
            else:
                line += " "
        pattern.append(line)
    return pattern

def print_N():
    pattern = []
    for i in range(5):
        line = ""
        for j in range(5):
            if j == 0 or j == 4 or i == j:
                line += "*"
            else:
                line += " "
        pattern.append(line)
    return pattern

def print_O():
    pattern = []
    for i in range(5):
        line = ""
        for j in range(5):
            if ((j == 0 or j == 4) and i > 0 and i < 4) or ((i == 0 or i == 4) and j > 0 and j < 4):
                line += "*"
            else:
                line += " "
        pattern.append(line)
    return pattern

def print_P():
    pattern = []
    for i in range(5):
        line = ""
        for j in range(5):
            if j == 0 or (i == 0 or i == 2) and j < 4 or (i == 1 and j == 4):
                line += "*"
            else:
                line += " "
        pattern.append(line)
    return pattern

def print_Q():
    pattern = []
    for i in range(5):
        line = ""
        for j in range(5):
            if ((j == 0 or j == 4) and i > 0 and i < 4) or ((i == 0 or i == 4) and j > 0 and j < 4) or (i == 3 and j == 3) or (i == 4 and j == 4):
                line += "*"
            else:
                line += " "
        pattern.append(line)
    return pattern

def print_R():
    pattern = []
    for i in range(5):
        line = ""
        for j in range(5):
            if j == 0 or (i == 0 or i == 2) and j < 4 or (i == 1 and j == 4) or (i == 3 and j == 2) or (i == 4 and j == 3):
                line += "*"
            else:
                line += " "
        pattern.append(line)
    return pattern

def print_S():
    pattern = []
    for i in range(5):
        line = ""
        for j in range(5):
            if i == 0 or i == 2 or i == 4 or (i == 1 and j == 0) or (i == 3 and j == 4):
                line += "*"
            else:
                line += " "
        pattern.append(line)
    return pattern

def print_T():
    pattern = []
    for i in range(5):
        line = ""
        for j in range(5):
            if i == 0 or j == 2:
                line += "*"
            else:
                line += " "
        pattern.append(line)
    return pattern

def print_U():
    pattern = []
    for i in range(5):
        line = ""
        for j in range(5):
            if (j == 0 or j == 4) and i != 4 or (i == 4 and j > 0 and j < 4):
                line += "*"
            else:
                line += " "
        pattern.append(line)
    return pattern

def print_V():
    pattern = []
    for i in range(5):
        line = ""
        for j in range(5):
            if (j == 0 and i < 4) or (j == 4 and i < 4) or (i == 4 and j == 2):
                line += "*"
            else:
                line += " "
        pattern.append(line)
    return pattern

def print_W():
    pattern = []
    for i in range(5):
        line = ""
        for j in range(5):
            if j == 0 or j == 4 or (i == j and i > 1) or (i + j == 4 and i > 1):
                line += "*"
            else:
                line += " "
        pattern.append(line)
    return pattern

def print_X():
    pattern = []
    for i in range(5):
        line = ""
        for j in range(5):
            if i == j or i + j == 4:
                line += "*"
            else:
                line += " "
        pattern.append(line)
    return pattern

def print_Y():
    pattern = []
    for i in range(5):
        line = ""
        for j in range(5):
            if (i == j and i < 3) or (i + j == 4 and i < 3) or (j == 2 and i >= 3):
                line += "*"
            else:
                line += " "
        pattern.append(line)
    return pattern

def print_Z():
    pattern = []
    for i in range(5):
        line = ""
        for j in range(5):
            if i == 0 or i == 4 or i + j == 4:
                line += "*"
            else:
                line += " "
        pattern.append(line)
    return pattern

letter_functions = {
    'A': print_A,
    'B': print_B,
    'C': print_C,
    'D': print_D,
    'E': print_E,
    'F': print_F,
    'G': print_G,
    'H': print_H,
    'I': print_I,
    'J': print_J,
    'K': print_K,
    'L': print_L,
    'M': print_M,
    'N': print_N,
    'O': print_O,
    'P': print_P,
    'Q': print_Q,
    'R': print_R,
    'S': print_S,
    'T': print_T,
    'U': print_U,
    'V': print_V,
    'W': print_W,
    'X': print_X,
    'Y': print_Y,
    'Z': print_Z,
   
}

name = input("Enter your name: ").upper()
output_lines = [""] * 5

for letter in name:
    if letter in letter_functions:
        pattern = letter_functions[letter]()
    else:
        pattern = ["     "] * 5  
    for i in range(5):
        output_lines[i] += pattern[i] + "  "


for line in output_lines:
    print(line)
