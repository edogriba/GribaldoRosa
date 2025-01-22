from backend.app.models.user import User


class Company(User):
    def __init__(self, id, email, password, companyName, logo, description, location):
        super().__init__(id, email, password, "company")
        self.companyName = companyName
        self.logo = logo
        self.description = description
        self.location = location
    
    def __repr__(self):
        return f"<Company: ({self.id}) {self.companyName}, Email: {self.email}"