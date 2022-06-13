package main

import "fmt"

func heapSort(tree []int) {
	l := len(tree)
	last_node := l - 1

	for i := last_node; i > 0; i-- {
		tree[i], tree[0] = tree[0], tree[i]
		heapify(tree, 0, i-1)
	}
}

func heapBuild(tree []int) {
	l := len(tree)
	last_node := l - 1
	parent := (last_node - 1) / 2
	for i := parent; i > -1; i-- {
		heapify(tree, i, last_node)
	}
}

func heapify(tree []int, i, end int) {
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
		// 在heap build阶段，因为是从最后一个parent向上 heapify，所以只要parent节点没有交换，就不用向下整理
		// 在heap sort 阶段，因为已经是基于堆再调整，所以只要parent 节点没有交换，就不用向下整理
		return
	}
	tree[max], tree[i] = tree[i], tree[max]
	heapify(tree, max, end)
}

func main() {
	data := []int{3, 5, 3, 0, 8, 6, 1, 5, 8, 6, 2, 4, 9, 4, 7, 0, 1, 8, 9, 7, 3, 1, 2, 5, 9, 7, 4, 0, 2, 6}
	fmt.Println(data)
	heapBuild(data)
	heapSort(data)
	fmt.Println(data)
}
