from sqlmodel import SQLModel, Field, Session, select
from src.config.db_config import engine
from src.utils.security import hash_password

class User(SQLModel, table=True):
    __tablename__ = "user"

    id: int = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    email: str = Field(index=True, unique=True)
    password: str
    created_at: str
    updated_at: str

    def __repr__(self):
        return f"User(id={self.id}, username={self.username}, email={self.email})"
    

# Create a function to create a user table
def create_user_table():
    user = User
    with Session(engine) as session:
         data = session.exec(select(user)).all()
         print(len(data))
         if len(data) == 0:
            SQLModel.metadata.create_all(engine)
            # Create an instance of the User model    
            user_1 = User(
                id=1,
                username="john_doe",
                email="test@test.com",
                password=hash_password("password123"), 
                created_at="2023-10-01T00:00:00Z",
                updated_at="2023-10-01T00:00:00Z"
                )
            session.add(user_1)
            session.commit()
            session.refresh(user_1)
         else:
            print("Table already exists or has data.")


