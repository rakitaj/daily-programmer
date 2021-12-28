namespace AdventOfCode2021
{
    public class Point : IEquatable<Point>
    {
        public int X { get; }
        public int Y { get; }

        public Point(int x, int y)
        {
            this.X = x;
            this.Y = y;
        }

        public override bool Equals(object? obj)
        {
            if (!(obj is Point)) { 
                return false; 
            } else {
                return this.Equals(obj as Point);
            }
        }

        public override int GetHashCode()
        {
            return this.X.GetHashCode() ^ this.Y.GetHashCode();
        }

        public override string ToString()
        {
            return $"({this.X}, {this.Y})";
        }

        public bool Equals(Point? other)
        {
            if (other is null) {
                return false;
            } else {
                return this.X == other.X && this.Y == other.Y;
            }
        }
    }
}
