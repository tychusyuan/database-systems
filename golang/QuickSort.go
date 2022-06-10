package main

import "fmt"

func quickSort(array []int, left, right int) {
	if left < right {
		//idx := partition(array, left, right)
		idx := partition2(array, left, right)
		quickSort(array, left, idx-1)
		quickSort(array, idx+1, right)
	}
}

func partition(array []int, left, right int) int {
	pivot := right
	i := left

	for j := left; j < right; j++ {
		if array[j] < array[pivot] {
			array[i], array[j] = array[j], array[i]
			i++
		}
	}
	array[i], array[pivot] = array[pivot], array[i]
	return i
}

func partition2(array []int, left, right int) int {
	pivot := right
	i := left
	j := right

	for i < j {
		for i < j && array[i] <= array[pivot] {
			i++
		}
		for i < j && array[j] >= array[pivot] {
			j--
		}
		array[i], array[j] = array[j], array[i]
	}

	array[i], array[pivot] = array[pivot], array[i]
	return i
}

func main() {
	data := []int{3, 5, 3, 0, 8, 6, 1, 5, 8, 6, 2, 4, 9, 4, 7, 0, 1, 8, 9, 7, 3, 1, 2, 5, 9, 7, 4, 0, 2, 6}
	fmt.Println(data)
	quickSort(data, 0, len(data)-1)
	fmt.Println(data)
}
