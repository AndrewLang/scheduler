import json
from .schedule_model import ScheduleModel

class Schedules:
    """
    {
        "schedules": [
            {
                "name": "",
                "description":"",
                "path":"",
                "args":"",
                "time":""
            }
        ]
    }
    """

    def __init__(self):
        self.models=[]


    def load(self, file):
        with open(file) as raw:
            data = json.load(raw)
            for item in data['schedules']:
                model = ScheduleModel()
                model.name = item['name']
                model.description = item['description']
                model.path = item['path']
                model.args = item['args']
                model.time = item['time']
                models.append(model)


