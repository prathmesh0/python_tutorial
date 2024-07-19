import pyttsx3
import os

# engin = pyttsx3.init()
# engin.say("hello World. kaisa hai tu")

# engin.runAndWait

# print('''
#       Twinkle twinkle little star.
# How I wonder what you are.
# Up above the world so high.
# Like a diamond in the sky.
# Twinkle twinkle little star.
# How I wonder what you are.

# Twinkle twinkle little star.
# How I wonder what you are.
# Up above the world so high.
# Like a diamond in the sky.
# Twinkle twinkle little star.
# How I wonder what you are.
# '''
# )

#specify the diractory path
directory_path =  '/MISSION POP'
#list all files and directory in the path
content  = os.listdir(directory_path)

#print the files and directory
for item in content:
    print(item)


