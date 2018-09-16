#Ran Bi

import unittest
import media as proj1

##Part 1: Implement and test a class system
class TestMediaMovieSong(unittest.TestCase):
    #test all class constructors work as specified
    def testConstructor(self):
        m0 = proj1.Media()
        m1 = proj1.Media("1999", "Prince", "1982")
        m2 = proj1.Song("Undo", "Sanna Nielsen", "2014" ,"No Album","Pop",190000)
        m3 = proj1.Movie("Inception","Christopher Nolan","2010","PG",8880000)
        self.assertEqual(m0.title, "No Title")
        self.assertEqual(m0.author, "No Author")
        self.assertEqual(m1.title, "1999")
        self.assertEqual(m1.author, "Prince")
        self.assertEqual(m1.releaseyear, "1982")
        self.assertEqual(m2.title, "Undo")
        self.assertEqual(m2.author, "Sanna Nielsen")
        self.assertEqual(m2.releaseyear, "2014")
        self.assertEqual(m2.genre, "Pop")
        self.assertEqual(m2.tracklength, 190000)
        self.assertEqual(m3.title, "Inception")
        self.assertEqual(m3.author, "Christopher Nolan")
        self.assertEqual(m3.releaseyear, "2010")
        self.assertEqual(m3.rating, "PG")
        self.assertEqual(m3.movielength, 8880000)
    #test __str__ works properly for all three classes
    def test__str__(self):
        m1 = proj1.Media("1999", "Prince", "1982")
        m2 = proj1.Song("Undo", "Sanna Nielsen", "2014" ,"No Album","Pop",190000)
        m3 = proj1.Movie("Inception","Christopher Nolan","2010","PG",8880000)
        self.assertEqual(m1.__str__(), "1999 by Prince (1982)")
        self.assertEqual(m2.__str__(), "Undo by Sanna Nielsen (2014) [Pop]")
        self.assertEqual(m3.__str__(), "Inception by Christopher Nolan (2010) [PG]")
    #test __len__ works properly for all three classes
    def test__len__(self):
        m1 = proj1.Media("1999", "Prince", "1982")
        m2 = proj1.Song("Undo", "Sanna Nielsen", "2014" ,"No Album","Pop",190000)
        m3 = proj1.Movie("Inception","Christopher Nolan","2010","PG",8880000)
        self.assertEqual(m1.__len__(), 0)
        self.assertEqual(m2.__len__(), 190)
        self.assertEqual(m3.__len__(), 148)
    #test classes do not have instance variables that are not relevant to them
    def testInstanceNotRelevant(self):
        m1 = proj1.Media("1999", "Prince", "1982")
        m2 = proj1.Song("Undo", "Sanna Nielsen", "2014" ,"No Album","Pop",190000)
        m3 = proj1.Movie("Inception","Christopher Nolan","2010","PG",8880000)
        self.assertFalse('rating' in dir(m1))  #Media does not have 'rating' instance variable
        self.assertFalse('movielength' in dir(m1))  #Media does not have 'movie length' instance variable
        self.assertFalse('tracklength' in dir(m1))  #Media does not have 'track length' instance variable
        self.assertFalse('rating' in dir(m2))  #Song does not have 'rating' instance variable
        self.assertFalse('movielength' in dir(m2))  #Song does not have 'movie length' instance variable
        self.assertFalse('tracklength' in dir(m3))  #Movie does not have 'track length' instance variable
        self.assertFalse('genre' in dir(m3))  #Movie does not have 'genre' instance variable
        self.assertFalse('album' in dir(m3))  #Movie does not have 'album' instance variable

##Part 2: Test objects created from JSON
class TestObjectsFromJson(unittest.TestCase):
    def testMedia_Json(self):
        m = proj1.creat_object_from_json('sample_json.json')
        m1 = m[2]
        self.assertEqual(m1.title, "Bridget Jones's Diary (Unabridged)")
        self.assertEqual(m1.author, "Helen Fielding")
        self.assertEqual(m1.releaseyear, "2012")
        self.assertEqual(m1.__str__(), "Bridget Jones's Diary (Unabridged) by Helen Fielding (2012)")
        self.assertEqual(m1.__len__(), 0)
        self.assertFalse('rating' in dir(m1))
    def testSong_Json(self):
        m = proj1.creat_object_from_json('sample_json.json')
        m2 = m[1]
        self.assertEqual(m2.title, "Hey Jude")
        self.assertEqual(m2.author, "The Beatles")
        self.assertEqual(m2.genre, "Rock")
        self.assertEqual(m2.__str__(), "Hey Jude by The Beatles (1968) [Rock]")
        self.assertEqual(m2.__len__(), 431)
        self.assertFalse('rating' in dir(m2))
    def testMovie_Json(self):
        m = proj1.creat_object_from_json('sample_json.json')
        m3 = m[0]
        self.assertEqual(m3.title, "Jaws")
        self.assertEqual(m3.author, "Steven Spielberg")
        self.assertEqual(m3.rating, "PG")
        self.assertEqual(m3.__str__(), "Jaws by Steven Spielberg (1975) [PG]")
        self.assertEqual(m3.__len__(), 124)

##Part 3: Test objects created from iTunes API
class TestObjectsFromApi(unittest.TestCase):
    def testExpectedRangeAndType(self):
        #query is baby with default 50 results
        base_url1 = "https://itunes.apple.com/search?term=baby"
        t1 = proj1.creat_object_from_api(base_url1)
        self.assertTrue(len(t1) >= 0 and len(t1) <= 50) #test within expected ranges
        self.assertTrue(all(isinstance(x,(proj1.Song,proj1.Media,proj1.Movie))for x in t1)) #test construct the correct type of object
        #query is moana
        base_url2 = "https://itunes.apple.com/search?term=moana"
        t2 = proj1.creat_object_from_api(base_url2)
        self.assertTrue(len(t2) >= 0 and len(t2) <= 50) #test within expected ranges
        self.assertTrue(all(isinstance(x,(proj1.Song,proj1.Media,proj1.Movie))for x in t2)) #test construct the correct type of object
        #qnonsense queries (“&@#!$”)
        base_url3 = "https://itunes.apple.com/search?term=&@#!$"
        t3 = proj1.creat_object_from_api(base_url3)
        self.assertEqual(len(t3), 0)    #expect an empty list
        #blank query
        base_url4 = "https://itunes.apple.com/search?term= "
        t4 = proj1.creat_object_from_api(base_url4)
        self.assertEqual(len(t4), 0)    #expect an empty list

unittest.main()
