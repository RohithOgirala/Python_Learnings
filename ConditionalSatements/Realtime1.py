strcmp=""
started=False
while strcmp!="quit":
 strcmp=input("Enter the comand(start,stop,quit) ").lower()
 if strcmp=="start":                               # lower() is used to convert uppercase to lower case if user gives uppercase letter
    if started==True:
        print("Game is already Started")
    else:
        started=True
        print("Game is Started")
 elif strcmp =="stop":
    if started==False:
        print("game is not started")
    else:
        started == False
        print("game is stopped")
 elif strcmp=="quit":
    print("your game is quitted")
    break
 elif strcmp!="start" or strcmp!="stop" or strcmp!="quit":
  print("your name is not in list")

#OutPut
#  Enter the comand(start,stop,quit) start
#  Game is Started
#  Enter the comand(start,stop,quit) start
#  Game is already Started
#  Enter the comand(start,stop,quit) stop
#  game is stopped
#  Enter the comand(start,stop,quit) stop
#  game is stopped
#  Enter the comand(start,stop,quit) quit
#  your game is quitted