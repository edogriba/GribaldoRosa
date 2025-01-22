from app.models.user import User
from app.db.dbModels.student_db import StudentDB

class Student(User):
    def __init__(self, id, email, password, firstName, lastName, phoneNumber, profilePicture, location, universityId, degreeProgram, GPA, graduationYear, skills, CV, languageSpoken):
        super().__init__(id, email, password, "student")
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumber = phoneNumber
        self.profilePicture = profilePicture
        self.location = location
        self.universityId = universityId          
        self.degreeProgram = degreeProgram
        self.GPA = GPA
        self.graduationYear = graduationYear
        self.skills = skills
        self.CV = CV
        self.languageSpoken = languageSpoken

    #def __repr__(self):
    #    return f"<Student: ({self.id}) {self.firstName} {self.lastName}, Email: {self.email}"
    
    def get_id(self):
        return super().get_id()
    
    def get_email(self):
        return super().get_email()
    
    def get_password(self):
        return super().get_password()
    
    def get_type(self):
        return super().get_type()
    
    def get_firstName(self):
        return self.firstName
    
    def get_lastName(self):
        return self.lastName

    def get_phoneNumber(self):
        return self.phoneNumber
    
    def get_profilePicture(self):
        return self.profilePicture
    
    def get_location(self):
        return self.location
    
    def get_universityId(self):
        return self.universityId
    
    def get_degreeProgram(self):
        return self.degreeProgram
    
    def get_gpa(self):
        return self.GPA
    
    def get_graduationYear(self):
        return self.graduationYear
    
    def get_skills(self):
        return self.skills
    
    def get_cv(self):
        return self.CV
    
    def get_languageSpoken(self):
        return self.languageSpoken
    

    @staticmethod
    def add(email: str, password: str, firstName: str, lastName: str, phoneNumber: str, profilePicturePath: str, location: str, 
            degreeProgram: str, gpa: float, graduationYear: int, CVpath: str, skills: str, languageSpoken: str, universityId: int):
        try:
            # Insert student data into the database
            studentConn = StudentDB()
            studentId = studentConn.insert(email, password, firstName, lastName, phoneNumber, profilePicturePath, location, 
                degreeProgram, gpa, graduationYear, CVpath, skills, languageSpoken, universityId)

            return Student(studentId, email, password, firstName, lastName, phoneNumber, profilePicturePath, location,
                           degreeProgram, gpa, graduationYear, CVpath, skills, languageSpoken, universityId)
        
        except Exception as e:
            raise e
        
        finally:
            studentConn.close()
