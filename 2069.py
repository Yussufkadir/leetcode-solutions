from typing import List
class Robot:

    def __init__(self, width: int, height: int):
        self.perimeter = 2 * (width + height - 2)
        self.pos = 0
        self.path = []
        self.started = False

        for x in range(width):
            self.path.append((x, 0, "East"))
        for y in range(1, height):
            self.path.append((width - 1, y, "North"))
        for x in range(width - 2, -1, -1):
            self.path.append((x, height - 1, "West"))
        for y in range(height - 2, 0, -1):
            self.path.append((0, y, "South"))

    def step(self, num: int) -> None:
        self.started = True
        self.pos = (self.pos + num) % self.perimeter

    def getPos(self) -> List[int]:
        x, y, _ = self.path[self.pos]
        return [x, y]

    def getDir(self) -> str:
        _, _, d = self.path[self.pos]
        if self.started and self.pos == 0:
            return "South"
        return d
