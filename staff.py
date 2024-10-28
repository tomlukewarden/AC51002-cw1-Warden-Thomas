class StaffData:
    def __init__(self, name, staff_id, hours_worked, items_produced):
        self.name = name
        self.staff_id = staff_id
        self.hours_worked = hours_worked
        self.items_produced = items_produced  

    def output(self):
        print('Operator name is: {:10s}'.format(self.name))
        print('This operator\'s unique ID is {:4d}'.format(self.staff_id))
        print('The hours worked by this operator is a total of {:4d}'.format(self.hours_worked))
        
