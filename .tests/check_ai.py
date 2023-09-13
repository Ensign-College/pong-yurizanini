# check_ai.py

def check_for_default_code(filename):
    with open(filename, 'r') as f:
        content = f.read()

    default_code_block = '''if love.keyboard.isDown('up') then
        player2.dy = -PADDLE_SPEED
    elseif love.keyboard.isDown('down') then
        player2.dy = PADDLE_SPEED
    else
        player2.dy = 0
    end'''

    return default_code_block not in content

# Check if AI was implemented
if check_for_default_code("main.lua"):
    print("Passed")
else:
    print("Failed")

