using System.Collections.Generic;
using FluentAssertions;
using NUnit.Framework;

namespace AdventOfCode2021.Tests
{
    public class GridTests
    {
        public static readonly IList<string> rawPuzzleInput = new string[] {
            "5483143223",
            "2745854711",
            "5264556173",
            "6141336146",
            "6357385478",
            "4167524645",
            "2176841721",
            "6882881134",
            "4846848554",
            "5283751526"};

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

        [Test]
        public void TestSquareGridFromIntPuzzleInput()
        {
            var grid = Grid<int>.FromIntPuzzleInput(rawPuzzleInput);
            grid.Height.Should().Be(10);
            grid.Width.Should().Be(10);
            grid.Get(0, 0).Should().Be(5);
        }

        [Test]
        public void TestGetNeighboringPointsUpperLeft()
        {
            var grid = Grid<int>.FromIntPuzzleInput(rawPuzzleInput);
            var neighboringPoints = grid.GetNeighborPoints(0, 0);
            neighboringPoints.Count.Should().Be(3);
        }

        [Test]
        public void TestGetNeighboringPointsMiddle()
        {
            var grid = Grid<int>.FromIntPuzzleInput(rawPuzzleInput);
            var neighboringPoints = grid.GetNeighborPoints(1, 1);
            neighboringPoints.Count.Should().Be(8);
        }

        [Test]
        public void TestGetNeighboringPointsBottomMiddle()
        {
            var grid = Grid<int>.FromIntPuzzleInput(rawPuzzleInput);
            var neighboringPoints = grid.GetNeighborPoints(5, 9);
            neighboringPoints.Count.Should().Be(5);
        }
    }
}