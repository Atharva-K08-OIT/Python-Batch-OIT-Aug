# Functions || WPWR ||

# Ex.1
# def percentage():
#     marks = [89, 85, 91, 94, 95, 97]
#     print(f"Percentage: {round(sum(marks)/len(marks), 2)}")


# percentage()

# Ex.2


# def Percentage():
#     suresh = {
#         "Maths": 89,
#         "Science": 85,
#         "English": 91,
#         "History": 94,
#         "Geography": 95,
#         "Marathi": 97
#     }
#     total = 0
#     for subject in suresh:
#         print(subject + " : " + str(suresh[subject]))
#         total += suresh[subject]

#     print(f"Suresh Have total {total} marks")
#     print(f"Suresh Have {round(total/len(suresh), 2)} %")


# Percentage()

# Ex.3 : NPNR --> WPWR

def Percentage(student,name):

    total = 0
    for subject in student:
        print(subject + " : " + str(student[subject]))
        total += student[subject]

    print(f"{name} Have total {total} marks")
    return round(total/len(student), 2)


# -----------------------------------------------------------
name = input("Enter Student Name: ")
student = {
    "Maths": int(input("Enter marks of Maths: ")),
    "Science": int(input("Enter marks of Science: ")),
    "English": int(input("Enter marks of English: ")),
    "History": int(input("Enter marks of History: ")),
    "Geography": int(input("Enter marks of Geography: ")),
    "Marathi": int(input("Enter marks of Marathi: "))
}
result = Percentage(student,name)
print(f"{name} Have {result} %")

