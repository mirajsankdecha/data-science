class TimeConverter:
    def __init__(self, value):
    #Initialize with the value to convert.
        self.value = value

    def seconds_to_minutes(self):
    #Convert seconds to minutes.
        return self.value / 60

    def seconds_to_hours(self):
    #Convert seconds to hours.
        return self.value / 3600

    def minutes_to_seconds(self):
    #Convert minutes to seconds.
        return self.value * 60

    def hours_to_seconds(self):
    #Convert hours to seconds.
        return self.value * 3600

    def hours_to_minutes(self):
    #Convert hours to minutes.
        return self.value * 60
