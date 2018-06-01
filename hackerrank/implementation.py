from typing import List

def grading(raw_grades: List[int]) -> List[int]:
    rounded_grades = list()
    for grade in raw_grades:
        if grade <= 37:
            rounded_grades.append(grade)
        else:
            if grade % 5 >= 3:
                rounded = grade + (5 - (grade % 5))
                rounded_grades.append(rounded)
            else:
                rounded_grades.append(grade)
    return rounded_grades

def kangaroo(x1: int, v1: int, x2: int, v2: int) -> str:
    if x1 == x2 and v1 == v2:
        return "YES"
    elif x1 != x2 and v1 == v2:
        return "NO"
    else:
        result = (x2 - x1) / (v1 - v2)
        if result % 1 == 0 and result > 0:
            return "YES"
        else:
            return "NO"

class TestImplementation(object):

    def test_grading(self):
        assert grading([73, 67, 38, 33]) == [75, 67, 40, 33]
        assert grading([37, 0, 100, 99, 98, 97]) == [37, 0, 100, 100, 100, 97]

    def test_kangaroo(self):
        assert kangaroo(0, 3, 4, 2) == "YES"
        assert kangaroo(0, 2, 5, 3) == "NO"
        