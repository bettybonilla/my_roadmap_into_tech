from sqlalchemy import create_engine

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Creates a database URL which is the location of the database where we want to store our to_do_app.db on our FastAPI
# application (backend server)
# Using SQLite as our Database Management System (DBMS)
DATABASE_URL = "sqlite:///./to_do_app.db"

# Using Postgres as our Database Management System (DBMS)
# DATABASE_URL = "postgresql://postgres:test1234!@localhost/ToDoAppDatabase"

# Using MySQL as our Database Management System (DBMS)
# DATABASE_URL = "mysql+pymysql://root:test1234!@127.0.0.1:3306/ToDoAppDatabase"

# Creates a database engine for our FastAPI application (backend server)
# Used to open up a connection so that we can use our database
# The connect_args parameter allows us to pass in arguments to define a connection to the database
# By default, SQLite will only allow one thread to communicate to it - Each thread should only handle one kind of
# request to prevent accidentally sharing the same connection to the database for different requests
# However, in FastAPI it's very normal to have more than one thread that can interact with the database at the same time
# Therefore, the {"check_same_thread": False} argument is used to let SQLite know that we don't want to be checking the
# same thread all the time since there could be multiple threads interacting with our database - It is only needed for
# SQLite (Postgres and MySQL don't need it)
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# engine = create_engine(DATABASE_URL)

# The sessionmaker class is known as a factory class since it creates new Session objects when called
# A factory creates and returns objects - Common in JavaScript where it's used as an alternative to using classes or
# constructors to create objects
# - sessionmaker is the cookie cutter: You configure the sessionmaker once with parameters like the bind parameter set
# to your database engine to use
# - Session objects are the cookies: When you call the sessionmaker, it produces a Session object tailored to the
# configuration you defined
# Each object of the sessionmaker class will have a database session which will become an actual database
# The bind parameter is set to our engine and binds it to the database session
# The autocommit and autoflush parameters are set to False in order to prevent the database from doing something
# automatically since we want to be in control of what our database is doing
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# In SQLAlchemy, declarative_base() is a function that creates a Base object for declarative class definitions which are
# used in SQLAlchemy's Object Relational Mapping (ORM)
# The declarative_base() function is known as a factory function since it creates a new Base object from which you'll
# inherit when defining your SQLAlchemy models (Python classes that represent database tables)
# This Base object created by declarative_base() internally includes a MetaData object and a mapper
# - The MetaData object holds information about your database schema, such as table definitions
# - The mapper links your Python class attributes (Ex: id, name, email, etc.) to the corresponding columns in your table
# This simplifies declarative mapping since the declarative approach allows you to define your database schema and the
# mapping to your Python classes within a single class declaration
Base = declarative_base()
