
class Menu():
  main_menu_messages = {
      'welcome': '-== welcome! ==-\n',
      'options': '1. Create workout\n2. Edit workout\n3. Delete workout\n4. List workouts\n5. Exit\n\n'
    }
  
  def __init__(self):
    self.loop_menu()

  def loop_menu(self):
    print(Menu.main_menu_messages['welcome'])

    while True:
      user_option = input(Menu.main_menu_messages['options'])
      user_option = user_option.lower().strip()

      print()

      if user_option in ['1', 'create', 'create workout']:
        create = CreateWorkout()
        create.workout_data['name'] = create.ask_workout_name()
        create.workout_data['days'] = create.ask_workout_days()
        break
      elif user_option in ['2', 'edit', 'edit workout']:
        print('edit workout')
        break
      elif user_option in ['3', 'delete', 'delete workout']:
        print('delete workout')
        break
      elif user_option in ['4', 'list', 'list workout']:
        print('exit')
        break
      elif user_option in ['5', 'exit']:
        print('exit')
        break
      else:
        print('invalid option')
        break

  
class CreateWorkout():
  create_workout_messages = {
    'ask_workout_name': 'What is the name of the workout?\n\n',
    'ask_workout_name_empty': 'Workout name cannot be empty!\n',
    'choose_day': 'Choose the day or type [d]one if finished: ',
    'choose_day_empty': 'You must select at least one day!',
    'choose_day_invalid': 'Select a valid day!\n',
    'ask_exercise_name': 'What is the exercise name? ',
    'ask_exercise_name_invalid': 'Enter a valid exercise name.\n',
    'ask_exercise_series': 'How many series? ',
    'ask_exercise_series_empty': 'You must enter at least one series',
    'ask_exercise_reps_min': 'How many minimum reps?',
    'ask_exercise_reps_max': 'How many maximum reps?',
    'ask_exercise_reps_not_number': 'Type only numbers!\n',
    'ask_exercise_reps_empty': 'You must enter at least one rep.'
  }

  def __init__(self):
    self.workout_data = {}
      # 'name': '',
      # 'days': {
      #   'monday': {
      #     'exercises': [
      #       {'name': '', 'series': '', 'reps': ''}
      #     ]
      #   },
      #   'tuesday': {},
      #   'wednesday': {},
      #   'thursday': {},
      #   'friday': {},
      #   'saturday': {},
      #   'sunday': {}
      # }

  def ask_workout_name(self):
    workout_name = ''
    while not workout_name:
      workout_name_input = input(self.create_workout_messages['ask_workout_name'])
      if len(workout_name_input) < 1:
        print(self.create_workout_messages['ask_workout_name_empty'])
        continue
      else:
        workout_name = workout_name_input.strip().title()
    return workout_name
  
  def ask_workout_days(self):
    day_name_options = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    num_selected_days = 0
    chosen_day = ''
    while not chosen_day:
      for index, day_option in enumerate(day_name_options):
        print(f'{index})', day_option.capitalize())
      
      print()
      day_input = input(self.create_workout_messages['choose_day']).strip().lower()
      
      if day_input in ['d', 'done'] and num_selected_days == 0:
        print(self.create_workout_messages['choose_day_empty'])
        continue
      elif day_input in ['d', 'done']:
        break
      else:
        if day_input.isdigit():
          index = int(day_input)
          if index >= 0 and index < len(day_name_options):
            chosen_day = day_name_options[index]
            num_selected_days += 1
        elif day_input in day_name_options:
          chosen_day = day_input
          num_selected_days += 1
        else:
          print(self.create_workout_messages['choose_day_invalid'])
          continue
      break

  def ask_exercise_name(self):
    exercise_name = ''
    while not exercise_name:
      exercise_name_input = input(self.create_workout_messages['ask_exercise_name']).strip()
      if exercise_name_input.isdigit() or len(exercise_name_input) < 1:
        print(self.create_workout_messages['ask_exercise_name_invalid'])
        continue
      else:
        exercise_name = exercise_name_input.title()
    return exercise_name

  def ask_exercise_series(self):
    exercise_series = 0
    while exercise_series <= 0:
      exercise_series_input = input(self.create_workout_messages['ask_exercise_series']).strip()
      if not exercise_series_input.isdigit():
        print(self.create_workout_messages['ask_exercise_series_empty'])
        continue
      exercise_series = int(exercise_series_input)
    return exercise_series
  
  def ask_exercise_reps(self):
    exercise_reps_min = 0
    exercise_reps_max = 0
    while exercise_reps_min <= 0 or exercise_reps_max <= 0:
      exercise_reps_min_input = input(self.create_workout_messages['ask_exercise_reps_min'])
      exercise_reps_max_input = input(self.create_workout_messages['ask_exercise_reps_max'])
      check_inputs_not_numbers = not exercise_reps_min_input.isdigit() or not exercise_reps_max_input.isdigit()
      check_inputs_value_zero = int(exercise_reps_min_input) == 0 or int(exercise_reps_max_input) == 0 
      if check_inputs_not_numbers:
        print(self.create_workout_messages['ask_exercise_reps_not_number'])
        continue
      if check_inputs_value_zero:
        print(self.create_workout_messages['ask_exercise_reps_empty'])
        continue
      exercise_reps_min_input_int = int(exercise_reps_min_input)
      exercise_reps_max_input_int = int(exercise_reps_max_input)
      exercise_reps_min = exercise_reps_min_input_int
      exercise_reps_max = exercise_reps_max_input_int
    return exercise_reps_min, exercise_reps_max

Menu()
