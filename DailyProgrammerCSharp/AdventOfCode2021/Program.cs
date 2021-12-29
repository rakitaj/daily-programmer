// See https://aka.ms/new-console-template for more information
using System;
using AdventOfCode2021;

Console.WriteLine("Hello, World!");
var puzzleInput = PuzzleInput.ToArrayOfStrings(10);
Console.WriteLine($"Syntax Scoring 2 {SyntaxScoring.SyntaxScoring2(puzzleInput)}");
Console.WriteLine($"Dumbo Octopus 1 {DumboOctopus_Part1()}");
Console.WriteLine($"Dumbo Octopus 2 {DumboOctopus_Part2()}");

int DumboOctopus_Part1()
{
    var puzzleInput = PuzzleInput.ToArrayOfStrings(11);
    var grid = Grid<int>.FromIntPuzzleInput(puzzleInput);
    var octopusFlash = new OctopusFlash(grid);
    List<int> totals = new List<int>();
    for (int i = 0; i < 100; i++) {
        totals.Add(octopusFlash.Tick());
    }
    return totals.Sum();
}

int DumboOctopus_Part2()
{
    var puzzleInput = PuzzleInput.ToArrayOfStrings(11);
    var grid = Grid<int>.FromIntPuzzleInput(puzzleInput);
    var octopusFlash = new OctopusFlash(grid);
    for (int i = 0; i < 1000; i++) {
        if (octopusFlash.Tick() == 100) {
            // Do the plus one because the first tick of 0 index is considered 1 by the puzzle.
            return i + 1;
        }
    }
    return -1;
}