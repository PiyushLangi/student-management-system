from utils import load_data, save_data, OutOfLimitError


def create_class():
    """Create a new class and store student data."""
    print("Class Name Example : 1st std, 2nd std, etc.")

    data = load_data()

    class_name = input("Enter the class name: ")
    student_count = int(input("Enter number of students: "))

    data[class_name] = {}

    for i in range(1, student_count + 1):
        roll_no = int(input("Enter Student Roll No: "))
        name = input("Enter Student Full Name: ")
        age = int(input("Enter Age: "))
        marks = float(input("Enter Marks: "))

        status = "Pass" if marks >= 35 else "Fail"

        student_data = {
            "roll_no": roll_no,
            "name": name,
            "age": age,
            "marks": marks,
            "status": status,
        }

        data[class_name][f"student{i}"] = student_data

    save_data(data)
    print("Class data saved successfully.")


def search_data():
    """Search student records."""
    try:
        data = load_data()
        if not data:
            print("No saved data found.")
            return

        print("""Search student By:
                1. Using Class Name
                2. Using Roll No
                3. Using Student Name
                4. Using Result (Pass/Fail)""")

        choice = int(input("Enter your choice: "))

        if choice < 1 or choice > 4:
            raise OutOfLimitError

        match choice:
            case 1:
                name = input("Enter class name: ")
                if name in data:
                    for key, value in data[name].items():
                        print(f"{key}: {value}")
                else:
                    print("Class not found.")

            case 2:
                roll_no = int(input("Enter roll no: "))
                found = False

                for class_name in data:
                    for student in data[class_name].values():
                        if student["roll_no"] == roll_no:
                            print(f"Class: {class_name}")
                            print(student)
                            found = True
                            break

                if not found:
                    print("No student found.")

            case 3:
                student_name = input("Enter student name: ").strip()
                class_name = input("Enter class name: ")

                if class_name in data:
                    found = False
                    for student in data[class_name].values():
                        if student["name"] == student_name:
                            print(student)
                            found = True
                    if not found:
                        print("Student not found in this class.")
                else:
                    print("Class does not exist.")

            case 4:
                result_state = input("Enter Result State: ").capitalize()
                found = False

                for cls in data:
                    for student in data[cls].values():
                        if student["status"] == result_state:
                            print(f"Class: {cls}", student)
                            found = True

                if not found:
                    print("No data found.")

    except ValueError:
        print("Please provide valid integer input.")
    except OutOfLimitError:
        print("Please provide input in the given range.")


def update_data():
    """Update student information."""
    try:
        data = load_data()
        if not data:
            print("No data found.")
            return

        print("""Update student By:
                1. Student Name and Class Name
                2. RollNo and Class Name""")

        choice = int(input("Enter your choice: "))

        if choice < 1 or choice > 2:
            raise OutOfLimitError

        if choice == 1:
            name = input("Enter student name: ")
            cls_name = input("Enter class name: ")

            if cls_name in data:
                for student in data[cls_name].values():
                    if student["name"] == name:
                        student["marks"] = float(input("Enter new marks: "))
                        student["status"] = (
                            "Pass" if student["marks"] >= 35 else "Fail"
                        )
                        save_data(data)
                        print("Updated successfully.")
                        return

            print("Student not found.")

        elif choice == 2:
            roll_no = int(input("Enter roll no: "))
            cls_name = input("Enter class name: ")

            if cls_name in data:
                for student in data[cls_name].values():
                    if student["roll_no"] == roll_no:
                        student["marks"] = float(input("Enter new marks: "))
                        student["status"] = (
                            "Pass" if student["marks"] >= 35 else "Fail"
                        )
                        save_data(data)
                        print("Updated successfully.")
                        return

            print("Student not found.")

    except ValueError:
        print("Please provide valid integer input.")
    except OutOfLimitError:
        print("Please provide input in the given range.")


def delete_data():
    """Delete class or student."""
    try:
        data = load_data()
        if not data:
            print("No data found.")
            return

        print("""Delete Options:
                1. Delete Entire Class
                2. Delete Student By Roll No""")

        choice = int(input("Enter your choice: "))

        if choice < 1 or choice > 2:
            raise OutOfLimitError

        match choice:
            case 1:
                cls_name = input("Enter class name to delete: ")
                if cls_name in data:
                    del data[cls_name]
                    save_data(data)
                    print("Class deleted successfully.")
                else:
                    print("Class not found.")

            case 2:
                roll_no = int(input("Enter roll no: "))
                class_name = input("Enter class name: ")

                if class_name in data:
                    for key, student in list(data[class_name].items()):
                        if student["roll_no"] == roll_no:
                            del data[class_name][key]
                            save_data(data)
                            print("Student deleted successfully.")
                            return
                    print("Student not found.")
                else:
                    print("Class not found.")

    except ValueError:
        print("Please provide valid integer input.")
    except OutOfLimitError:
        print("Please provide input in the given range.")