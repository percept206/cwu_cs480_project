class BaseParser:
    def __init__(self):
        pass

    def parse(self, data):
        raise NotImplementedError("Parse method must be implemented by subclasses.")