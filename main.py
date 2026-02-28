from operations import create_class, search_data, update_data, delete_data
from utils import OutOfLimitError


def main():
    while True:
        try:
            print("""
            -------------- MENU --------------
            1. Create New Class
            2. Search Data
            3. Update Data
            4. Delete Data
            5. Exit
            """)

            choice = int(input("Enter your choice: "))

            if choice < 1 or choice > 5:
                raise OutOfLimitError

            match choice:
                case 1:
                    create_class()
                case 2:
                    search_data()
                case 3:
                    update_data()
                case 4:
                    delete_data()
                case 5:
                    print("Exiting program...")
                    break

        except ValueError:
            print("Please provide valid integer input.")
        except OutOfLimitError:
            print("Please provide input within the given range.")


if __name__ == "__main__":
    main()