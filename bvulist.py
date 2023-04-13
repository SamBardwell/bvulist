
class bvulist(list):
    def prepend(self, value):
        self.insert(0, value)
# This is a test
    def pop_back(self):
        return self.pop()

    def pop_front(self):
        save = self[0]
        del self[0]
        return save
        
