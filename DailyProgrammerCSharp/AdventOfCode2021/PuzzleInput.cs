using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdventOfCode2021
{
    public class PuzzleInput
    {
        public static string GetFilePath(int dayNumber)
        {
            var dayWithLeadingZeros = dayNumber.ToString("D2");
            string filePath = Path.Join("..", "..", "..", "..", "..", "aoc2021", "puzzleinput", $"day{dayWithLeadingZeros}.txt");
            return filePath;
        }

        public static string[] ToArrayOfStrings(Func<string> getFilePathFunc)
        {
            var filePath = getFilePathFunc.Invoke();
            return File.ReadAllLines(filePath);
        }
    }
}
