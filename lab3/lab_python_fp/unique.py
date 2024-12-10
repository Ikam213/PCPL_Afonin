class Unique(object):
    def __init__(self, items, **kwargs):
        self.used_elements = set()
        self.items = items
        self.counter = 0
        if len(kwargs) != 0:
            self.ignore_case = kwargs
        else:
            self.ignore_case = False

    def __next__(self):
        while True:
            for item in self.items:
                temp_item = item
                self.counter += 1
                if (temp_item not in self.used_elements):
                  if not(self.ignore_case):
                      self.used_elements.add(temp_item)
                      return temp_item
                  else:
                   if not(temp_item.swapcase() in self.used_elements):
                       self.used_elements.add(temp_item)
                       return temp_item
            else:
                raise StopIteration

    def __iter__(self):
        return self
