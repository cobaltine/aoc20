package main

import (
	"fmt"
	"io"
	"os"
	"time"
)

// Read numbers from a text file into a slice of ints
func readInput() []int {
	file, _ := os.Open("input.txt")
	var num int
	var nums []int
	for {
		if _, err := fmt.Fscanf(file, "%d\n", &num); err == io.EOF {
			break
		}
		nums = append(nums, num)
	}
	return nums
}

// Get a sum for numbers based on their indexes in the slice
func getSum(nums *[]int, indexes *[]int) int {
	sum := 0
	for _, i := range *indexes {
		sum += (*nums)[i]
	}
	return sum
}

// Recursive lookup for a set of numbers that match the target sum
func iterateNums(nums *[]int, depth int, maxDepth int, indexes []int, target int, results *[]int) {
	depth += 1
	for i, _ := range *nums {
		if len(*results) > 0 {
			break
		}
		indexes = append(indexes, i)
		if depth < maxDepth {
			iterateNums(nums, depth, maxDepth, indexes, target, results)
		} else if getSum(nums, &indexes) == target {
			for _, index := range indexes {
				*results = append(*results, (*nums)[index])
			}
			break
		}
		indexes = indexes[:len(indexes)-1]
	}
}

// Search for a target sum formed by a sum of an arbitrary set of numbers
func findSet(nums *[]int, set int, target int) {
	start := time.Now()
	var indexes []int
	var results []int
	iterateNums(nums, 0, set, indexes, target, &results)
	elapsed := time.Since(start)
	fmt.Printf("Found a set of %d numbers, %d, that sum up to %d in %s\n", set, results, target, elapsed)
}

func main() {
	nums := readInput()
	target := 2020
	findSet(&nums, 2, target)
	findSet(&nums, 3, target)
}
