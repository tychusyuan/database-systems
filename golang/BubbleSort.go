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
	data := []int{1, 7, 7, 9, 1, 8, 5, 0}
	fmt.Println(data)
	bubbleSort(data)
	fmt.Println(data)
}
