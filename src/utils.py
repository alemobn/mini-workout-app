import os

global_messages = {
    'welcome': '-== Welcome! ==-',
    'back': 'Type [b]ack to return ',
    'invalid_workout': 'Invalid workout selection.',
    'empty_workout': 'No workout was found.',
    'listed_workouts': 'Workouts found',
    'invalid_input': 'Invalid input.',
}


def clear_screen():
    system = os.name
    if system == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def check_empty_list(workouts):
    if len(workouts) == 0:
        print(global_messages['empty_workout'])
        return True
    return False


def list_workouts(msg, workouts):
    message = (
        f"{msg} "
        f"({len(workouts)}):\n"
    )
    return message


def is_nonempty_string(value):
    return isinstance(value, str) and value.strip() != ""


def get_validated_input(prompt, validate_func, error_msg):
    while True:
        value = input(prompt).strip()
        try:
            return validate_func(value)
        except ValueError:
            print(error_msg)


def validate_is_digit(value, error_msg):
    if not value.isdigit():
        raise ValueError(error_msg)
    return int(value)


def validate_positive_int(value, error_msg):
    num = validate_is_digit(value, error_msg)
    if num <= 0:
        raise ValueError(error_msg)
    return num
