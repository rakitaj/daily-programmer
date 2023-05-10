package gosolutions

func sliceEquality[T comparable](slice1 []T, slice2 []T) bool {
	if len(slice1) != len(slice2) {
		return false
	} else {
		for i := range slice1 {
			if slice1[i] != slice2[i] {
				return false
			}
		}
	}
	return true
}
