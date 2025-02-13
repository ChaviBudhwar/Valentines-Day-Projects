import time

def typewriter_effect(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print("\n")

heart = """
      *****     *****  
    **     ** **     **  
   **       ***       **  
   **                 **  
    **               **  
      **           **  
        **       **  
          **   **  
            **  
"""

print(heart)

typewriter_effect("Happy Valentine's Day, [His Name]! 💖")
typewriter_effect("You make my heart smile every day! 😊")
typewriter_effect("Wishing you all the love and happiness in the world! ❤️")
