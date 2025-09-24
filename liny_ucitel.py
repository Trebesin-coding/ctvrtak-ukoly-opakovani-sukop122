import random
import json
import os


os.chdir(os.path.dirname(os.path.abspath(__file__)))

path = "grades.json"

students = {

}

def read():
    global students
    with open(path, mode="r") as f:
        students = json.load(f)

def save():
    with open(path, mode="w") as f:
        json.dump(students, f, indent=2)

def average(grades):
    if not grades:
        return 0
    return round(sum(grades) /len(grades), 2)


def main():
    global students
    read()

    while True:
        for value, key in students.items():
            print(f'{value} --> {key} ')
        print('')    

        name = input("Vaše jméno? (T = seznam, q = konec)\n")
        
        if name.lower() == "q":
            print("Konec programu.")
            break


        elif name.lower() == "t":
            for student, grades in students.items():
               avg = average(grades)
               print(f"{student}: průměr {avg}")
            print()
            continue

        elif name == "Petr":
            print("hura")
            z = input("Jakou bys si chtel znamku?")
            try:
                grade = int(z)
                if 1 <= grade <= 5:
                    students[name].append(grade)
                    save()
                    print("znamka pridana")
                else:
                    print("znamka musi byt 1 az 5")
            except ValueError:
                print("to neni znamka , jenom znamku")

        elif name not in students:
            x = input("Studenta v seznamu nevidím, mám přidat? ano/ne: ")
            if x.lower() == "ano":
                grade = random.randint(1, 5)
                students[name] = [grade]
                save()
                print(f"Přidán student {name} se známkou {grade}\n")
            else:
                print("Nepridám.\n")
        else:
            grade = random.randint(1, 5)
            students[name].append(grade)
            print(f"Tvůj průměr je {average(students[name])}\n")
            save()

main()