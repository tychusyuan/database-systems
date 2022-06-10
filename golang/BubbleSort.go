package main

import (
	"fmt"
)

func bubbleSort(array []int) {
	l := len(array)
	for i := 0; i < l; i++ {
		for j := 0; j < l-i-1; j++ {
			if array[j] > array[j+1] {
				array[j], array[j+1] = array[j+1], array[j]
			}
		}
	}
}

func main() {
	data := []int{3, 5, 3, 0, 8, 6, 1, 5, 8, 6, 2, 4, 9, 4, 7, 0, 1, 8, 9, 7, 3, 1, 2, 5, 9, 7, 4, 0, 2, 6}
	fmt.Println(data)
	bubbleSort(data)
	fmt.Println(data)
}
