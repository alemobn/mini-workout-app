
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
        create = Create_workout()
        create.workout_infos['name'] = create.ask_workout_name()
        create.ask_workout_days()
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

  
class Create_workout():
  create_workout_messages = {
    'name': 'What is the name of the workout?\n\n',
    'name_error': 'Workout name cannot be empty!\n',
    'choose_day': 'Choose the day or type [d]one if finished: ',
    'no_days_selected': 'You must select at least one day!',
    'day_error': 'Select a valid day!\n'
  }

  def __init__(self):
    self.workout_infos = {}
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
    name = ''
    while not name:
      name_typing = input(self.create_workout_messages['name'])
      if len(name_typing) < 1:
        print(self.create_workout_messages['name_error'])
        continue
      else:
        name = name_typing.strip().title()
    return name
  
  def ask_workout_days(self):
    day_name_options = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    number_of_days = 0
    day = ''
    while not day:
      for index, day_option in enumerate(day_name_options):
        print(f'{index})', day_option.capitalize())
      
      print()
      day_typing = input(self.create_workout_messages['choose_day']).strip().lower()
      
      if day_typing in ['d', 'done'] and number_of_days == 0:
        print(self.create_workout_messages['no_days_selected'])
        continue
      elif day_typing in ['d', 'done']:
        break
      else:
        if day_typing.isdigit():
          index = int(day_typing)
          if index >= 0 and index < len(day_name_options):
            chosen_day = day_name_options[index]
            day = chosen_day
            number_of_days += 1
        elif day_typing in day_name_options:
          day = day_typing
          number_of_days += 1
        else:
          print(self.create_workout_messages['day_error'])
          continue
      break

    print(day)


Menu()
