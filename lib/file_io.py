def write_file(file_name, file_content):
    with open(f"{file_name}.txt", mode="w", encoding="utf-8") as file_name:
        file_name.write(file_content)


def append_file(file_name, append_content):
    with open(f"{file_name}.txt", mode="a", encoding="utf-8") as file_name:
        file_name.write(append_content)


def read_file(file_name):
    with open(f"{file_name}.txt", encoding="utf-8") as file:
        contents = file.read()
    return contents

#Example , you must create dir journal.

# date = input("Enter today's date:")
# mood = input("How do you rate your mood from 1 to 10?")
# thoughts = input("Let your thoughts flow: \n")


# with open(f"../journal/{date}.txt", "w") as file:
    # file.write(mood + 2* "\n")
    # file.write(thoughts)
