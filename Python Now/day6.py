# #conditional statement

# age  = int(input("Enter Your age : "))
# if(age >= 18):
#     print("You are above age of consent")
#     print("Good for you")
# elif(age< 0 ):
#     print("You are entered invalid negative age(negative)")
# elif(age == 0 ):
#     print("You are entered invalid age(0)")
# else:
#     print("You are below age of consent")
    
# print("End of program")

# #chapter 6 Practice set

# a1 = int(input("Enter number 1 : "))
# a2 = int(input("Enter number 2 : "))
# a3 = int(input("Enter number 3 : "))
# a4 = int(input("Enter number 4 : "))

# if(a1 > a2 and a1>a3 and a1>a4):
#     print("Greatest Number is a1 : ", a1)
# elif(a2 > a1 and a2>a3 and a2>a4):
#     print("Greatest Number is a2 : ", a2)
# elif(a3 > a1 and a3>a2 and a3>a4):
#     print("Greatest Number is a3 : ", a3)
# elif(a4 > a1 and a4>a2 and a4>a3):
#     print("Greatest Number is a4 : ", a4)
    
# marks1 = int(input("Enter marks 1 : "))
# marks2 = int(input("Enter marks 2 : "))
# marks3 = int(input("Enter marks 3 : "))

# #check  for total percentage
# total_percentage =(100*(marks1+marks2+marks3)) /300

# if(total_percentage >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33):
#     print("You are pass : ", total_percentage)
# else:
#     print("You are failed, try again next year!", total_percentage)


# p1 = "Make a lot of money"
# p2 = "Buy now"
# p3 = "subscribe this"
# p4 = "click this"

# message = input("Enter your comment : ")

# if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
#     print("Spam comment")
# else:
#     print("Comment is not spam")
    
# username = input("Enter your username : ")

# if(len(username) < 10):
#     print("Username contains less than 10 character")
# else:
#     print("All good!")
    
# l =  ["Harry", "Rohan", "Shubham", "Divya"]
# name = input("Enter your name:")

# if(name in l):
#     print("Your name is in the list")
# else:
#     print("Your name is not in the list")

post = input("Enter your post:")

if("Harry".lower() in post.lower()):
    print("This post is talking about Harry")
else:
    print("This post is not talking about Harry")
    