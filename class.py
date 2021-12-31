import webbrowser
#webbrowser imports the open() function, which allows the opening of webpages

import datetime
#datetime allows the program to read what time and day of the week it is


def openClass(date):
    
    ########
    #MONDAY#
    ########
    if date.weekday() == 0:
        ###########################w
        # MTH 714 LECTURE 11AM - 2PM
        #
        if (10 == date.timetuple()[3] and 45 < date.timetuple()[4]) or (11 == date.timetuple()[3] and 30 > date.timetuple()[4]):
            webbrowser.open('https://ryerson.zoom.us/j/99524332807?pwd=MjJyRUR3enVIM0VySXRwd3l1dFpaQT09')
            
        ##########################
        #CPS 305 LECTURE 2PM - 3PM
        #
        elif (13 == date.timetuple()[3] and 45 < date.timetuple()[4]) or (14 == date.timetuple()[3] and 30 > date.timetuple()[4]):
            webbrowser.open('https://courses.ryerson.ca/d2l/le/content/543807/viewContent/3901425/View')
            
        

    #########
    #TUESDAY#
    #########
    elif date.weekday() == 1:
        
        #######################w
        #MTH 108 LECTURE 8AM - 10AM
        #
        if (7 == date.timetuple()[3] and 45 < date.timetuple()[4]) or (8 == date.timetuple()[3] and 30 > date.timetuple()[4]):
            webbrowser.open('https://ryerson.zoom.us/j/98836755855?pwd=RlpkSkd2QVJVdlhtcWJESk9Zb0dlQT09')
            
        ############################
        #CPS 393 LECTURE 11AM - 1PM
        #
        elif (10 == date.timetuple()[3] and 45 < date.timetuple()[4]) or (11 == date.timetuple()[3] and 30 > date.timetuple()[4]):
            webbrowser.open('https://ryerson.zoom.us/j/98869774311?pwd=cG1qQ1NrdjRhUGtZQXBiNWZFOWpsUT09')
            
        

    ###########
    #WEDNESDAY#
    ###########
    elif date.weekday() == 2:
        
        ###########################w
        #MTH 714 TUTORIAL 10AM - 11AM
        #
        if date.timetuple()[3] >= 9 and date.timetuple()[3] <= 11:
            webbrowser.open('https://ryerson.zoom.us/j/98391128075?pwd=eHVGeFBQYlIzYTgwSzczdHJhTUlBdz09')

        ###########################w
        #CPS 305 LECTURE 12PM - 2PM
        #
        elif (11 == date.timetuple()[3] and 45 < date.timetuple()[4]) or (12 == date.timetuple()[3] and 30 > date.timetuple()[4]):
            webbrowser.open('https://ryerson.zoom.us/j/93275255781?pwd=M1o4dXdHOXBHNUVlQnUzSkd6djJqdz09#success')

        ###########################w
        #CPS 393 LAB 2PM - 3PM
        #
        elif (13 == date.timetuple()[3] and 45 < date.timetuple()[4]) or (14 == date.timetuple()[3] and 30 > date.timetuple()[4]):
            webbrowser.open('https://ryerson.zoom.us/j/98610752341?pwd=RVFqcVJ6N2RsdWZCcmY1YUd2TVZVZz09')



            
    ##########
    #THURSDAY#
    ##########
    elif date.weekday() == 3:

        ############################w
        #MTH 108 LAB 10AM - 11AM
        #
        if (9 == date.timetuple()[3] and 45 < date.timetuple()[4]) or (10 == date.timetuple()[3] and 30 > date.timetuple()[4]):
            webbrowser.open('https://ryerson.zoom.us/j/98283811244?pwd=VSsvbUFDRlNpQzFoL3VpMGY0U0tHZz09')

        ############################w
        #CPS 393 LECTURE 11AM - 12PM
        #
        elif (10 == date.timetuple()[3] and 45 < date.timetuple()[4]) or (11 == date.timetuple()[3] and 30 > date.timetuple()[4]):
            webbrowser.open('https://ryerson.zoom.us/j/98869774311?pwd=cG1qQ1NrdjRhUGtZQXBiNWZFOWpsUT09')

        ######################w
        #CPS 305 LAB 2PM - 3PM
        #
        elif (13 == date.timetuple()[3] and 45 < date.timetuple()[4]) or (14 == date.timetuple()[3] and 40 > date.timetuple()[4]):
            webbrowser.open('https://ryerson.zoom.us/j/92551508700?pwd=V3ArWEQ4eHlReTVMOUVncFY2M25WZz09')

            
    ########    
    #FRIDAY#
    ########
    elif date.weekday() == 4:

        ###########################w
        #MTH 108 LECTURE 8AM - 10AM
        #
        if (7 == date.timetuple()[3] and 45 < date.timetuple()[4]) or (8 == date.timetuple()[3] and 59 > date.timetuple()[4]):
            webbrowser.open('https://ryerson.zoom.us/j/99504411891?pwd=cUUxbzhvTW84bGlEaGh5cnpwMnNIdz09')

        ############################
        #CPS 310 LECTURE 10AM - 12PM
        #
        elif (9 == date.timetuple()[3] and 45 < date.timetuple()[4]) or (10 == date.timetuple()[3] and 30 > date.timetuple()[4]):
            webbrowser.open('https://ryerson.zoom.us/j/94195550253?pwd=S2F3ZlBmeEhBY3VITm5uakJPSUZEdz09')
            


date = datetime.datetime.today()
#assigns the date to the variable so it can be interacted with
#format is a tuple with order (year, month, day, hour, minute, second)
#Day --> Monday=0 , Friday=4 , Sunday=6

openClass(date)
#calls openClass() function to produce the useful output
