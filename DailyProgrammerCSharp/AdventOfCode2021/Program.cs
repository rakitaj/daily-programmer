// See https://aka.ms/new-console-template for more information
using System;
using AdventOfCode2021;

Console.WriteLine("Hello, World!");
var puzzleInput = PuzzleInput.ToArrayOfStrings(10);
Console.WriteLine($"Syntax Scoring 2 {SyntaxScoring.SyntaxScoring2(puzzleInput)}");

