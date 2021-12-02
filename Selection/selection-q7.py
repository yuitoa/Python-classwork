temperature = input("Do you have a temperature? [Y/N]")
if temperature.upper() == 'Y': #then
    sore_throat = input("Do you have a sore throat?")
    if sore_throat == 'Y': #then
        print('You might have throat infection')
    else:
        cough = input('Do you have a cough?')
        if cough == 'Y': #then
            print('You have a chest infection')
        else:
            print('You have a temperture')
        #end if
    #end if 
else:
    print('You are fine!')
#end if



