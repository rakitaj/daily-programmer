using FluentAssertions;
using NUnit.Framework;

namespace LeetCode.Tests
{
    public class ReverseVowelsTests
    {
        [SetUp]
        public void Setup()
        {
        }

        [Test]
        public void TestReverseVowels()
        {
            var reverseVowels = new ReverseVowels();
            string result = reverseVowels.Solve("hello");
            result.Should().Be("holle");
        }

        [Test]
        public void TestReverseVowels2()
        {
            var reverseVowels = new ReverseVowels();
            string result = reverseVowels.Solve("leetcode");
            result.Should().Be("leotcede");
        }
    }
}