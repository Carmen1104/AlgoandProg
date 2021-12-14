class person:
    def __init__(self, name , address):
        self.__name = name
        self.__address = address

    def setRadius(self, address):
        self.__address = address

    def getName(self):
        return self.__name
    def getAddress(self):
        return self.__address

    def __str__(self) :
        return "{{}}".format(self.__name,self.__address)

class student(person):
    def __init__(self, name, address , numCourses, course, grade):
        super().__init__(name, address)
        self.__numCourses = numCourses
        self.__courses = [course]
        self.__grade = [grade]

    def addCourseGrade(self, course, grade):
        self.__courses.append(course)
        self.__grade.append(grade)
        print(self.__grade)

    def getAverageGrade(self):
        avgScore = sum(self.__grade)/len(self.__grade)
        return avgScore

    def __str__(self) :
        return "{{}}".format(self.__name,self.__address)

class teacher(person):
    def __init__(self, name, address, numCourses, course):
        super().__init__(name, address)
        self.__numCourses = numCourses
        self.__courses = [course]

    def addCourse(self, course):
        courseName = input("Enter the name of the course you want to add: ")
        if courseName not in self.__courses[course]:
            self.__courses.append(courseName)
        else:
            print("Please enter another course")
    
    def removeCourse(self, course):
        courseName = input("Enter the name of the course you want to add: ")
        if courseName in self.__courses[course]:
            self.__courses.remove(courseName)
        else:
            print("Course name doesn't exist")
    
    def __str__(self) :
        return "{{}}".format(self.__name,self.__address)
