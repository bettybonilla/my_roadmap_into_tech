"""
The below shows how we can use the zip() function in different ways to
pair/group the test scores of students
"""

midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ["Dan", "Ang", "Kate"]

print(list(zip(students, midterms, finals)))

# However, the teacher wants to drop the lowest test score for each student and
# base the final grades on their highest test score
# Therefore, a dictionary comprehension is used with the zip() function and
# the max() function to get the larger value between the midterms and finals
# and pair them to each corresponding student
final_grades = {
    item[0]: max(item[1], item[2]) for item in zip(students, midterms, finals)
}
print(final_grades)

# Alternative code using the map() function
# The map() function uses a lambda with the max() function to get the larger
# value between the midterms and finals then the zip() function is used to
# pair them to each corresponding student which is wrapped in the dict()
# function to return a dictionary
final_grades = dict(
    zip(
        students,
        map(
            lambda item: max(item),
            zip(midterms, finals),
        ),
    )
)
print(final_grades)
