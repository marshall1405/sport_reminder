class League:
    def __init__(self, id, start_index, end_index, name, single):
        self.id = id
        self.start_index = start_index
        self.end_index = end_index
        self.name = None
        self.single = None

    def set_name(self, name):
        self.name = name

    def set_single(self, single):
        self.single = single
