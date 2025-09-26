from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

from .database import Base


# This models.py file outlines the structure and schema of the database tables below which are created for our
# database.py file and are going to be stored in our database URL
# Singular name for the class
class ToDo(Base):
    # Title of the table
    # Plural name for the database table
    __tablename__ = "to_dos"

    # Columns of the table
    # id will be an int and will distinguish each database record uniquely therefore the primary_key parameter is set to
    # True since we will use it as our primary key
    # The index parameter is also set to True to increase performance by telling our table that it is indexable
    id = Column(Integer, primary_key=True, index=True)
    # title will be a str
    title = Column(String)
    # description will be a str
    description = Column(String)
    # priority will be an int
    priority = Column(Integer)
    # complete will be a bool and the default parameter is set to False in order to indicate the to-do is not complete
    complete = Column(Boolean, default=False)
    # owner_id will be an int and is the foreign key which holds the primary key from the users table below which links
    # both tables and to create a one-to-many relationship so that a user can have many to-dos
    owner_id = Column(Integer, ForeignKey("users.id"))


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    # role will be a str to specify whether a user is an admin
    role = Column(String)
    phone_number = Column(String)
