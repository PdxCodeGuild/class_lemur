from random import choice

students = [
    'megan',
    'demetric',
    'swartwood',
    'david',
    'mark',
    'matt',
    'scott'
]

while len(students) > 0:
    student = choice(students)
    students.remove(student)
    if input(student):
        break

# truthy_or_falsey_string = input(choice(students))
# if truthy_or_falsey_string:
# 	break

# run program...
# $ demetric # hit enter
# $ mark # hit enter
# $ megan # hit space (or anything) then hit enter
# $ # (program exits)
