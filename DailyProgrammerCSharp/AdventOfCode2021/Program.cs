// See https://aka.ms/new-console-template for more information
using System;
using AdventOfCode2021;

Console.WriteLine("Hello, World!");
var puzzleInput = PuzzleInput.ToArrayOfStrings(10);
Console.WriteLine($"Syntax Scoring 2 {SyntaxScoring.SyntaxScoring2(puzzleInput)}");
Console.WriteLine($"Dumbo Octopus 1 {DumboOctopus_Part1()}");

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
