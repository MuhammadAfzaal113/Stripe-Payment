from sys import platform


class Config:

    @staticmethod
    def mode(mode_selection):
        def check_os():
            if platform == "linux" or platform == "linux2" or platform == "darwin":
                return "linux"

            elif platform == "win32" or platform == "win64":
                return "windows"
            else:
                # In case it doesnt know OS then choose windows by default
                return "windows"

        os_env = check_os()

        if mode_selection == 'development':
            return 1
        elif mode_selection == 'production':
            return 3
        elif mode_selection == 'stagging':
            return 2

    @staticmethod
    def environment(mode_selection):
        if mode_selection == 'development':
            from stripe_example.environment import development
            return development
        elif mode_selection == 'production':
            from stripe_example.environment import production
            return production
        elif mode_selection == 'staging':
            from stripe_example.environment import staging
            return staging


if __name__ == '__main__':
    pass
