#!/bin/python3
# Imports
import requests

id = int(input("Starting ID: "))

try:
    while True:
        response = requests.get(f"https://trainingserver.atec.pt/TrainingServer/Mulberry/JSON/Controls/Calendar/getCalendarDataSource.ashx?command=_SelectAllSchedulesDataSetGivenByUserId&oId={id}&idField=DataValueField&titleField=DataTextField&startDateField=DataStartField&endDateField=DataEndField&backgroundColorField=&textColorField=textcolor&eventColorField=color&description=description&picField=pic&urlField=url&start=1746399600&end=1747004400&_=1746736138904")
        if "Sessão como Formador" in response.text and "Rogélio" in response.text:
            print(f"Found him! {id}")
            id += 1
            break
        else:
            id += 1
            print(id)
except:
    print(id)
