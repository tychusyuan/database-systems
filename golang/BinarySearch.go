package main

import (
	"fmt"
	"math"
)

func search(nums []int, target int) int {
	l := 0
	r := len(nums) - 1

	for l <= r {
		mid := (l + r) / 2
		if target < nums[mid] {
			r = mid - 1
		} else if target > nums[mid] {
			l = mid + 1
		} else {
			return mid
		}
	}
	return -1
}

func ()  {
	
}

func main() {
	nums := []int{-1, 0, 3, 5, 9, 12}
	target := 9
	fmt.Println(search(nums, target))
	target = 2
	fmt.Println(search(nums, target))
	target = 5
	fmt.Println(search(nums, target))

	math.Sqrt(9)
}
