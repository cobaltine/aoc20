package main

import (
	"testing"
)

func TestPart1(t *testing.T) {
	expected := 25
	actions := readActions("input_test.txt")
	vessel := Vessel{
		y:   0,
		x:   0,
		wp:  Waypoint{},
		deg: 90,
	}
	vessel.directDrive(&actions)
	manhattanDist := (abs(vessel.x) + abs(vessel.y))
	if manhattanDist != expected {
		t.Errorf("Expected manhattan distance: %d, got: %d", expected, manhattanDist)
	}
}

func TestPart2(t *testing.T) {
	expected := 286
	actions := readActions("input_test.txt")
	vessel := Vessel{
		y: 0,
		x: 0,
		wp: Waypoint{
			x: 10,
			y: 1,
		},
	}
	vessel.execute(&actions)
	manhattanDist := (abs(vessel.x) + abs(vessel.y))
	if manhattanDist != expected {
		t.Errorf("Expected manhattan distance: %d, got: %d", expected, manhattanDist)
	}
}
