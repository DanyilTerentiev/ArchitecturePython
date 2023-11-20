from abc import abstractmethod, ABC


class InternationalStudent:
    def __init__(self, first_name, last_name, age, grade):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.grade = grade


class InternationalRelationsDepartment:
    def enroll_in_university(self, university_name, student):
        if student.grade.lower() != "a":
            print("Sorry, but your score is not high enough to enroll on this course")
        else:
            print(f"Congratulations, {student.first_name} {student.last_name}! You are enrolled in a {university_name}")


class IDepartmentAdapter(ABC):
    @abstractmethod
    def enroll_in_university(self, university_name, ukrainian_student):
        pass


def international_student(first_name, last_name, age, grade):
    return {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "grade": grade
    }


class DepartmentAdapter(IDepartmentAdapter):
    def __init__(self, international_relations_department):
        self.grade_dictionary = {
            lambda grade: grade >= 90: "A",
            lambda grade: grade >= 80: "B",
            lambda grade: grade >= 70: "C",
            lambda grade: grade >= 60: "D",
            lambda grade: grade >= 50: "E",
            lambda grade: grade < 50: "F",
        }
        self.international_relations_department = international_relations_department

    def enroll_in_university(self, university_name, ukrainian_student):
        for grade_check, grade_value in self.grade_dictionary.items():
            if grade_check(ukrainian_student.grade):
                int_st = InternationalStudent(
                    ukrainian_student.first_name, ukrainian_student.last_name,
                    ukrainian_student.age, grade_value
                )
                self.international_relations_department.enroll_in_university(university_name, int_st)
                break


class UkrainianStudent:
    def __init__(self, first_name, last_name, grade, age):
        self.first_name = first_name
        self.last_name = last_name
        self.grade = grade
        self.age = age


if __name__ == "__main__":
    ukr_student = UkrainianStudent(first_name="Danyil", last_name="Terentiev", age=19, grade=100)
    international_dep = InternationalRelationsDepartment()
    adapter = DepartmentAdapter(international_dep)
    adapter.enroll_in_university("Berlin Universität", ukr_student)
