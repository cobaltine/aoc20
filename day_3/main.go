package main

import (
	"fmt"
	"io"
	"os"
	"time"
)

func readMap() []string {
	file, _ := os.Open("input.txt")
	var line string
	var lines []string
	for {
		if _, err := fmt.Fscanf(file, "%s\n", &line); err == io.EOF {
			break
		}
		lines = append(lines, line)
	}
	return lines
}

func extendLine(line string, x int) string {
	for {
		if len(line)/x > 1 {
			break
		}
		line = line + line
	}
	return line
}

func countTrees(treemap []string, x int, y int, stepX int, stepY int) int {
	trees := 0
	for lat, line := range treemap {
		if lat > 0 && lat%stepY == 0 {
			x += stepX
			y += stepY
			line = extendLine(line, x)
			if y <= lat && string(line[x]) == "#" {
				trees += 1
			}
		}
	}
	return trees
}

func main() {
	treemap := readMap()
	var results []int
	start := time.Now()
	results = append(results, countTrees(treemap, 0, 0, 1, 1))
	results = append(results, countTrees(treemap, 0, 0, 3, 1)) // Part 1
	results = append(results, countTrees(treemap, 0, 0, 5, 1))
	results = append(results, countTrees(treemap, 0, 0, 7, 1))
	results = append(results, countTrees(treemap, 0, 0, 1, 2))
	elapsed := time.Since(start)
	fmt.Printf("Found a set of trees, %d, with given x-y steps in %s\n", results, elapsed)
}
