import pandas as pd
from sqlalchemy import create_engine, text #this creates our db engine
from dotenv import load_dotenv # lets you read from our .env file
import psycopg2

engine = create_engine(
    "postgresql+psycopg2://postgres@localhost:5432/postgres"
)

#we can execute raw sql queries using the execute method on our engine
query = "SELECT student_id, first_name, last_name FROM student;"
student_df = pd.read_sql(query, engine)
print(student_df)

#create a new student in our db
new_student = pd.DataFrame(
    {"first_name": ["Jayden"],
     "last_name": ["Miller"],
     "email": ["JMIll@email.com"],
     "major": ["MB"]
     }
)

#the to_sql method allows us to write a dataframe to a sql table
new_student.to_sql(name="student", con=engine, if_exists="append", index=False)


update_student = text("UPDATE student SET phone = '1564877' WHERE student_id = 5;")
#update statements need to be executed using a connection
with engine.connect() as connection:
    connection.execute(update_student)
    connection.commit()

#delete records
delete_sql = text("DELETE FROM student WHERE email = 'JMIll@email.com';")
with engine.connect() as connection:
    connection.execute(delete_sql)
    connection.commit()

#Call our stored procedure

#print(pd.read_sql('selectAllStudents()', engine))
# student_major = 'CS'
# result = f"CALL selectmajorstudents('{student_major}');"
# result_df = pd.read_sql(result, engine)
# print(result_df)

with engine.begin() as connection:
    connection.execute(text("CALL updatemajorstudents(:major, :student_id)"), {"major": "CS", "student_id": 2})
    connection.commit

student_id = 2
course_count_sql = f"SELECT first_name, last_name, get_course_count({student_id}) AS course_count FROM student;"
course_count_df = pd.read_sql(course_count_sql, engine)
print(course_count_df)

#We want to make sure we are closing our connection/engine when we are done
connection.close()