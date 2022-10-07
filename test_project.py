from project import Course, calculate_semester, calculate_cumulative, lowest_courses

def test_calculate_semester():
    assert [round(num, 2) for num in calculate_semester({
        Course("CSE0a31s", 2, "B-"),
        Course("PHM021s", 3, "C"),
        Course("PHM041s", 3, "C+"),
        Course("PHM031s", 3, "B-"),
        Course("MDP011s", 3, "C+"),
        Course("PHM012s", 3, "B-")
    })] == [2.44, 17]


def test_calculate_cumulative():
    assert [round(num, 2) for num in  calculate_cumulative({(2.44, 17), (3.18, 17)})] == [2.81, 34]


def test_lowest_courses():
    assert set(lowest_courses({"PHM022s": "A-", "PHM013s": "B", "CEP011s": "B+", "MDP081s": "C"}, 2)) == set([("PHM013s", "B"), ("MDP081s", "C")])
