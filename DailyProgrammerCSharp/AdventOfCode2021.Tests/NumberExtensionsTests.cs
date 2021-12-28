using System;
using FluentAssertions;
using NUnit.Framework;

namespace AdventOfCode2021.Tests
{
    internal class NumberExtensionsTests
    {
        [TestCase('1', 1)]
        [TestCase('0', 0)]
        [TestCase('9', 9)]
        public void TestCharToInt(char c, int expected)
        {
            c.ToInt().Should().Be(expected);
        }

        [TestCase('a')]
        [TestCase('A')]
        [TestCase('$')]
        public void TestCharToIntShouldThrow(char c)
        {
            c.Invoking(x => x.ToInt()).Should().Throw<ArgumentOutOfRangeException>();
        }
    }
}
