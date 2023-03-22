class Menu():

    def __init__(self, options):
        if not isinstance(options, list):
            raise TypeError("Menu options must be a list!")

        self.options = options

    def __str__(self):
        ppmenu = (
            '({}) {}\n'.format(
                str(idx + 1), option
            ) for idx, option in enumerate(self.options)
        )

        return ''.join(ppmenu) + '> '

    def addOption(self, option):
        self.options.append(option)

    def getChoice(self):

        choice = 0

        while choice not in range(1, len(self.options) + 1):
            try:
                choice = int(input(self))
                if choice not in range(1, len(self.options) + 1):
                    print('You must enter a number between {}, and {}!\n'.format(1, len(self.options)))

            except ValueError:
                print('You must enter a number!\n')

        return choice


