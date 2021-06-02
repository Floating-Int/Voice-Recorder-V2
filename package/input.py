import keyboard


class Input:

    @staticmethod
    def is_action_pressed(action):  # -> bool
        return keyboard.is_pressed(action)
