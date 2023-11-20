class UniversityAttendee:
    def visit(self):
        pass


class Lecturer(UniversityAttendee):
    def visit(self):
        print("I'm visiting the university by car")


class Student(UniversityAttendee):
    def visit(self):
        print("Ohh, I'm soo poor, can't afford any car")


class AttendeeFactory:
    def create_attendee(self):
        pass


class LecturerAttendeeFactory(AttendeeFactory):
    def create_attendee(self):
        return Lecturer()


class StudentAttendeeFactory(AttendeeFactory):
    def create_attendee(self):
        return Student()


class Client:
    def main(self):
        print("Lecturer creation")
        self.client_code(LecturerAttendeeFactory())

        print()

        print("Student creation")
        self.client_code(StudentAttendeeFactory())

    def client_code(self, attendee_factory):
        print("I'm not aware what is creating right now, but I definitely know that is a factory")
        attendee_factory.create_attendee().visit()


if __name__ == "__main__":
    Client().main()
