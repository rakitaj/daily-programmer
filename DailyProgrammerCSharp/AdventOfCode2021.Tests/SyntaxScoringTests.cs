using System.Collections;
using System.Collections.Generic;
using FluentAssertions;
using NUnit.Framework;

namespace AdventOfCode2021.Tests
{
    internal class SyntaxScoringTests
    {
        [TestCase("{([(<{}[<>[]}>{[]{[(<()>", '}')]
        [TestCase("[[<[([]))<([[{}[[()]]]", ')')]
        [TestCase("[{[{({}]{}}([{[{{{}}([]", ']')]
        [TestCase("[<(<(<(<{}))><([]([]()", ')')]
        [TestCase("<{([([[(<>()){}]>(<<{{", '>')]
        public void TestSyntaxParser(string puzzleLine, char expected)
        {
            var actual = SyntaxScoring.SyntaxParser(puzzleLine);
            actual.Should().Be(expected);
        }

        [TestCase("[({(<(())[]>[[{[]{<()<>>", "}}]])})]")]
        [TestCase("[(()[<>])]({[<{<<[]>>(", ")}>]})")]
        [TestCase("(((({<>}<{<{<>}{[]{[]{}", "}}>}>))))")]
        [TestCase("{<[[]]>}<{[{[{[]{()[[[]", "]]}}]}]}>")]
        [TestCase("<{([{{}}[<[[[<>{}]]]>[]]", "])}>")]
        public void TestSyntaxAutocomplete(string puzzleLine, string expected)
        {
            var actual = SyntaxScoring.SyntaxAutocomplete(puzzleLine);
            var expectedAsCharList = expected.ToCharArray();
            actual.Should().Equal(expectedAsCharList);
        }

        [TestCase("])}>", 294)]
        public void TestSyntaxAutocompleteScope(string characters, long expected)
        {
            long score = SyntaxScoring.SyntaxAutocompleteScore(characters.ToCharArray());
            score.Should().Be(expected);
        }

        [TestCase("[({(<(())[]>[[{[]{<()<>>", 288957)]
        [TestCase("[(()[<>])]({[<{<<[]>>(", 5566)]
        [TestCase("(((({<>}<{<{<>}{[]{[]{}", 1480781)]
        [TestCase("{<[[]]>}<{[{[{[]{()[[[]", 995444)]
        [TestCase("<{([{{}}[<[[[<>{}]]]>[]]", 294)]
        public void TestSyntaxAutocompleteAndScore(string puzzleLine, long expected)
        {
            var charactersToScore = SyntaxScoring.SyntaxAutocomplete(puzzleLine);
            var score = SyntaxScoring.SyntaxAutocompleteScore(charactersToScore);
            score.Should().Be(expected);
        }

        [Test]
        public void TestSyntaxScoreMidpoint()
        {
            var inputStrings = new List<string>() {
                "[({(<(())[]>[[{[]{<()<>>",
                "[(()[<>])]({[<{<<[]>>(",
                "(((({<>}<{<{<>}{[]{[]{}",
                "{<[[]]>}<{[{[{[]{()[[[]",
                "<{([{{}}[<[[[<>{}]]]>[]]"};
            var actual = SyntaxScoring.SyntaxScoring2(inputStrings);
            actual.Should().Be(288957);
        }
    }
}
