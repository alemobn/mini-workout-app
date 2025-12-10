from .workout_action import WorkoutAction
from ..utils import (
    global_messages,
    clear_screen,
    check_empty_list
)

class DeleteWorkout(WorkoutAction):
    DELETE_WORKOUT_MESSAGES = {
        'ask_delete': 'Which workout do you wish to delete? ',
        'ask_sure_delete': (
            'Are you sure? This action is irreversible! '
            '[y]es / [n]o '),
        'successfully_deleted': 'Workout successfully deleted!'
    }

    def delete_workout(self):
        clear_screen()
        if check_empty_list(self.storage.workouts):
            return   
        workout_to_delete = self._list_and_select_workout(
            self.DELETE_WORKOUT_MESSAGES['ask_delete']
        )
        if not workout_to_delete:
            return
        workout_to_delete_name = workout_to_delete["name"]
        user_response = False
        while not user_response:
            sure_or_not = input(
                self.DELETE_WORKOUT_MESSAGES['ask_sure_delete']
            ).strip().lower()
            if sure_or_not in ['y', 'yes']:
                self.storage.delete_workout(workout_to_delete_name)
                user_response = True
                clear_screen()
                print(
                    self.DELETE_WORKOUT_MESSAGES['successfully_deleted']
                )
            elif sure_or_not in ['n', 'no']:
                user_response = True
                clear_screen()
            else:
                clear_screen()
                print(global_messages['invalid_input'])
