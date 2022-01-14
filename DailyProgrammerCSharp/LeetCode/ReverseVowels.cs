using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Runtime.CompilerServices;
using System.Text;

namespace LeetCode
{
    public class ReverseVowels
    {
        public readonly HashSet<char> Vowels = new HashSet<char>() { 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U' };

        public string Solve(string s)
        {
            StringBuilder result = new StringBuilder();
            Stack<char> stack = new Stack<char>();
            foreach(char ch in s) {
                if (this.Vowels.Contains(ch)) {
                    stack.Push(ch);
                }
            }
            foreach (char ch in s) {
                if (this.Vowels.Contains(ch)) {
                    var c = stack.Pop();
                    result.Append(c);
                } else {
                    result.Append(ch);
                }
            }
            return result.ToString();
        }
    }
}
