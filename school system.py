# SCHOOL MANAGEMENT SYSTEM
# Demonstrates all OOP and SOLID Principles

from abc import ABC, abstractmethod


# PERSON CLASS - Abstract Base Class
# Demonstrates: Abstraction, Encapsulation

class Person(ABC):
    """Abstract base class for all people in school"""
    
    # Class attribute
    total_people = 0
    
    def __init__(self, person_id, name, age, phone):
        # Protected attributes (Encapsulation)
        self._person_id = person_id
        self._name = name
        self._age = age
        self._phone = phone
        Person.total_people += 1
    
    # Getter methods
    def get_id(self):
        return self._person_id
    
    def get_name(self):
        return self._name
    
    def get_age(self):
        return self._age
    
    def get_phone(self):
        return self._phone
    
    # Setter methods
    def set_name(self, name):
        self._name = name
    
    def set_phone(self, phone):
        self._phone = phone
    
    # Abstract methods (must be implemented by child classes)
    @abstractmethod
    def display_info(self):
        """Display person information"""
        pass
    
    @abstractmethod
    def get_role(self):
        """Return role of person"""
        pass
    
    # Class method
    @classmethod
    def get_total_people(cls):
        """Get total number of people created"""
        return cls.total_people
    
    # Static method
    @staticmethod
    def validate_phone(phone):
        """Check if phone number is valid"""
        return len(phone) >= 10


# STUDENT CLASS
# Demonstrates: Inheritance, Polymorphism

class Student(Person):
    """Student class that inherits from Person"""
    
    # Class attribute
    total_students = 0
    
    def __init__(self, person_id, name, age, phone, grade, student_class):
        # Call parent constructor
        super().__init__(person_id, name, age, phone)
        self._grade = grade
        self._student_class = student_class
        self._grades = {}
        Student.total_students += 1
    
    # Getter methods
    def get_grade_level(self):
        return self._grade
    
    def get_class(self):
        return self._student_class
    
    def get_grades(self):
        return self._grades.copy()
    
    # Instance methods
    def add_grade(self, subject, grade):
        """Add or update grade for a subject"""
        if 0 <= grade <= 100:
            self._grades[subject] = grade
            return True
        return False
    
    def calculate_average(self):
        """Calculate average grade"""
        if not self._grades:
            return 0
        return sum(self._grades.values()) / len(self._grades)
    
    # Override parent methods (Polymorphism)
    def display_info(self):
        """Override display_info to show student-specific info"""
        info = f"ID: {self._person_id}\n"
        info += f"Name: {self._name}\n"
        info += f"Age: {self._age}\n"
        info += f"Phone: {self._phone}\n"
        info += f"Grade: {self._grade}\n"
        info += f"Class: {self._student_class}\n"
        info += f"Average: {self.calculate_average():.2f}"
        return info
    
    def get_role(self):
        """Override get_role method"""
        return "Student"
    
    # Class method
    @classmethod
    def get_total_students(cls):
        """Get total number of students"""
        return cls.total_students
    
    # Static method
    @staticmethod
    def is_passing_grade(grade):
        """Check if a grade is passing"""
        return grade >= 50



# TEACHER CLASS
# Demonstrates: Inheritance, Polymorphism

class Teacher(Person):
    """Teacher class that inherits from Person"""
    
    # Class attribute
    total_teachers = 0
    
    def __init__(self, person_id, name, age, phone, subject, salary):
        # Call parent constructor
        super().__init__(person_id, name, age, phone)
        self._subject = subject
        self._salary = salary
        self._classes = []
        Teacher.total_teachers += 1
    
    # Getter methods
    def get_subject(self):
        return self._subject
    
    def get_salary(self):
        return self._salary
    
    def get_classes(self):
        return self._classes.copy()
    
    # Setter method
    def set_salary(self, new_salary):
        """Update teacher salary"""
        if new_salary > 0:
            self._salary = new_salary
            return True
        return False
    
    # Instance methods
    def add_class(self, class_name):
        """Assign a class to this teacher"""
        if class_name not in self._classes:
            self._classes.append(class_name)
            return True
        return False
    
    # Override parent methods (Polymorphism)
    def display_info(self):
        """Override display_info to show teacher-specific info"""
        info = f"ID: {self._person_id}\n"
        info += f"Name: {self._name}\n"
        info += f"Age: {self._age}\n"
        info += f"Phone: {self._phone}\n"
        info += f"Subject: {self._subject}\n"
        info += f"Salary: ${self._salary}\n"
        info += f"Classes: {', '.join(self._classes) if self._classes else 'None'}"
        return info
    
    def get_role(self):
        """Override get_role method"""
        return "Teacher"
    
    # Class method
    @classmethod
    def get_total_teachers(cls):
        """Get total number of teachers"""
        return cls.total_teachers
    
    # Static method
    @staticmethod
    def calculate_tax(salary):
        """Calculate tax on salary"""
        if salary < 5000:
            return salary * 0.1
        return salary * 0.15



# STUDENT MANAGER CLASS
# Demonstrates: Single Responsibility Principle (SRP)

class StudentManager:
    """Manages all student operations - Single Responsibility"""
    
    def __init__(self):
        self._students = {}
    
    def add_student(self, student):
        """Add a new student to the system"""
        student_id = student.get_id()
        if student_id not in self._students:
            self._students[student_id] = student
            return True
        return False
    
    def get_student(self, student_id):
        """Get a student by ID"""
        return self._students.get(student_id)
    
    def get_all_students(self):
        """Get all students"""
        return list(self._students.values())
    
    def count(self):
        """Count total number of students"""
        return len(self._students)


# TEACHER MANAGER CLASS
# Demonstrates: Single Responsibility Principle (SRP)

class TeacherManager:
    """Manages all teacher operations - Single Responsibility"""
    
    def __init__(self):
        self._teachers = {}
    
    def add_teacher(self, teacher):
        """Add a new teacher to the system"""
        teacher_id = teacher.get_id()
        if teacher_id not in self._teachers:
            self._teachers[teacher_id] = teacher
            return True
        return False
    
    def get_teacher(self, teacher_id):
        """Get a teacher by ID"""
        return self._teachers.get(teacher_id)
    
    def get_all_teachers(self):
        """Get all teachers"""
        return list(self._teachers.values())
    
    def count(self):
        """Count total number of teachers"""
        return len(self._teachers)


# GRADE CALCULATOR CLASS
# Demonstrates: Open/Closed Principle (OCP)

class GradeCalculator:
    """Base calculator - Open for extension, closed for modification"""
    
    def calculate_letter_grade(self, numeric_grade):
        """Convert numeric grade to letter grade"""
        if numeric_grade >= 90:
            return "A"
        elif numeric_grade >= 80:
            return "B"
        elif numeric_grade >= 70:
            return "C"
        elif numeric_grade >= 60:
            return "D"
        else:
            return "F"
    
    def calculate_gpa(self, grades_dict):
        """Calculate GPA from grades dictionary"""
        if not grades_dict:
            return 0.0
        
        total = 0
        for grade in grades_dict.values():
            if grade >= 90:
                total += 4.0
            elif grade >= 80:
                total += 3.0
            elif grade >= 70:
                total += 2.0
            elif grade >= 60:
                total += 1.0
        
        return total / len(grades_dict)


# ADVANCED GRADE CALCULATOR CLASS
# Demonstrates: Open/Closed Principle (OCP) - Extension

class AdvancedGradeCalculator(GradeCalculator):
    """Extended calculator - adds features without modifying base class"""
    
    def get_grade_status(self, average):
        """Get status based on average grade"""
        if average >= 85:
            return "Excellent"
        elif average >= 70:
            return "Good"
        elif average >= 60:
            return "Pass"
        else:
            return "Fail"


# NOTIFIABLE INTERFACE
# Demonstrates: Interface Segregation Principle (ISP)

class Notifiable(ABC):
    """Small, focused interface for notifications"""
    
    @abstractmethod
    def send_notification(self, message):
        """Send notification"""
        pass


# EMAIL NOTIFICATION CLASS
# Demonstrates: Liskov Substitution Principle (LSP)

class EmailNotification(Notifiable):
    """Email notification implementation"""
    
    def send_notification(self, message):
        """Send notification via email"""
        print(f"[EMAIL] {message}")
        return True


# SMS NOTIFICATION CLASS
# Demonstrates: Liskov Substitution Principle (LSP)

class SMSNotification(Notifiable):
    """SMS notification implementation - can substitute EmailNotification"""
    
    def send_notification(self, message):
        """Send notification via SMS"""
        print(f"[SMS] {message}")
        return True


# REPORT GENERATOR CLASS
# Demonstrates: Dependency Inversion Principle (DIP)

class ReportGenerator:
    """Generates reports - depends on Notifiable interface, not concrete class"""
    
    def __init__(self, notifier: Notifiable):
        """Inject notification dependency"""
        self._notifier = notifier
    
    def generate_student_report(self, student):
        """Generate a student report"""
        report = "=" * 50 + "\n"
        report += "STUDENT REPORT\n"
        report += "=" * 50 + "\n"
        report += student.display_info()
        report += "\n" + "=" * 50
        return report
    
    def send_report(self, report):
        """Send report using injected notifier"""
        return self._notifier.send_notification(report)


# SCHOOL CLASS - Main System

class School:
    """Main school management system"""
    
    def __init__(self, school_name):
        self._school_name = school_name
        
        # Use manager classes (SRP)
        self._student_mgr = StudentManager()
        self._teacher_mgr = TeacherManager()
        
        # Use calculator (OCP)
        self._grade_calc = AdvancedGradeCalculator()
        
        # Use dependency injection (DIP)
        notifier = EmailNotification()
        self._report_gen = ReportGenerator(notifier)
    
    def get_school_name(self):
        return self._school_name
    
    # Student operations
    def add_student(self, student):
        return self._student_mgr.add_student(student)
    
    def get_student(self, student_id):
        return self._student_mgr.get_student(student_id)
    
    def get_all_students(self):
        return self._student_mgr.get_all_students()
    
    # Teacher operations
    def add_teacher(self, teacher):
        return self._teacher_mgr.add_teacher(teacher)
    
    def get_all_teachers(self):
        return self._teacher_mgr.get_all_teachers()
    
    # Grade operations
    def calculate_student_gpa(self, student_id):
        student = self._student_mgr.get_student(student_id)
        if student:
            return self._grade_calc.calculate_gpa(student.get_grades())
        return 0.0
    
    def get_letter_grade(self, student_id):
        student = self._student_mgr.get_student(student_id)
        if student:
            avg = student.calculate_average()
            return self._grade_calc.calculate_letter_grade(avg)
        return "N/A"
    
    # Report operations
    def generate_report(self, student_id):
        student = self._student_mgr.get_student(student_id)
        if student:
            return self._report_gen.generate_student_report(student)
        return "Student not found"
    
    # Statistics
    def get_statistics(self):
        stats = f"\nSchool: {self._school_name}\n"
        stats += f"Students: {self._student_mgr.count()}\n"
        stats += f"Teachers: {self._teacher_mgr.count()}\n"
        stats += "-" * 30
        return stats



# MAIN PROGRAM


def main():
    """Main demonstration program"""
    
    print("\n" + "="*50)
    print("SCHOOL MANAGEMENT SYSTEM")
    print("="*50 + "\n")
    
    # Create school
    school = School("Bright Future School")
    print(f"Welcome to {school.get_school_name()}\n")
    
    # Create students
    s1 = Student("S001", "Ahmed Hassan", 16, "0123456789", 10, "A")
    s2 = Student("S002", "Sara Mohamed", 15, "0123456790", 9, "B")
    s3 = Student("S003", "Omar Ali", 16, "0123456791", 10, "A")
    
    school.add_student(s1)
    school.add_student(s2)
    school.add_student(s3)
    
    # Add grades
    s1.add_grade("Math", 92)
    s1.add_grade("English", 88)
    s1.add_grade("Science", 95)
    
    s2.add_grade("Math", 85)
    s2.add_grade("English", 90)
    
    # Add teachers
    t1 = Teacher("T001", "Dr. Mahmoud", 45, "0111111111", "Math", 5000)
    t2 = Teacher("T002", "Ms. Nour", 35, "0122222222", "English", 4500)
    
    t1.add_class("10-A")
    t2.add_class("9-B")
    
    school.add_teacher(t1)
    school.add_teacher(t2)
    
    # Show statistics
    print(school.get_statistics() + "\n")
    
    # Demonstrate Polymorphism
    print("="*50)
    print("POLYMORPHISM DEMO")
    print("="*50)
    all_people = school.get_all_students() + school.get_all_teachers()
    for person in all_people:
        print(f"{person.get_name()} - {person.get_role()}")
    
    # Show student details
    print("\n" + "="*50)
    print("STUDENT DETAILS")
    print("="*50)
    print(s1.display_info())
    
    # Calculate grades
    print("\n" + "="*50)
    print("GRADE CALCULATIONS")
    print("="*50)
    for student in school.get_all_students():
        gpa = school.calculate_student_gpa(student.get_id())
        letter = school.get_letter_grade(student.get_id())
        print(f"{student.get_name()}: GPA={gpa:.2f}, Grade={letter}")
    
    # Class methods demo
    print("\n" + "="*50)
    print("CLASS METHODS DEMO")
    print("="*50)
    print(f"Total People: {Person.get_total_people()}")
    print(f"Total Students: {Student.get_total_students()}")
    print(f"Total Teachers: {Teacher.get_total_teachers()}")
    
    # Static methods demo
    print("\n" + "="*50)
    print("STATIC METHODS DEMO")
    print("="*50)
    print(f"Is grade 75 passing? {Student.is_passing_grade(75)}")
    print(f"Phone valid? {Person.validate_phone('0123456789')}")
    
    # Generate report
    print("\n" + school.generate_report("S001"))
    
    print("\n" + "="*50)
    print("DEMO COMPLETE")
    print("="*50 + "\n")


if __name__ == "__main__":
    main()