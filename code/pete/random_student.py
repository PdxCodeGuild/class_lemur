from random import choice
import argparse

parser = argparse.ArgumentParser(description='random students')
parser.add_argument('groups', type=int, default=0, nargs='?', help='Number of groups', metavar='G')
args = parser.parse_args()

students = [
    'megan',
    'demetric',
    'swartwood',
    'david',
    'mark',
    'matt',
    'scott'
]

def random_students():
    while len(students) > 0:
        student = choice(students)
        students.remove(student)
        if input(student):
            break

def random_groups(n):
    print(f'split into {n} groups')

if args.groups != 0:
    random_groups(args.groups)
else:
    random_students()

# truthy_or_falsey_string = input(choice(students))
# if truthy_or_falsey_string:
# 	break

# run program...
# $ demetric # hit enter
# $ mark # hit enter
# $ megan # hit space (or anything) then hit enter
# $ # (program exits)
