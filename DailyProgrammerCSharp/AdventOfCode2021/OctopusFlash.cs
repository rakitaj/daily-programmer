namespace AdventOfCode2021
{
    public class OctopusFlash
    {
        public Grid<int> OctopusGrid { get; }

        public OctopusFlash(Grid<int> grid)
        {
            this.OctopusGrid = grid;
        }

        public int Tick()
        {
            var flashPoints = this.Increase();
            var alreadyFlashed = this.Flash(flashPoints);
            this.ZeroOutFlashed(alreadyFlashed);
            return alreadyFlashed.Count;
        }

        private void ZeroOutFlashed(HashSet<Point> alreadyFlashed)
        {
            foreach(var point in alreadyFlashed) {
                this.OctopusGrid.Set(point.X, point.Y, 0);
            }
        }

        public HashSet<Point> Increase()
        {
            var flashPoints = new HashSet<Point>();
            for (int x = 0; x < this.OctopusGrid.Width; x++) {
                for (int y = 0; y < this.OctopusGrid.Height; y++) {
                    var currentValue = this.OctopusGrid.Get(x, y);
                    this.OctopusGrid.Set(x, y, currentValue + 1);
                    if (10 <= this.OctopusGrid.Get(x, y)) {
                        flashPoints.Add(new Point(x, y));
                    }
                }
            }
            return flashPoints;
        }

        public HashSet<Point> Flash(HashSet<Point> flashPoints)
        {
            var flashQueue = new Queue<Point>(flashPoints);
            var alreadyFlashed = new HashSet<Point>();
            while (0 < flashQueue.Count) {
                var flashPoint = flashQueue.Dequeue();
                if (!alreadyFlashed.Contains(flashPoint)) {
                    alreadyFlashed.Add(flashPoint);
                    var neighboringPoints = this.OctopusGrid.GetNeighborPoints(flashPoint.X, flashPoint.Y);
                    foreach (var p in neighboringPoints) {
                        var value = this.OctopusGrid.Get(p.X, p.Y);
                        this.OctopusGrid.Set(p.X, p.Y, value + 1);
                        if (10 <= this.OctopusGrid.Get(p.X, p.Y)) {
                            flashQueue.Enqueue(p);
                        }
                    }
                }
                

            }
            return alreadyFlashed;
        }
    }
}
