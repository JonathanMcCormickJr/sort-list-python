names = ['Emma', 'Olivia', 'Ava', 'Isabella', 'Sophia', 'Mia', 'Charlotte', 'Amelia', 'Harper', 'Evelyn', 'Abigail', 'Emily', 'Elizabeth', 'Avery', 'Sofia', 'Ella', 'Madison', 'Scarlett', 'Victoria', 'Aria', 'Grace', 'Chloe', 'Camila', 'Penelope', 'Riley', 'Nora', 'Lily', 'Eleanor', 'Hazel', 'Aubrey', 'Ruby', 'Adalynn', 'Adalyn', 'Adalene', 'Adaline', 'Adalina', 'Adalisse', 'Adaliz', 'Adalene', 'Adalicia', 'Adalisse', 'Adalita', 'Adalicia', 'Adaliz', 'Adalena', 'Adaleta', 'Adalicia', 'Adalisse', 'Jordan', 'Taylor', 'Ethan', 'Mason', 'Liam', 'Noah', 'Aiden', 'Lucas', 'Elijah', 'Oliver', 'Jaxon', 'Jayden', 'Logan', 'Alexander', 'Caleb', 'Eli', 'Leah', 'Avery', 'Aurora', 'Avery', 'Jordan', 'Avery', 'Jorden', 'Riley', 'Jordanne', "Emma", "Olivia", "Ava", "Isabella", "Sophia", "Mia", "Charlotte", "Amelia", "Harper", "Evelyn",     "Abigail", "Emily", "Elizabeth", "Avery", "Sofia", "Ella", "Madison", "Scarlett", "Victoria", "Aria",     "Grace", "Chloe", "Camila", "Penelope", "Riley", "Luna", "Natalie", "Audrey", "Brooklyn", "Hazel",     "Nora", "Aaliyah", "Violet", "Stella", "Lily", "Eva", "Arianna", "Adalynn", "Makayla", "Aubrey",     "Kaylee", "Annabelle", "Hannah", "Khloé", "Bella", "Mila", "Aurora", "Genesis", "Willow", "Everly",     "Caleb", "Landon", "Ethan", "Mason", "Noah", "Lincoln", "Elijah", "Oliver", "Aiden", "James",     "Logan", "Benjamin", "Lucas", "Jacob", "Michael", "Daniel", "Henry", "Jackson", "Sebastian", "Matthew",     "Samuel", "David", "Joseph", "Carter", "Owen", "Wyatt", "John", "Jack", "Luke", "Jayden",     "Anthony", "Isaac", "Grayson", "Jaxon", "Julian", "Léo", "Eli", "Levi", "Miles", "Gael",     "Muhammad", "Juan", "Carlos", "José", "Miguel", "Diego", "Jorge", "Ricardo", "Hector", "Luis",     "Gustavo", "Jaime", "Manuel", "Enrique", "Roberto", "Javier", "Carlos", "Angel", "José", "Mauricio",     "Andrés", "Francisco", "Alex", "Juan", "David", "Ivan", "Oscar", "Gustavo", "Rafael", "José", "Samael", "Lilith", "Lucifer", "Lex", "Ayn", "Edward", "Thomas", "Jefferson", "Vít", "Amara","Juan","Fatima","Ivan","Aaliyah","Miguel","Isabella","Ahmed","Sophia","Lee","Yasmin","Ethan","Ava","Kim","Maya","David","Zoe","Jack","Mia","Ali"]


def sort_list(list):
    list.sort()
    return list

def remove_duplicates(original_list):
    updated_list = []
    for item in original_list:
        if item not in updated_list:
            updated_list.append(item)
    return updated_list

def simplify_list(list):
    new_list = remove_duplicates(sort_list(list))
    
    return new_list

print(simplify_list(names))