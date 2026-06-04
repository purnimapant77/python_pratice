# Personal Bio-Data Card Generator

print("Personal Bio-Data Card Generator")
name = input("Enter your full name: ")
city = input("Enter your city: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in feet: "))
student = input("Are you a student? (yes/no): ")
is_student = student.lower() == "yes"
day = int(input("Enter birth day: "))
month = int(input("Enter birth month: "))
year = int(input("Enter birth year: "))
dob = (day, month, year)

print("Enter 3 hobbies:")
hobby1 = input("Hobby 1: ")
hobby2 = input("Hobby 2: ")
hobby3 = input("Hobby 3: ")
hobbies = [hobby1, hobby2, hobby3]

print("Enter 3 languages:")
lang1 = input("Language 1: ")
lang2 = input("Language 2: ")
lang3 = input("Language 3: ")
languages = {lang1, lang2, lang3}

profile = {
    "name": name,
    "city": city,
    "age": age,
    "height": height,
    "is_student": is_student,
    "dob": dob,
    "hobbies": hobbies,
    "languages": languages
}

print("\n" + "=" * 40)
print("       PERSONAL BIO-DATA CARD")
print("=" * 40)

print(f"Name              : {profile['name']}")
print(f"City              : {profile['city']}")
print(f"Age               : {profile['age']}")
print(f"Height            : {profile['height']}")
print(f"Student           : {profile['is_student']}")
print(f"Date of Birth     : {profile['dob']}")
print(f"Hobbies           : {profile['hobbies']}")
print(f"Languages         : {profile['languages']}")

print("-" * 40)

print(f"First letter of name      : {name[0]}")
print(f"Number of hobbies         : {len(hobbies)}")
print(f"Number of unique languages: {len(languages)}")

print("-" * 40)

print(f"Type of name      : {type(name)}")
print(f"Type of age       : {type(age)}")
print(f"Type of height    : {type(height)}")
print(f"Type of student   : {type(is_student)}")
print(f"Type of dob       : {type(dob)}")
print(f"Type of hobbies   : {type(hobbies)}")
print(f"Type of languages : {type(languages)}")

print("=" * 40)