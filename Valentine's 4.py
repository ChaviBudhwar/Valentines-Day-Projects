import time

print("💖 Hey there! I have a little message for you. 💖")
input("Press Enter to see it... ")

message = "You're amazing, and I like you a lot! ❤️"
for char in message:
    print(char, end="", flush=True)#see later
    time.sleep(0.1)#see later

print("\n\nHope this made you smile! 😊")

#Explanation:
#By default, print() adds a new line (\n) after printing something. If you don't want a new line, you can use end="" to control what gets printed after the text.
# Normally, Python buffers output, meaning it waits before printing to the screen. flush=True forces Python to print immediately instead of waiting.
# time.sleep(0.1) pauses the program for 0.1 seconds after printing each character. It causes a short delay between each character, making the output appear one character at a time like a typewriter effect.
# "\n" is a newline character in Python, which means it moves the text to a new line. So, \n\n means two new lines, creating a blank line between text.