location = input("Are you at home?[Y/N]")
if location == "No" :
    sensor = input("Is there a movement?[Y/N]")
    if sensor == "Yes" :
        alarm = True
        if alarm :
            print("An intrusion was detected")
        #endif
    #endif
else:
    print("alarm is off")
