class Funcs():
    def add(self, num):
        self.viewer_values = self.viewer_values + str(num)
        self.viewer_text.set(self.viewer_values)
    def clear(self):
        self.viewer_values = ''
        self.viewer_text.set(self.viewer_values)
    def equals(self):
        self.viewer_values = str(eval(self.viewer_values))
        self.viewer_text.set(self.viewer_values)
    def log(self):
        pass
    def sin(self):
        pass
    def cos(self):
        pass
    def tan(self):
        pass
