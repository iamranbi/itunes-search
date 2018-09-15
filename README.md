# itunes-search
A simple command line tool for searching the iTunes store.

## Files
media.py: defines classes and functions
<br> media_test.py: defines test cases
<br> sample_json.txt: sample output from the iTunes web API

## Code Structure
1. implement a set of classes to model the iTunes data
<br> - Media (base class): instance variables: title, author, release year
<br> - Song (subclass of Media): additional instance variables: album, track length
<br> - Movie (subclass of Media): additional instance variables: rating, movie length
2. create objects from JSON
3. create objects from iTunes API
4. create an interactive search interface 
<br> - add the ability for users to enter their own queries and receive nicely formatted results


## User Guide
### run the test file (unit testing)
`$ python3 media_test.py`
### run the program
`$ python3 media.py`
### choose command line options
* **exit**
<br> - description: exits the program
<br> - sample command: `Enter a search term, or "exit" to quit: exit`
* **\<a search term>**
<br> - description: 
<br> - sample command: `Enter a search term, or "exit" to quit: Beatles`
