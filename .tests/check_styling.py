# check_styling.py

def check_for_long_lines(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    for line in lines:
        if len(line) > 80:
            return False
    return True

# Check for styling
if check_for_long_lines("main.lua"):
    print("Passed")
else:
    print("Failed")

