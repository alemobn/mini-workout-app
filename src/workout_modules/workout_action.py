from ..utils import (
    global_messages,
    list_workouts,
    clear_screen
)


class WorkoutAction:
    def __init__(self, storage):
        self.storage = storage

    def _list_and_select_workout(self, prompt_msg):
        while True:
            print(
                list_workouts(
                    global_messages['listed_workouts'],
                    self.storage.workouts
                )
            )
            for i, workout in enumerate(self.storage.workouts):
                print(f'{i})', workout['name'])
            print(f"\n{global_messages['back']}")
            user_input = input(prompt_msg).strip().lower()
            clear_screen()
            if user_input in ['b', 'back']:
                print(global_messages['welcome'])
                return None
            if user_input.isdigit():
                index = int(user_input)
                if 0 <= index < len(self.storage.workouts):
                    return self.storage.workouts[index]
            print(global_messages['invalid_workout'])
