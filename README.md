    # College GPA Calculator & grades analyzer
    #### Video Demo:  https://youtu.be/lCTHAwjRXmk
    #### Description:
    This is a simple program that calculates your GPA in each semester, your cumulative GPA, total credit hours taken. Also tells you your lowest n courses in case you want to retake them to improve your GPA.
    Usage: project.py [-h] [-l LOWEST] files [files ...]
    files should be csv files and they must have course_code,ch,grade in the header
    You can enter any number of semester files you like (at least 1)
    You can specify the number of courses you want to improve (defaults to 2 if unspecified)

    ##### If you dont know how to calculate GPA:
    In calculating college GPA, course credit hours are thrown into the mix. Most college courses are 3 credit hours, but some are worth more depending on the difficulty of the class or extra work like science and computer labs.

    Just like high school, the letter grade is first converted to grade points (usually according to the 4.0 scale). After that, the grade points are multiplied by the number of credit hours that the class is worth.

    Say you took an English 101 course worth 3 credit hours and made an "A". To find the total number of points, multiply the credit hours (3) by the grade points (4.0).

    3 credit hours x 4.0 grade points = 12 total points

    Sample output:
    semester1: 2.44
    semester2: 3.18
    Total GPA: 2.81
    Total CHs: 34
    Lowest courses: [('PHM021s', 'C'), ('MDP081s', 'C')]
