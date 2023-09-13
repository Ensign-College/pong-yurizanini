# check_run.py

import subprocess

def check_if_runs(filename):
    result = subprocess.run(["luac", "-p", filename], capture_output=True)
    return result.returncode == 0

# Check if code runs
if check_if_runs("main.lua"):
    print("Passed")
else:
    print("Failed")

