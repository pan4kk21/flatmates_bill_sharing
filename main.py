class Bill:
    """
    An object that contains data about a bill, such as total amount and a period of the bill
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    An object that contains data about the flatmate such as name,
    number of days spent in the house during the period and the amount to be paid for the period
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill):
        pass


class PDFReport:
    """An object that creates a pdf file with information on all flatmates and bill """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass
