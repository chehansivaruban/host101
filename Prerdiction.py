import pickle
import numpy as np
from datetime import datetime


class Prediction:
    def __init__(self, date, time,endTime):
        self.date = date
        self.time = time
        self.endTime = endTime

    def getIrradiance(self):
        date_time_obj = datetime.strptime(self.time, '%H:%M:%S')
        hour = date_time_obj.hour

        end_date_time_obj = datetime.strptime(self.endTime, '%H:%M:%S')
        endHour = end_date_time_obj.hour
        # print(hour)
        date_obj = datetime.strptime(self.date, '%Y-%m-%d')

        day_of_month = date_obj.day
        # print(day_of_month)

        day_of_week = date_obj.weekday()
        # print(day_of_week)

        month = date_obj.month
        # print(month)

        year = date_obj.year
        # print(year)
        with open('final_decision_Tree_model.pkl', 'rb') as f:
            model = pickle.load(f)

        numHour = endHour - hour
        predIrr = 0
        for i in range(numHour):
            test_data = np.array([hour, day_of_month, day_of_week, month, year])
            irradaiance = model.predict(test_data.reshape(1, 5))
            print(i,irradaiance)
            hour = hour + 1
            predIrr= predIrr + irradaiance[0]
            print(predIrr)
        return predIrr

# x = Prediction("2005-01-01", "01:00:00")
# x.getIrradiance()











# with open('final_decision_Tree_model', 'rb') as f:
#     model = pickle.load(f)
#
# test_data = np.array([16, 2, 5, 1, 2021])
# answer =model.predict(test_data.reshape(1, 5))
# print(answer)
# list = answer.tolist()
# print(list[0])

