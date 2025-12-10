from utils import clear_screen, global_messages
from workout_manager import (
    CreateWorkout,
    EditWorkout,
    DeleteWorkout,
    ListWorkout
)


class Menu:
    MENU = """
1. Create workout
2. Edit workout
3. Delete workout
4. List workouts
5. Exit\n
"""

    def __init__(self, storage):
        self.storage = storage
        self.actions = self._setup_actions()
        self.loop_menu()

    def _setup_actions(self):
        return {
            '1': CreateWorkout(self.storage).build_workout,
            'create': CreateWorkout(self.storage).build_workout,
            'create workout': CreateWorkout(self.storage).build_workout,
            '2': EditWorkout(self.storage).edit_workout,
            'edit': EditWorkout(self.storage).edit_workout,
            'edit workout': EditWorkout(self.storage).edit_workout,
            '3': DeleteWorkout(self.storage).delete_workout,
            'delete': DeleteWorkout(self.storage).delete_workout,
            'delete workout': DeleteWorkout(self.storage).delete_workout,
            '4': ListWorkout(self.storage).list_workouts,
            'list': ListWorkout(self.storage).list_workouts,
            'list workout': ListWorkout(self.storage).list_workouts,
        }

    def loop_menu(self):
        clear_screen()
        print(global_messages['welcome'])
        while True:
            user_option = input(Menu.MENU).lower().strip()
            print()
            if user_option in ['5', 'exit']:
                clear_screen()
                exit()
            action = self.actions.get(user_option)
            if action:
                action()
                continue
            clear_screen()
            print(global_messages['welcome'])
