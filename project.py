from argparse import ArgumentParser
from csv import DictReader
from os import path

GRADES = {
    "A+": 4.0,
    "A": 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B": 3.0,
    "B-": 2.7,
    "C+": 2.3,
    "C": 2.0,
    "C-": 1.7,
    "D+": 1.3,
    "D": 1.0,
    "F": 0.0,
}

class Course:
    def __init__(self, course_code, ch, grade):
        self.code = course_code
        self.ch = int(ch)
        self.grade = grade
    
    def __str__(self) -> str:
        return f"({self.code};{self.ch};{self.grade})"

    # Geter for grade
    @property
    def grade(self):
        return self._grade

    # Setter for grade
    @grade.setter
    def grade(self, grade):
        if grade not in GRADES:
            raise ValueError("Invalid grade")
        self._grade = grade


def main():
    parser = ArgumentParser(description="Calculates semester and cumulative GPA")
    parser.add_argument("files", nargs='+', type=open, help="CSV file that contain user's grades")
    parser.add_argument("-l", "--lowest", type=int, default=2, help="Number of courses to improve")
    args = parser.parse_args()
    semesters = set()
    all_courses = {}
    for file in args.files:
        reader = DictReader(file)
        courses = set()
        for course in reader:
            courses.add(Course(**course))
            all_courses[course["course_code"]] = course["grade"]
        semester = calculate_semester(courses)
        semesters.add(semester)
        print(f"{path.splitext(file.name)[0]}: {semester[0]:.2f}")
    cumulative = calculate_cumulative(semesters)
    print(f"Total GPA: {cumulative[0]:.2f}")
    print(f"Total CHs: {cumulative[1]}")
    print("Lowest courses:", lowest_courses(all_courses, args.lowest))  


def calculate_semester(courses: set):
    """
    takes a set of Course objects as its argument
    returns tuple: (GPA, total_CHs)
    """
    points = 0.0
    total_chs = 0
    for course in courses:
        points += GRADES[course.grade] * course.ch
        total_chs += course.ch
    gpa = float(points) / float(total_chs)
    return (gpa, total_chs)


def calculate_cumulative(semesters: set):
    """
    takes a set of tuples (GPA, CH) as its argument
    returns cumulative gpa & total CHs as tuple: (GPA, CH)
    """
    points = 0.0
    total_chs = 0
    for semester in semesters:
        points += semester[0] * semester[1]
        total_chs += semester[1]
    gpa = points / total_chs
    return (gpa, total_chs)


def lowest_courses(courses: dict, n: int):
    """
    takes as input a dict object of key, value pairs where:
        the keys are courses' codes
        the values are the grades
    returns least n courses as a list of tuples; each tuples is (course_code, grade)
    if multiple courses have the same low grade: return the least name ASCII values
    """
    sorted_courses = sorted(courses.items(), key=lambda kv: GRADES[kv[1]])
    return sorted_courses[:n]


if __name__ == "__main__":
    main()
