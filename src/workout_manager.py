from utils import (
    clear_screen,
    global_messages,
    check_empty_list,
    list_workouts,
    is_nonempty_string,
    get_validated_input,
    validate_positive_int,
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


class CreateWorkout:
    DAYS = ['monday',
            'tuesday',
            'wednesday',
            'thursday',
            'friday',
            'saturday',
            'sunday'
            ]

    CREATE_WORKOUT_MESSAGES = {
        'ask_workout_name': 'What is the workout name? ',
        'invalid_workout_name': 'Please enter a valid name.',
        'ask_exercise_name': 'Enter the exercise name: ',
        'invalid_exercise_name': 'Please enter a valid exercise name.',
        'ask_another_exercise': (
            'Add another exercise for this day? '
            '[y]es / [n]o: '
        ),
        'ask_exercise_series': 'How many sets? ',
        'invalid_exercise_series': 'You must enter at least one set.',
        'ask_exercise_reps_min': 'Minimum reps: ',
        'ask_exercise_reps_max': 'Maximum reps: ',
        'invalid_exercise_reps': 'Invalid input. Please enter valid numbers.',
        'available_days': 'Available days:\n',
        'choose_day': '\nChoose a day or type [d]one to finish: ',
        'no_days_selected': 'You must select at least one day.',
        'invalid_day': 'Please choose a valid day.',
        'complete_workout': 'Workout created successfully!'
    }

    def __init__(self, storage):
        self.storage = storage
        self.workout_data = {}

    def _validate_name(self, name, error_msg):
        if not is_nonempty_string(name) or name.isdigit():
            raise ValueError(error_msg)
        return name.strip().title()

    def _validate_workout_name(self, name):
        return self._validate_name(
            name, self.CREATE_WORKOUT_MESSAGES['invalid_workout_name']
        )

    def _validate_exercise_name(self, name):
        return self._validate_name(
            name, self.CREATE_WORKOUT_MESSAGES['invalid_exercise_name']
        )

    def _validate_series(self, value):
        return validate_positive_int(
            value, self.CREATE_WORKOUT_MESSAGES['invalid_exercise_series']
        )

    def _validate_reps_min(self, value):
        return validate_positive_int(
            value, self.CREATE_WORKOUT_MESSAGES['invalid_exercise_reps']
        )

    def _validate_reps_max(self, value, reps_min):
        num = validate_positive_int(
            value, self.CREATE_WORKOUT_MESSAGES['invalid_exercise_reps']
        )
        if num < reps_min:
            raise ValueError(
                self.CREATE_WORKOUT_MESSAGES['invalid_exercise_reps']
            )
        return num

    def _ask_workout_name(self):
        clear_screen()
        return get_validated_input(
            self.CREATE_WORKOUT_MESSAGES['ask_workout_name'],
            self._validate_workout_name,
            self.CREATE_WORKOUT_MESSAGES['invalid_workout_name']
        )

    def _ask_exercise_name(self):
        clear_screen()
        return get_validated_input(
            self.CREATE_WORKOUT_MESSAGES['ask_exercise_name'],
            self._validate_exercise_name,
            self.CREATE_WORKOUT_MESSAGES['invalid_exercise_name']
        )

    def _ask_exercise_series(self):
        clear_screen()
        return get_validated_input(
            self.CREATE_WORKOUT_MESSAGES['ask_exercise_series'],
            self._validate_series,
            self.CREATE_WORKOUT_MESSAGES['invalid_exercise_series']
        )

    def _ask_exercise_reps(self):
        clear_screen()
        reps_min = get_validated_input(
            self.CREATE_WORKOUT_MESSAGES['ask_exercise_reps_min'],
            self._validate_reps_min,
            self.CREATE_WORKOUT_MESSAGES['invalid_exercise_reps']
        )
        reps_max = get_validated_input(
            self.CREATE_WORKOUT_MESSAGES['ask_exercise_reps_max'],
            lambda value: self._validate_reps_max(value, reps_min),
            self.CREATE_WORKOUT_MESSAGES['invalid_exercise_reps']
        )
        return reps_min, reps_max

    def _ask_day(self, available_days):
        while True:
            print(self.CREATE_WORKOUT_MESSAGES['available_days'])
            for i, day in enumerate(available_days):
                print(f"{i}) {day.capitalize()}")
            day_input = input(
                self.CREATE_WORKOUT_MESSAGES['choose_day']
            ).strip().lower()
            if day_input in ['d', 'done']:
                return 'done'
            if day_input.isdigit():
                index = int(day_input)
                if 0 <= index < len(available_days):
                    return available_days[index]
            elif day_input in available_days:
                return day_input
            clear_screen()
            print(self.CREATE_WORKOUT_MESSAGES['invalid_day'])

    def _ask_exercises_for_day(self, day):
        while True:
            exercise_name = self._ask_exercise_name()
            series = self._ask_exercise_series()
            reps_min, reps_max = self._ask_exercise_reps()
            self.workout_data['days'][day]['exercises'].append({
                'name': exercise_name,
                'series': series,
                'reps_min': reps_min,
                'reps_max': reps_max
            })
            clear_screen()
            while True:
                add_another = input(
                    self.CREATE_WORKOUT_MESSAGES['ask_another_exercise']
                ).strip().lower()
                if add_another in ['n', 'no']:
                    clear_screen()
                    return
                elif add_another in ['y', 'yes']:
                    clear_screen()
                    break
                else:
                    clear_screen()
                    print(global_messages['invalid_input'])

    def build_workout(self):
        workout_name = self._ask_workout_name()
        clear_screen()
        self.workout_data['name'] = workout_name
        self.workout_data['days'] = {}
        available_days = self.DAYS.copy()
        while available_days:
            chosen_day = self._ask_day(available_days)
            if chosen_day == 'done':
                if not self.workout_data['days']:
                    clear_screen()
                    print(self.CREATE_WORKOUT_MESSAGES['no_days_selected'])
                    continue
                break  
            self.workout_data['days'][chosen_day] = {'exercises': []}
            self._ask_exercises_for_day(chosen_day)
            available_days.remove(chosen_day)
        clear_screen()
        self.storage.save_workout(self.workout_data)
        print(self.CREATE_WORKOUT_MESSAGES['complete_workout'])


class EditWorkout(WorkoutAction):
    EDIT_WORKOUT_MESSAGES = {
        'ask_edit_workout': 'Which workout do you want to edit? ',
        'invalid_edit_workout_option': 'Invalid option.',
        'available_for_edit': 'Available for editing:\n',
        'ask_edit_workout_item': 'Which item do you want to edit? ',
        'ask_new_workout_name': 'What name would you like to use? '
    }

    def edit_workout(self):
        clear_screen()
        if check_empty_list(self.storage.workouts):
            return   
        selected_workout = self._list_and_select_workout(
            self.EDIT_WORKOUT_MESSAGES['ask_edit_workout']
        )
        if not selected_workout:
            return
        editing = True
        while editing:
            under_development = (
                '-== This menu is still under development.. ==-\n'
            )
            print(under_development)
            available_options = ['rename workout']
            workout_name_msg = (
                f"Workout: {selected_workout['name']}\n"
            )
            print(workout_name_msg)
            print(self.EDIT_WORKOUT_MESSAGES['available_for_edit'])
            for i, option in enumerate(available_options):
                print(f'{i}) {option.title()}')
            print(f"\n{global_messages['back']}")
            
            edit_input_option = input(
                self.EDIT_WORKOUT_MESSAGES['ask_edit_workout_item']
            ).strip().lower() 
            if edit_input_option in ['b', 'back']:
                clear_screen()
                break
            if edit_input_option == '0':
                self.rename_workout(
                    selected_workout,
                    workout_name_msg
                )
            else:
                clear_screen()
                print(
                    self.EDIT_WORKOUT_MESSAGES['invalid_edit_workout_option']
                )

    def rename_workout(self, workout, title_msg):
        rename_workout_flag = True
        while rename_workout_flag:
            clear_screen()
            print(title_msg)
            new_workout_name = input(
                self.EDIT_WORKOUT_MESSAGES['ask_new_workout_name']
            ).strip().title()
            old_name = workout['name']
            workout['name'] = new_workout_name
            self.storage.rename_workout_file(
                old_name, new_workout_name, workout
            )
            rename_workout_flag = False
            clear_screen()


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


class ListWorkout(WorkoutAction):
    LIST_WORKOUT_MESSAGES = {
        'view_workout': 'Which workout would you like to view? '
    }

    def list_workouts(self):
        clear_screen()
        if check_empty_list(self.storage.workouts):
            return
        while True:
            selected_workout = self._list_and_select_workout(
                self.LIST_WORKOUT_MESSAGES['view_workout']
            )
            if not selected_workout:
                return
            while True:
                clear_screen()
                print(self.format_workout(selected_workout))
                back = input(f"{global_messages['back']}")
                if back.strip().lower() in ['b', 'back']:
                    clear_screen()
                    break

    def format_workout(self, workout):
        workout_name = f"Workout: {workout['name']}\n"
        output = workout_name
        for day, info in workout['days'].items():
            output += f'\n{day.capitalize()}:\n'
            for exercises in info['exercises']:
                output += (
                    f"    - {exercises['name']}: "
                    f"{exercises['series']} series x "
                    f"{exercises['reps_min']}-{exercises['reps_max']} reps\n"
                )
        return output
