package main

import "fmt"

func quickSort(array []int) {

}

func partition(array []int, l, r int) int {
	p := r
	i := l
	j := p - 1

	for ; i < j; i++ {
		if array[i] > array[p] {
			for ; i < j; j++ {
				if array[j] < array[p] {
					array[i], array[j] = array[j], array[i]
				}
			}
		}
	}
}

func main() {
	data := []int{1, 7, 7, 9, 1, 8, 5, 0}
	fmt.Println(data)
	quickSort(data)
	fmt.Println(data)
}
