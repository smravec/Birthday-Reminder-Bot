# Default Class
class Human:

    all_instances = []

    def __init__(self, name, birthday_date, nameday_date):
        # Attributes
        self.name = name
        self.birthday_date = birthday_date
        self.nameday_date = nameday_date

        # Counting all instances
        self.__class__.all_instances.append(self)