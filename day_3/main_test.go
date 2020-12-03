package main

import (
	"testing"
)

func TestCountTrees(t *testing.T) {
	treemap := []string{
		"..##.......",
		"#...#...#..",
		".#....#..#.",
		"..#.#...#.#",
		".#...##..#.",
		"..#.##.....",
		".#.#.#....#",
		".#........#",
		"#.##...#...",
		"#...##....#",
		".#..#...#.#",
	}
	var results []int
	expected_results := []int{7}
	results = append(results, countTrees(treemap, 0, 0, 3, 1)) // Part 1
	if results[0] != expected_results[0] {
		t.Errorf("Expected results: %d, got: %d", expected_results, results)
	}
}
