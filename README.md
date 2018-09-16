# iTunes Search
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
<br> - function: creat_object_from_json()
<br> - param: json file
<br> - return: a list of objects (Movie, Song, Media)
3. create objects from iTunes API
<br> - function: creat_object_from_api()
<br> - param: an url
<br> - return: a list of objects (Movie, Song, Media)
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
<br> - description: prints the results one per line and the results are grouped into Songs, Movies, and Other Media
<br> - sample command: `Enter a search term, or "exit" to quit: Beatles`
* **after a query has been run, a third option becomes available: \<the number of the result want to preview>**
<br> - description: uses the webbrowser module to open the trackViewURL, while also printing the URL to the screen
<br> - sample command: `Enter a number for more info, or another search term, or exit: 1`
