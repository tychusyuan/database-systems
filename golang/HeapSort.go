package main

import "fmt"

func heapSort(tree []int) {
	l := len(tree)
	last_node := l - 1
	parent := (last_node - 1) / 2
	for i := parent; i > -1; i-- {
		heap(tree, i, last_node)
	}

	for i := last_node; i > 0; i-- {
		tree[i], tree[0] = tree[0], tree[i]
		heap(tree, 0, i-1)
	}
}

func heap(tree []int, i, end int) {
	l_node := 2*i + 1
	if l_node > end {
		return
	}
	max := l_node
	r_node := 2*i + 2
	if r_node <= end && tree[r_node] > tree[l_node] {
		max = r_node
	}
	if tree[i] > tree[max] {
		return
	}
	tree[max], tree[i] = tree[i], tree[max]
	heap(tree, max, end)
}

func main() {
	data := []int{3, 5, 3, 0, 8, 6, 1, 5, 8, 6, 2, 4, 9, 4, 7, 0, 1, 8, 9, 7, 3, 1, 2, 5, 9, 7, 4, 0, 2, 6}
	fmt.Println(data)
	heapSort(data)
	fmt.Println(data)
}
