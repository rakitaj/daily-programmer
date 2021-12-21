using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdventOfCode2021
{
    public class SyntaxScoring
    {
        private static readonly Dictionary<char, char> _openingCharMap = new Dictionary<char, char>() { { '(', ')' }, { '[', ']' }, { '{', '}' }, { '<', '>' } };
        private static readonly Dictionary<char, char> _closingCharMap = new Dictionary<char, char>() { { ')', '(' }, { ']', '[' }, { '}', '{' }, { '>', '<' } };

        public static long SyntaxAutocompleteScore(IList<char> result)
        {
            var scoreMap = new Dictionary<char, int>() { { ')', 1 }, { ']', 2 }, { '}', 3 }, { '>', 4 } };
            long total = 0;
            foreach (char c in result) {
                total = total * 5;
                total += scoreMap[c];
            }
            return total;
        }

        public static char? SyntaxParser(string puzzleInputLine)
        {
            var stack = new Stack<char>();
            foreach (char c in puzzleInputLine) {
                if (_openingCharMap.ContainsKey(c)) {
                    stack.Push(c);
                }
                else if (stack.Peek() == _closingCharMap[c]) {
                    stack.Pop();
                }
                else {
                    return c;
                }
            }
            return null;
        }

        public static List<char> SyntaxAutocomplete(string puzzleInputLine)
        {
            var result = new List<char>();
            var stack = new Stack<char>();
            foreach (char c in puzzleInputLine) {
                if (_openingCharMap.ContainsKey(c)) {
                    stack.Push(c);
                }
                else if (stack.Peek() == _closingCharMap[c]) {
                    stack.Pop();
                }
            }
            foreach (char c in stack) {
                result.Add(_openingCharMap[c]);
            }
            return result;
        }

        public static long SyntaxScoring2(IList<string> puzzleInput)
        {
            var scores = new List<long>();
            foreach (var line in puzzleInput) {
                char? invalidChar = SyntaxScoring.SyntaxParser(line);
                if (invalidChar != null) {
                    continue;
                }
                var result = SyntaxScoring.SyntaxAutocomplete(line);
                var score = SyntaxScoring.SyntaxAutocompleteScore(result);
                scores.Add(score);
            }
            // Now find the middle score.
            scores.Sort();
            var middleIndex = scores.Count / 2;
            return scores[middleIndex];
        }
    }
}
