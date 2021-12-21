using FluentAssertions;
using NUnit.Framework;

namespace AdventOfCode2021.Tests
{
    public class GridTests
    {
        [SetUp]
        public void Setup()
        {
            

        }

        [Test]
        public void TestGridGet()
        {
            var numbers = new int[][] { new[] { 1, 2, 3 }, new[] { 4, 5, 6 }, new[] { 7, 8, 9 } };
            var grid = new Grid<int>(numbers);
            grid.Get(1, 2).Should().Be(8);
        }
    }
}