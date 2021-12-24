from algos import Grid, Point


class OctopusGrid(Grid):
    def increase(self) -> list[Point]:
        """Increase every Octopus energy level by 1 and return the list of points
        that have 9 or more power, which means they will flash in the next step."""
        will_flash: list[Point] = list()
        for x in range(self.x_length):
            for y in range(self.y_length):
                val = self.get(x, y)
                if val is None:
                    continue
                if 9 <= val + 1:
                    will_flash.append(Point(x, y))
                self.set(x, y, val + 1)
        return will_flash

    def flash(self, flash_points: list[Point]) -> int:
        """Get a list of every college that needs to flash, and execute the flash."""
        count = 0
        extra_flash_points: list[Point] = list()
        for fp in flash_points:
            # Get neighboring points
            pass
        return count
