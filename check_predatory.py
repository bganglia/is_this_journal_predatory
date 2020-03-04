import json

class PredatoryInfo():
     self.predatory_path = ""
     def __init__(self):
         self._load(predatory_path)
     def _load(self):
         with open(self.predatory_path) as handle:
             self._data = json.load(handle)
     def update(self):
         pass
     def is_predatory(self, name):
         pass
