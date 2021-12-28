namespace AdventOfCode2021
{
    public static class Extensions
    {
        public static int ToInt(this char c)
        {
            if (c < '0' || '9' < c) {
                throw new ArgumentOutOfRangeException(nameof(c));
            }
            return (int)c - '0';
        }
    }
}
