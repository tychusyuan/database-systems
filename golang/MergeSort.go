package main

import (
	"fmt"
)

func mergeSort(array []int) []int {
	l := len(array)
	if l < 2 {
		return array
	}
	mid := l / 2
	return merge(mergeSort(array[:mid]), mergeSort(array[mid:]))
}

func merge(left, right []int) []int {
	final := []int{}
	i := 0
	j := 0
	l := len(left)
	r := len(right)
	for i < l && j < r {
		if left[i] < right[j] {
			final = append(final, left[i])
			i++
		} else {
			final = append(final, right[j])
			j++
		}
	}

	for i < l {
		final = append(final, left[i])
		i++
	}
	for j < r {
		final = append(final, right[j])
		j++
	}
	return final
}

func main() {
	data := []int{3, 5, 3, 0, 8, 6, 1, 5, 8, 6, 2, 4, 9, 4, 7, 0, 1, 8, 9, 7, 3, 1, 2, 5, 9, 7, 4, 0, 2, 6}
	fmt.Println(data)
	result := mergeSort(data)
	fmt.Println(result)
}
