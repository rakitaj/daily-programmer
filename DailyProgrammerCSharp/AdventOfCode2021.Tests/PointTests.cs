using FluentAssertions;
using NUnit.Framework;

namespace AdventOfCode2021.Tests
{
    internal class PointTests
    {
        [Test]
        public void PointsWithTheSameCoordinatesShouldBeEqual()
        {
            var p1 = new Point(42, 42);
            var p2 = new Point(42, 42);
            p1.Should().Be(p2);
        }

        [Test]
        public void PointsWithDifferentCoordinatesShouldNotBeEqual()
        {
            var p1 = new Point(0, 12);
            var p2 = new Point(12, 0);
            p1.Should().NotBe(p2);
        }

        [Test]
        public void PointsWithTheSameCoordinatesShouldHaveTheSameHashCode()
        {
            Point p1 = new Point(1, 1);
            Point p2 = new Point(2, 2);
            p1.GetHashCode().Should().Be(p2.GetHashCode());
        }

        [Test]
        public void PointsWithDifferentCoordinatesCanHaveTheSameHashCodeAndShouldNotBeEqual()
        {
            Point p1 = new Point(1, 1);
            Point p2 = new Point(2, 2);
            p1.GetHashCode().Should().Be(p2.GetHashCode());
            p1.Should().NotBe(p2);
        }

        [Test]
        public void PointEqualsNullShouldBeFalse()
        {
            Point p1 = new Point(2, 3);
            p1.Equals(null).Should().BeFalse();
        }
    }
}
