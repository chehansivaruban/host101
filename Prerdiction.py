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
        end_date_time_obj = datetime.strptime(self.endTime, '%H:%M:%S')
        endHour = end_date_time_obj.hour
        change_date_time_obj = datetime.strptime(changetime, '%H:%M:%S')
        endHour = endHour - change_date_time_obj.hour
        if endHour<0:
            endHour = 0


        date_obj = datetime.strptime(self.date, '%Y-%m-%d')

        day_of_month = date_obj.day


        day_of_week = date_obj.weekday()


        month = date_obj.month


        year = date_obj.year

        with open('final_decision_Tree_model.pkl', 'rb') as f:
            model = pickle.load(f)

        numHour = endHour - hour
        predIrr = 0
        irradianceArray=[]
        for i in range(numHour):
            test_data = np.array([hour, day_of_month, day_of_week, month, year])
            irradaiance = model.predict(test_data.reshape(1, 5))
            hour = hour + 1
            predIrr= predIrr + irradaiance[0]
            irradianceArray.insert(i,irradaiance[0])

        return irradianceArray









