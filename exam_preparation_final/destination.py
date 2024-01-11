import re


def travel():

    string = input()
    pattern = r'/(\={1}[A-Z][a-z]{3,}\={1})(\/{1}[A-Z][a-z]{3,}\/{1})/'
    result = re.finditer(pattern, string)

    for res in result:
        city = res.group()

        print(city)


travel()
