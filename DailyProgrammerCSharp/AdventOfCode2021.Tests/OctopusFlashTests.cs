using System.Collections.Generic;
using System.Linq;
using FluentAssertions;
using NUnit.Framework;

namespace AdventOfCode2021.Tests
{
    internal class OctopusFlashTests
    {
        public string[] LargePuzzleInput => new string[] {
            "5483143223",
            "2745854711",
            "5264556173",
            "6141336146",
            "6357385478",
            "4167524645",
            "2176841721",
            "6882881134",
            "4846848554",
            "5283751526"
            };

        public string[] LargePuzzleInput_1_Tick => new string[] {
            "6594254334",
            "3856965822",
            "6375667284",
            "7252447257",
            "7468496589",
            "5278635756",
            "3287952832",
            "7993992245",
            "5957959665",
            "6394862637"
        };

        public string[] LargePuzzleInput_2_Tick => new string[] {
            "8807476555",
            "5089087054",
            "8597889608",
            "8485769600",
            "8700908800",
            "6600088989",
            "6800005943",
            "0000007456",
            "9000000876",
            "8700006848"
        };

        public string[] SmallPuzzleInput => new string[] { "11111", "19991", "19191", "19991", "11111" };

        public string[] SmallPuzzleInput_1_Tick => new string[] { "34543", "40004", "50005", "40004", "34543" };

        public string[] SmallPuzzleInput_2_Tick => new string[] { "45654", "51115", "61116", "51115", "45654" };

        [Test]
        public void SmallPuzzleInputTicks()
        {
            var grid = Grid<int>.FromIntPuzzleInput(this.SmallPuzzleInput);
            var octopusFlash = new OctopusFlash(grid);
            octopusFlash.Tick().Should().Be(9);
        }

        [Test]
        public void SmallPuzzleInputTickAndGridEquality()
        {
            var grid = Grid<int>.FromIntPuzzleInput(this.SmallPuzzleInput);
            var octopusFlash = new OctopusFlash(grid);
            octopusFlash.Tick().Should().Be(9);
            var expectedGrid1 = Grid<int>.FromIntPuzzleInput(this.SmallPuzzleInput_1_Tick);
            octopusFlash.OctopusGrid.Should().Be(expectedGrid1);
            var expectedGrid2 = Grid<int>.FromIntPuzzleInput(this.SmallPuzzleInput_2_Tick);
            octopusFlash.Tick().Should().Be(0);
            octopusFlash.OctopusGrid.Should().Be(expectedGrid2);
        }

        [TestCase(10, 204)]
        [TestCase(100, 1656)]
        public void LargePuzzleInputTicks(int numTicks, int expectedFlashes)
        {
            var grid = Grid<int>.FromIntPuzzleInput(this.LargePuzzleInput);
            var octopusFlash = new OctopusFlash(grid);
            List<int> totals = new List<int>();
            for (int i = 0; i < numTicks; i++) {
                totals.Add(octopusFlash.Tick());
            }
            totals.Sum().Should().Be(expectedFlashes);
        }

        [Test]
        public void LargePuzzleInputAfter1Tick()
        {
            var grid = Grid<int>.FromIntPuzzleInput(this.LargePuzzleInput);
            var expected = Grid<int>.FromIntPuzzleInput(this.LargePuzzleInput_1_Tick);
            var octopusFlash = new OctopusFlash(grid);
            octopusFlash.Tick();
            octopusFlash.OctopusGrid.Should().Be(expected);
        }

        [Test]
        public void LargePuzzleInputAfter2Tick()
        {
            var grid = Grid<int>.FromIntPuzzleInput(this.LargePuzzleInput);
            var expected = Grid<int>.FromIntPuzzleInput(this.LargePuzzleInput_2_Tick);
            var octopusFlash = new OctopusFlash(grid);
            octopusFlash.Tick();
            octopusFlash.Tick();
            octopusFlash.OctopusGrid.Should().Be(expected);
        }
    }
}
