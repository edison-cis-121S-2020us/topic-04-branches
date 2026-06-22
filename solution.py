# Topic 04 Collaborative Assignment
# Your Name: Troy Post
# Date: 6/22/26

# --- STARTER CODE ---
# This starter program checks if a temperature is hot, warm, or cold.
# Extend it, change the theme, or use it as inspiration for your own idea.

temp_input = input("Enter a temperature in Fahrenheit: ")
temperature = float(temp_input)

if temperature >= 90:
    print("It is hot outside.")
elif temperature >= 60:
    print("It is warm outside.")
else:
    print("It is cold outside.")

# --- YOUR EXTENSION BELOW THIS LINE ---
# Ideas: Add more conditions, change the topic entirely,
# or add a second input and a second set of branches.

if temperature >= 90:
    if weather == "sunny":
        print("Perfect day to go swimming at the pool!")
      elif weather == "rainy":
        print("It's a humid, stormy day. Better stay inside with the A/C.")
        else:
        print("Whew, stay hydrated out there whatever you do!")

elif temperature >= 60:
    if weather == "sunny":
        print("Great weather for a picnic or a bike ride in the park.")
    elif weather == "rainy":
        print("Don't forget your umbrella if you are heading out!")
      else:
        print("Sounds like nice, comfortable weather to touch some grass.")

else: # Temperature is cold (< 60)
    if weather == "snowy":
        print("Time to build a snowman or go sledding!")
    elif weather == "rainy":
        print("Brr! A cold, dreary rain. Grab a blanket and some hot cocoa.")
    else:
        print("Make sure to wear a heavy coat before you head out!")


