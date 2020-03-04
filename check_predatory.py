import json

class PredatoryInfo():
     predatory_path = "../is_predatory/is_predatory/spiders/predatory_journals.json"
     def __init__(self):
         self._load(self.predatory_path)
     def _load(self, path):
         with open(path) as handle:
             self._data = json.load(handle)[0]
     def update(self):
         pass
     def search(self, name):
         def matches_domain(query_domain, db_domain):
             return query_domain == db_domain
         def matches_name(query_name, db_name):
             return query_name == db_name
         for listing_id in self._data:
             listing = self._data[listing_id]
             if matches_domain(name, listing["url"]):
                 return listing
             if matches_name(name, listing["name"]):
                 return listing
         return {}
     def warn_predatory(self, result):
         return "The journal {0} at {1} is listed as a predatory journal in Beall's List.".format(result["name"], result["url"]
     def probably_not_predatory(self, name):
         return "{0} is not listed as a predatory journal. To judge for yourself, read more at https://thinkchecksubmit.org/".format(name
     def is_predatory(self, name):
         result = self.search(name)
         if result:
             return self.warn_predatory(result)
         else:
             return self.probably_not_predatory(name)
