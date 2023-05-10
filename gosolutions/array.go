package gosolutions

func plusOne(digits []int) []int {
	length := len(digits)
	digits[length-1] = digits[length-1] + 1
	return digits
}
