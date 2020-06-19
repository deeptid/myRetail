class Parser(object):
  def __init__(self, response):
     self.response = response

  def getValueOf(self, path):
     """
     :param path: json path
     :return: value evaluated from json dict if present else None
     """
     path = str(path)
     attributes = path.split('.')
     result = self.response

     for attr in attributes:
        if result is not None:
           if attr.__contains__("["):
              responseListName = attr[:attr.index("[")]
              startOfIndex = attr.index("[") + 1
              endOfIndex = attr.rindex("]")
              index = int(attr[startOfIndex:endOfIndex])
              if not result.get(responseListName):
                 return None
              result = result.get(responseListName)[index] if len(result.get(responseListName)) > index else None
           else:
              result = result.get(attr, None)
     if result:
        if isinstance(result, dict) and result.__contains__("$"):
           for key, val in result.items():
              if key == '$':
                 return val if val else None

     return result

