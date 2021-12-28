namespace AdventOfCode2021
{
    public class Grid<T> : IEquatable<Grid<T>> where T : IEquatable<T>
    {
        public readonly List<List<T>> grid;

        public int Height => this.grid.Count;
        public int Width => this.grid.First().Count;

        public Grid(IList<IList<T>> rawGrid)
        {
            List<List<T>> g = new List<List<T>>();
            foreach (var row in rawGrid) {
                g.Add(row.ToList());
            }
            this.grid = g;
        }

        public T Get(int x, int y)
        {
            return this.grid[y][x];
        }

        public void Set(int x, int y, T value)
        {
            this.grid[y][x] = value;
        }

        public HashSet<Point> GetNeighborPoints(int x, int y)
        {
            var result = new HashSet<Point>();
            for (int xOffset = -1; xOffset <= 1; xOffset++) {
                for (int yOffset = -1; yOffset <= 1; yOffset++) {
                    var xWithOffset = x + xOffset;
                    var yWithOffset = y + yOffset;
                    if (xWithOffset < 0 || yWithOffset < 0 || this.Width <= xWithOffset || this.Height <= yWithOffset) {
                        continue;
                    }
                    if (xOffset == 0 && yOffset == 0) {
                        continue;
                    }
                    result.Add(new Point(xWithOffset, yWithOffset));
                }
            }
            return result;
        }

        public static Grid<int> FromIntPuzzleInput(IList<string> puzzleInput, string splitString = "")
        {
            var rawGrid = new List<IList<int>>();
            foreach (var row in puzzleInput) {
                List<int> numbers = new List<int>();
                if (String.IsNullOrEmpty(splitString)) {
                    numbers.AddRange(row.ToCharArray().Select(x => x.ToInt()));
                }
                else {
                    numbers.AddRange(row.Split(splitString).Select(x => int.Parse(x)));
                }
                rawGrid.Add(numbers);
            }
            return new Grid<int>(rawGrid);
        }

        public bool Equals(Grid<T>? other)
        {
            if (other == null || this.Width != other.Width || this.Height != other.Height) {
                return false;
            }
            else {
                for (int x = 0; x < this.Width; x++) {
                    for (int y = 0; y < this.Height; y++) {
                        if (this.Get(x, y).Equals(other.Get(x, y)) == false) {
                            return false;
                        }
                    }
                }
                return true;
            }
        }

        public override bool Equals(object? obj)
        {
            if (obj is Grid<T>) {
                return this.Equals(obj as Grid<T>);
            } else {
                return false;
            }
        }

        public override int GetHashCode()
        {
            int hashCode = 0;
            for (int x = 0; x < this.Width; x++) {
                for (int y = 0; y < this.Height; y++) {
                    hashCode = hashCode ^ this.Get(x, y).GetHashCode();
                }
            }
            return hashCode;
        }
    }
}
