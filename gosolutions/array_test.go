package gosolutions

import (
	"testing"
)

func TestIncrementByOne(t *testing.T) {
	digits := []int{1, 2, 3}
	result := plusOne(digits)
	if !sliceEquality(result, []int{1, 2, 4}) {
		t.Fatalf("Test failed")
	}
}
