package main

import (
	"testing"
)

// TestPassportReader for part 1
func TestPassportReader(t *testing.T) {
	passports := ReadPassports("input_test.txt")
	if len(passports) != 4 {
		t.Errorf("Expected total passports: %d, got: %d", 4, len(passports))
	}

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
	if validPassports != 2 {
		t.Errorf("Expected valid passports: %d, got: %d", 2, validPassports)
	}
}

// TestPassportsCombinedValidations for part 2
func TestPassportCombinedValidations(t *testing.T) {
	expectedValidPassports := 4
	passports := ReadPassports("input_test_2.txt")
	if len(passports) != 8 {
		t.Errorf("Expected total passports: %d, got: %d", 8, len(passports))
	}

	validPassports := 0
	for _, p := range passports {
		if p.IsValid() == true {
			validPassports++
		}
	}

	if validPassports != expectedValidPassports {
		t.Errorf("Expected valid passports: %d, got: %d", expectedValidPassports, validPassports)
	}
}
