package main

import (
	"errors"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

var input_folderpath string
var input_filename string

func main() {

	fmt.Print("Enter where you want your folders to be created: ")
	fmt.Scanln(&input_folderpath)
	fmt.Print("Enter the filename you desired: ")
	fmt.Scanln(&input_filename)

	folderpath := input_folderpath

	filename := strings.Split(input_filename, ",")

	for list_next := 0; list_next < len(filename); list_next++ {
		createfolder := folderpath + filename[list_next]
		if _, err := os.Stat(createfolder); errors.Is(err, os.ErrNotExist) {
			err := os.Mkdir(createfolder, os.ModePerm)
			if err != nil {
				log.Println(err)
			}
		}
		fmt.Println("Program: " + filename[list_next] + " created suscessfully")
	}
	fmt.Println("Program: " + strconv.Itoa(len(filename)) + " folders created suscessfully")
}
