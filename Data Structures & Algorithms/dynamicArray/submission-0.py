class DynamicArray:
    
    def __init__(self, capacity: int):
        self.da = []
        self.capacity = capacity

    def get(self, i: int) -> int:
        return self.da[i]


    def set(self, i: int, n: int) -> None:
        self.da[i] = n

    def pushback(self, n: int) -> None:
        end_i = len(self.da)
        if self.capacity == end_i:
            self.capacity *= 2
        self.da.append(n)


    def popback(self) -> int:
        return self.da.pop()

    def resize(self) -> None:
        extend = [0] * len(self.da)
        self.da.extend(extend)

    def getSize(self) -> int:
        return len(self.da)
        
    def getCapacity(self) -> int:
        return self.capacity