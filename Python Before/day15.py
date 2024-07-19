import time

timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)

current_time =  int(time.strftime('%H'))
if(current_time < 12):
    print("Good Morning")
elif(current_time >= 12):
    print("Good Afternoon")
elif(current_time >= 18):
    print("Good Evening")
elif(current_time >= 18 and current_time <= 21):
    print("Good Evening")
else:
    print("Good Night")


