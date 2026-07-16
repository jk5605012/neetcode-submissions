class PrefixTree:

    def __init__(self):
        self.cell = []

    def insert(self, word: str) -> None:
        self.cell.append(word)

    def search(self, word: str) -> bool:
        if word in self.cell:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        for i in self.cell:
            if str(i).startswith(prefix):
                return True
        return False