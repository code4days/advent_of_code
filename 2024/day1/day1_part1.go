package main

import (
  "fmt"
  s "strings"
  "strconv"
  "slices"
  "os"
  "bufio"
)

func check(e error) {
	if e != nil {
          panic(e)
	}
}
func main() {

	useTestInput := false
	var input string
	if useTestInput {
	    input = `3   4
	    4   3
	    2   5
	    1   3
	    3   9
	    3   3`
	} else {

	    file, err := os.Open("input_day1_part1.txt")
	    check(err)
	    defer file.Close()

	    var sb s.Builder
	    scanner := bufio.NewScanner(file)
	    for scanner.Scan() {
	    	sb.WriteString(scanner.Text() + "\n")
	    }
	    check(scanner.Err())
	    input = sb.String()
	}

	var left_list, right_list []int

	// fmt.Println("Input: ", s.Split(input, "\n"))
	lines := s.Split(s.TrimSpace(input), "\n")
	for _, line := range lines {
		parts := s.Fields(line)
		num1, err1 := strconv.Atoi(parts[0])
		check(err1)
		left_list = append(left_list, num1)
		num2, err2 := strconv.Atoi(parts[1])
		check(err2)
		right_list = append(right_list, num2)
	}
        // fmt.Println("Left list: ", left_list)
        // fmt.Println("Right list: ", right_list)

	slices.Sort(left_list)
	slices.Sort(right_list)

        // fmt.Println("Left list sorted: ", left_list)
        // fmt.Println("Right list sorted: ", right_list)

	var total int
	for i := 0; i < len(left_list); i++ {
		diff := right_list[i] - left_list[i]
		if diff < 0 {
	          diff = -diff
		}
		total += diff
	}

	fmt.Println("Total:", total)
}
