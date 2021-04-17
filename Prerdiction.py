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
        changetime = "05:30:00"
        change_date_time_obj = datetime.strptime(changetime, '%H:%M:%S')
        hour = hour-change_date_time_obj.hour
        if hour<0:
            hour = 0
        print("new time",hour)
        end_date_time_obj = datetime.strptime(self.endTime, '%H:%M:%S')
        endHour = end_date_time_obj.hour
        change_date_time_obj = datetime.strptime(changetime, '%H:%M:%S')
        endHour = endHour - change_date_time_obj.hour
        if endHour<0:
            endHour = 0
        print("new end time", endHour)
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
        irradianceArray=[]
        for i in range(numHour):
            test_data = np.array([hour, day_of_month, day_of_week, month, year])
            irradaiance = model.predict(test_data.reshape(1, 5))
            print(i,irradaiance)
            hour = hour + 1
            predIrr= predIrr + irradaiance[0]
            irradianceArray.insert(i,irradaiance[0])
            print(predIrr)
            print(irradianceArray)
        return irradianceArray

# x = Prediction("2005-04-01", "6:00:00","7:00:00")
# x.getIrradiance()











# with open('final_decision_Tree_model', 'rb') as f:
#     model = pickle.load(f)
#
# test_data = np.array([16, 2, 5, 1, 2021])
# answer =model.predict(test_data.reshape(1, 5))
# print(answer)
# list = answer.tolist()
# print(list[0])

