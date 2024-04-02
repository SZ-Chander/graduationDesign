class WorkSchedulePage:
    def __init__(self):
        self.workScheduleList = None
        self.staff = None

    def setWorkScheduleList(self,workScheduleList):
        self.workScheduleList = workScheduleList
    def setStaff(self,staff):
        self.staff = staff

    def getStaff(self):
        return self.staff
    def getWorkScheduleList(self):
        return self.workScheduleList