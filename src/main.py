from .menu import Menu
from .storage import Storage

def main():
    storage = Storage()
    storage.load_workouts()
    Menu(storage)


if __name__ == '__main__':
    main()
