### PROVA

class LoginManager:
    def __init__(self, db_session):
        self.db_session = db_session

    def sign_in(self, email, password):
        # Validate user credentials
        user = self.db_session.query(User).filter_by(email=email).first()
        if user and user.check_password(password):
            # Generate session token
            token = generate_session_token(user.id)
            return {"token": token, "user": user}
        raise AuthenticationError("Invalid credentials.")

    def logout(self, token):
        # Invalidate the session token
        invalidate_session_token(token)
