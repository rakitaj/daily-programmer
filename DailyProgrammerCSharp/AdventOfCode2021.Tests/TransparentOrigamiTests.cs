using System.Collections.Generic;
using System.IO;
using System.Linq;
using NUnit.Framework;

namespace AdventOfCode2021.Tests
{
    internal class TransparentOrigamiTests
    {
        public static string GetTestDataFilePath(int dayNumber, int testCaseID)
        {
            var dayWithLeadingZeros = dayNumber.ToString("D2");
            string filePath = Path.Join("Data", $"day{dayWithLeadingZeros}-{testCaseID}.txt");
            return filePath;
        }

        public static IList<string> ReadTestData(int testCaseNumber)
        {
            List<string> data = PuzzleInput.ToArrayOfStrings(() => GetTestDataFilePath(13, 1)).ToList();
            return data;
        }

        [TestCase]
        public void TestReadingWithFunc()
        {
            var result = ReadTestData(13);
        }
    }
}
