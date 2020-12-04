package main

import (
	"fmt"
	"time"
)

func main() {
	passports := ReadPassports("input.txt")

	start := time.Now()
	validPassports := 0
	for _, p := range passports {
		if p.byr != "" &&
			p.ecl != "" &&
			p.eyr != "" &&
			p.hcl != "" &&
			p.hgt != "" &&
			p.iyr != "" &&
			p.pid != "" {
			validPassports++
		}
	}
	elapsed := time.Since(start)
	fmt.Printf("Part 1: found %d valid passports from a total of %d passports in %s\n", validPassports, len(passports), elapsed)

	start = time.Now()
	validPassports = 0
	for _, p := range passports {
		if p.IsValid() == true {
			validPassports++
		}
	}
	elapsed = time.Since(start)
	fmt.Printf("Part 2: found %d valid passports from a total of %d passports in %s", validPassports, len(passports), elapsed)
}
