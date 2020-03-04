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
     def search(self):
         pass
     def is_predatory(self, name):
         result = self.search(name)
         if result:
             return self.warn_predatory(result)
         else:
             return self.probably_not_predatory(result)
