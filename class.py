import webbrowser
#webbrowser imports the open() function, which allows the opening of webpages

import datetime
#datetime allows the program to read what time and day of the week it is


class Course:
    def __init__(self,
                lecture1_day, lecture1_time, lecture1_link,
                lecture2_day, lecture2_time, lecture2_link,
                lab_day, lab_time, lab_link):
        self.lecture1_day = lecture1_day
        self.lecture1_time = lecture1_time
        self.lecture1_link = lecture1_link
        self.lecture2_day = lecture2_day
        self.lecture2_time = lecture2_time
        self.lecture2_link = lecture2_link
        self.lab_day = lab_day
        self.lab_time = lab_time
        self.lab_link = lab_link

def openClass(date,courses):

    for course in courses:
        if course.lecture1_day == date.weekday():
            if (course.lecture1_time == date.timetuple()[3] and date.timetuple()[4] < 45) \
               or (course.lecture1_time == (date.timetuple()[3] - 1) and date.timetuple()[4] > 45):
                webbrowser.open(course.lecture1_link)
        elif course.lecture2_day == date.weekday():
            if (course.lecture2_time == date.timetuple()[3] and date.timetuple()[4] < 45) \
               or (course.lecture2_time == (date.timetuple()[3] - 1) and date.timetuple()[4] > 45):
                webbrowser.open(course.lecture2_link)
        elif course.lab_day == date.weekday():
            if (course.lab_time == date.timetuple()[3] and date.timetuple()[4] < 45) \
               or (course.lab_time == (date.timetuple()[3] - 1) and date.timetuple()[4] > 45):
                webbrowser.open(course.lab_link)
        

    
courses = []

#################
#USER INPUT BEGIN
#################

#######
#MTH108
#
lecture1_day = 0    #0 = Monday, 1 = Tuesday, 2 = Wednesday, 3 = Thursday, 4 = Friday
lecture1_time = 13  #Round to nearest hour; use 24 hour clock
lecture1_link = 'https://ryerson.zoom.us/j/94195550253?pwd=S2F3ZlBmeEhBY3VITm5uakJPSUZEdz09' #link to zoom meeting

lecture2_day = 0    #0 = Monday, 1 = Tuesday, 2 = Wednesday, 3 = Thursday, 4 = Friday
lecture2_time = 13  #Round to nearest hour; use 24 hour clock
lecture2_link = 'https://ryerson.zoom.us/j/94195550253?pwd=S2F3ZlBmeEhBY3VITm5uakJPSUZEdz09' #link to zoom meeting

lab_day = 0         #0 = Monday, 1 = Tuesday, 2 = Wednesday, 3 = Thursday, 4 = Friday
lab_time = 13       #Round to nearest hour; use 24 hour clock
lab_link = 'https://ryerson.zoom.us/j/94195550253?pwd=S2F3ZlBmeEhBY3VITm5uakJPSUZEdz09' #link to zoom meeting

course1 = Course(lecture1_day, lecture1_time, lecture1_link,
                lecture2_day, lecture2_time, lecture2_link,
                lab_day, lab_time, lab_link)
courses.append(course1)

#######
#MTH714
#
lecture1_day = 0    #0 = Monday, 1 = Tuesday, 2 = Wednesday, 3 = Thursday, 4 = Friday
lecture1_time = 13  #Round to nearest hour; use 24 hour clock
lecture1_link = 'https://ryerson.zoom.us/j/94195550253?pwd=S2F3ZlBmeEhBY3VITm5uakJPSUZEdz09' #link to zoom meeting

lecture2_day = 0    #0 = Monday, 1 = Tuesday, 2 = Wednesday, 3 = Thursday, 4 = Friday
lecture2_time = 13  #Round to nearest hour; use 24 hour clock
lecture2_link = 'https://ryerson.zoom.us/j/94195550253?pwd=S2F3ZlBmeEhBY3VITm5uakJPSUZEdz09' #link to zoom meeting

lab_day = 0         #0 = Monday, 1 = Tuesday, 2 = Wednesday, 3 = Thursday, 4 = Friday
lab_time = 13       #Round to nearest hour; use 24 hour clock
lab_link = 'https://ryerson.zoom.us/j/94195550253?pwd=S2F3ZlBmeEhBY3VITm5uakJPSUZEdz09' #link to zoom meeting

course2 = Course(lecture1_day, lecture1_time, lecture1_link,
                lecture2_day, lecture2_time, lecture2_link,
                lab_day, lab_time, lab_link)
courses.append(course2)

#######
#CPS305
#
lecture1_day = 0    #0 = Monday, 1 = Tuesday, 2 = Wednesday, 3 = Thursday, 4 = Friday
lecture1_time = 13  #Round to nearest hour; use 24 hour clock
lecture1_link = 'https://ryerson.zoom.us/j/94195550253?pwd=S2F3ZlBmeEhBY3VITm5uakJPSUZEdz09' #link to zoom meeting

lecture2_day = 0    #0 = Monday, 1 = Tuesday, 2 = Wednesday, 3 = Thursday, 4 = Friday
lecture2_time = 13  #Round to nearest hour; use 24 hour clock
lecture2_link = 'https://ryerson.zoom.us/j/94195550253?pwd=S2F3ZlBmeEhBY3VITm5uakJPSUZEdz09' #link to zoom meeting

lab_day = 0         #0 = Monday, 1 = Tuesday, 2 = Wednesday, 3 = Thursday, 4 = Friday
lab_time = 13       #Round to nearest hour; use 24 hour clock
lab_link = 'https://ryerson.zoom.us/j/94195550253?pwd=S2F3ZlBmeEhBY3VITm5uakJPSUZEdz09' #link to zoom meeting

course3 = Course(lecture1_day, lecture1_time, lecture1_link,
                lecture2_day, lecture2_time, lecture2_link,
                lab_day, lab_time, lab_link)
courses.append(course3)

#######
#CPS393
#
lecture1_day = 4    #0 = Monday, 1 = Tuesday, 2 = Wednesday, 3 = Thursday, 4 = Friday
lecture1_time = 13  #Round to nearest hour; use 24 hour clock
lecture1_link = 'https://ryerson.zoom.us/j/94195550253?pwd=S2F3ZlBmeEhBY3VITm5uakJPSUZEdz09' #link to zoom meeting

lecture2_day = 0    #0 = Monday, 1 = Tuesday, 2 = Wednesday, 3 = Thursday, 4 = Friday
lecture2_time = 13  #Round to nearest hour; use 24 hour clock
lecture2_link = 'https://ryerson.zoom.us/j/94195550253?pwd=S2F3ZlBmeEhBY3VITm5uakJPSUZEdz09' #link to zoom meeting

lab_day = 0         #0 = Monday, 1 = Tuesday, 2 = Wednesday, 3 = Thursday, 4 = Friday
lab_time = 13       #Round to nearest hour; use 24 hour clock
lab_link = 'https://ryerson.zoom.us/j/94195550253?pwd=S2F3ZlBmeEhBY3VITm5uakJPSUZEdz09' #link to zoom meeting

course4 = Course(lecture1_day, lecture1_time, lecture1_link,
                lecture2_day, lecture2_time, lecture2_link,
                lab_day, lab_time, lab_link)
courses.append(course4)

#######
#CMN300
#
lecture1_day = 0    #0 = Monday, 1 = Tuesday, 2 = Wednesday, 3 = Thursday, 4 = Friday
lecture1_time = 13  #Round to nearest hour; use 24 hour clock
lecture1_link = 'https://ryerson.zoom.us/j/94195550253?pwd=S2F3ZlBmeEhBY3VITm5uakJPSUZEdz09' #link to zoom meeting

lecture2_day = 0    #0 = Monday, 1 = Tuesday, 2 = Wednesday, 3 = Thursday, 4 = Friday
lecture2_time = 13  #Round to nearest hour; use 24 hour clock
lecture2_link = 'https://ryerson.zoom.us/j/94195550253?pwd=S2F3ZlBmeEhBY3VITm5uakJPSUZEdz09' #link to zoom meeting

lab_day = 0         #0 = Monday, 1 = Tuesday, 2 = Wednesday, 3 = Thursday, 4 = Friday
lab_time = 13       #Round to nearest hour; use 24 hour clock
lab_link = 'https://ryerson.zoom.us/j/94195550253?pwd=S2F3ZlBmeEhBY3VITm5uakJPSUZEdz09' #link to zoom meeting

course5 = Course(lecture1_day, lecture1_time, lecture1_link,
                lecture2_day, lecture2_time, lecture2_link,
                lab_day, lab_time, lab_link)
courses.append(course5)

###############
#USER INPUT END
###############


date = datetime.datetime.today() #format is a tuple with order: (year, month, day, hour, minute, second)
openClass(date, courses)
