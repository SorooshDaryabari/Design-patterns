class Course(object):
    def displayCourse(self, user, course_name):
        print(f"[{user}'s course ]: {course_name}")


class User(object):
    def __init__(self, name):
        self.name = name
        self.course = Course()

    def sendCourse(self, course_name):
        self.course.displayCourse(self, course_name)

    def __str__(self):
        return self.name


if __name__ == "__main__":
    mayank = User("Python")
    lakshya = User("Java")
    krishna = User("Go")

    mayank.sendCourse("Data Structures and Algorithms")
    lakshya.sendCourse("Software Development Engineer")
    krishna.sendCourse("Standard Template Library")
