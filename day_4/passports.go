package main

import (
	"bufio"
	"math"
	"os"
	"regexp"
	"strconv"
	"strings"
)

// Passport data
type Passport struct {
	byr string // Birth year
	cid string // County ID
	ecl string // Eye color
	eyr string // Expiration year
	hcl string // Hair color
	hgt string // Height
	iyr string // Issue year
	pid string // Passport ID
}

// Create new Passport
func (p *Passport) Create(raw string) {
	src := strings.Split(raw, " ")
	for _, pair := range src {
		v := strings.Split(pair, ":")
		switch v[0] {
		case "byr":
			p.byr = v[1]
		case "cid":
			p.cid = v[1]
		case "ecl":
			p.ecl = v[1]
		case "eyr":
			p.eyr = v[1]
		case "hcl":
			p.hcl = v[1]
		case "hgt":
			p.hgt = v[1]
		case "iyr":
			p.iyr = v[1]
		case "pid":
			p.pid = v[1]
		}
	}
}

// ValidateYear where year must be between 'min' and 'max'
func ValidateYear(s string, min int, max int) bool {
	var re = regexp.MustCompile(`^[0-9]{4}$`)
	if re.MatchString(s) {
		val, _ := strconv.Atoi(s)
		if val >= min && val <= max {
			return true
		}
	}
	return false
}

// ValidateHeight where height between 'min' and 'max',
// with automatic inches-to-centimeters conversion
func ValidateHeight(s string, min int, max int) bool {
	re := regexp.MustCompile(`^[0-9]{2,3}(cm|in)$`)
	if re.MatchString(s) {
		unit := s[len(s)-2 : len(s)]
		val, _ := strconv.ParseFloat(s[:len(s)-2], 32)
		if unit == "in" {
			val = 2.54 * val
		}

		height := int(math.Round(val))
		if height >= min && height <= max {
			return true
		}
	}
	return false
}

// ValidateHairColor for hexadecimal color code pattern
func ValidateHairColor(s string) bool {
	re := regexp.MustCompile(`^#[0-9a-f]{6}$`)
	return re.MatchString(s)
}

// ValidateEyeColor for presence of 3-letter predefined color codes
func ValidateEyeColor(s string) bool {
	re := regexp.MustCompile(`^(amb|blu|brn|gry|grn|hzl|oth)$`)
	return re.MatchString(s)
}

// ValidatePassportID for a numerical 9-digit pattern
func ValidatePassportID(s string) bool {
	re := regexp.MustCompile(`^[0-9]{9}$`)
	return re.MatchString(s)
}

// IsValid invokes all field-level validations
func (p *Passport) IsValid() bool {
	if ValidateYear(p.byr, 1920, 2002) == false {
		return false
	}
	if ValidateYear(p.iyr, 2010, 2020) == false {
		return false
	}
	if ValidateYear(p.eyr, 2020, 2030) == false {
		return false
	}
	if ValidateHeight(p.hgt, 150, 193) == false {
		return false
	}
	if ValidateHairColor(p.hcl) == false {
		return false
	}
	if ValidateEyeColor(p.ecl) == false {
		return false
	}
	if ValidatePassportID(p.pid) == false {
		return false
	}
	return true
}

// ReadPassports from given filename
func ReadPassports(filename string) []Passport {
	file, _ := os.Open(filename)
	defer file.Close()
	scanner := bufio.NewScanner(file)
	var raw string
	for scanner.Scan() {
		line := scanner.Text()
		if len(line) == 0 {
			raw = raw + ","
		} else {
			raw = raw + " " + line
		}
	}

	var passports []Passport
	for _, val := range strings.Split(raw, ",") {
		var p Passport
		p.Create(val)
		passports = append(passports, p)
	}
	return passports
}
