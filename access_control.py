from constants import ADMIN_USERNAME, UNKNOWN_COMMAND


def access_control(method):
    def wrapper(self, *args, **kwargs):
        if self.username == ADMIN_USERNAME:
            method(self, *args, **kwargs)
        else:
            print(UNKNOWN_COMMAND)
    return wrapper
