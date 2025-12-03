from menu import Menu
from storage import Storage

storage = Storage()
storage.load_workouts()
Menu(storage)
