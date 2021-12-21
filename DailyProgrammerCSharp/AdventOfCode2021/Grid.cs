using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdventOfCode2021
{
    public class Grid<T>
    {
        public readonly List<List<T>> grid;

        public Grid(IList<IList<T>> rawGrid)
        {
            List<List<T>> g = new List<List<T>>();
            foreach(var row in rawGrid) 
            {
                g.Add(row.ToList());
            }
            this.grid = g;
        }

        public T Get(int x, int y)
        {
            return grid[y][x];
        }
    }
}
