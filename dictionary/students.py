information = {}
student = input()
while ':' in student:
    info = student.split(":")
    name = info[0]
    id = int(info[1])
    course = info[2]
    if course not in information:
        information[course] = {}
    information[course][id] = name
    student = input()

course = " ".join(student.split('_'))
for key, value in information.items():
    if key == course:
        for id, name in value.items():
            print(f"{name} - {id}")
