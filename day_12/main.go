package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)

type Action struct {
	typ string // Action type: N, S, E, W, L, R, F
	val int    // Action value
}

type Waypoint struct {
	x int // Position shifting on east-west axis
	y int // Position shifting on north-south axis
}

type Vessel struct {
	x   int      // Position shifting on east-west axis
	y   int      // Position shifting on north-south axis
	wp  Waypoint // Active waypoint
	deg int      // Set drive direction in degrees, with north being 0° (Part 1)
}

func (v *Vessel) move(a Action) {
	v.x = v.x + v.wp.x*a.val
	v.y = v.y + v.wp.y*a.val
}

// directDrive for executin instructions directly (Part 1)
func (v *Vessel) directDrive(a *[]Action) {
	for _, a := range *a {
		switch a.typ {
		case "N":
			v.y = v.y + a.val
		case "S":
			v.y = v.y - a.val
		case "E":
			v.x = v.x + a.val
		case "W":
			v.x = v.x - a.val
		case "L":
			v.deg = v.deg - a.val
			if v.deg < 0 {
				v.deg = 360 - abs(v.deg)
			}
		case "R":
			v.deg = v.deg + a.val
			if v.deg >= 360 {
				v.deg = v.deg % 360
			}
		case "F":
			if v.deg == 0 {
				v.y = v.y + a.val
			} else if v.deg == 90 {
				v.x = v.x + a.val
			} else if v.deg == 180 {
				v.y = v.y - a.val
			} else if v.deg == 270 {
				v.x = v.x - a.val
			}
		}
	}
}

// set waypoint relative to the given vessel's x and y positions (Part 2)
func (wp *Waypoint) set(a Action) {
	switch a.typ {
	case "N":
		wp.y = wp.y + a.val
	case "S":
		wp.y = wp.y - a.val
	case "E":
		wp.x = wp.x + a.val
	case "W":
		wp.x = wp.x - a.val
	case "L":
		// Refactored and adapted this much leaner L/R switching logic by 'j4rv':
		// https://github.com/j4rv/advent-of-code-2020/blob/main/day-12/main.go#L90
		a.val = mod(-a.val, 360)
		fallthrough
	case "R":
		switch a.val {
		case 90:
			wp.x, wp.y = +wp.y, -wp.x
		case 180:
			wp.x, wp.y = -wp.x, -wp.y
		case 270:
			wp.x, wp.y = -wp.y, wp.x
		}
	}
}

func (v *Vessel) execute(actions *[]Action) {
	for _, a := range *actions {
		if a.typ == "F" {
			v.move(a)
		} else {
			v.wp.set(a)
		}
	}
}

func readActions(filename string) []Action {
	f, _ := os.Open(filename)
	defer f.Close()
	scanner := bufio.NewScanner(f)
	var actions []Action
	for scanner.Scan() {
		line := scanner.Text()
		val, _ := strconv.Atoi(string(line[1:]))
		actions = append(actions, Action{
			typ: string(line[0]),
			val: val,
		})
	}
	return actions
}

func abs(val int) int {
	return int(math.Abs(float64(val)))
}

func mod(val, m int) int {
	val = val % m
	if val < 0 {
		val = m + val
	}
	return val
}

func main() {
	actions := readActions("input.txt")
	vesselPart1 := Vessel{
		y:   0,
		x:   0,
		wp:  Waypoint{},
		deg: 90,
	}
	vesselPart1.directDrive(&actions)
	manhattanPart1 := abs(vesselPart1.y) + abs(vesselPart1.x)
	fmt.Println("Part 1: manhattan distance: ", manhattanPart1)
	vesselPart2 := Vessel{
		x: 0,
		y: 0,
		wp: Waypoint{
			x: 10,
			y: 1,
		},
	}
	vesselPart2.execute(&actions)
	manhattanPart2 := abs(vesselPart2.y) + abs(vesselPart2.x)
	fmt.Println("Part 2: manhattan distance: ", manhattanPart2)
}
