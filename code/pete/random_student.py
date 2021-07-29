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

while True:
	if input(choice(students)):
		break
	# truthy_or_falsey_string = input(choice(students))
	# if truthy_or_falsey_string:
	# 	break

# run program...
# $ demetric # hit enter
# $ mark # hit enter
# $ megan # hit space (or anything) then hit enter
# $ # (program exits)