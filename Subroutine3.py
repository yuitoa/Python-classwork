def getPword(attempt):
    global Done
    Done = False
    while not Done:
        if attempt == 1:
            password1 = input("enter the password:")
            password2 = input("re-enter the password:")
        #endif

        while password1 != password2:
            print("error, password do not match")
            password1 = input("enter the password:")
            password2 = input("re-enter the password:")
        
        while password1==password2 and not Done:
            if len(password2) < 6 and len(password2) <= 8:
               print("you have successfully changed the password:")
               Done = True
        Done = True
            #endif
        #end while
    #end while

Done = False
getPword(1)
                    