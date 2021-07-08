from sqlalchemy import Column, Integer, String, Boolean
from app.configs.database import db
from werkzeug.security import generate_password_hash, check_password_hash
from dataclasses import dataclass

@dataclass
class EmployeesModel(db.Model):
    id: int
    name: str
    login: str
    cpf: str
    is_admin: bool
    api_key: str

    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)

    name = Column(String(150), nullable=False)
    login = Column(String(150), nullable=False)
    password_hash = Column(String(511), nullable=False)
    cpf = Column(String(11), nullable=False)
    is_admin = Column(Boolean, default=False)
    api_key = Column(String(511), nullable=False)

    @property
    def password(self):
        raise AttributeError("Password cannot be accessed!!")

    @password.setter
    def password(self, password_to_hash) -> None:
        self.password_hash = generate_password_hash(password_to_hash)


    def check_password(self, password_to_compare) -> bool:
        return check_password_hash(self.password_hash, password_to_compare)
