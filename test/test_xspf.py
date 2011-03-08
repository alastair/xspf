import unittest
import os
import sys
sys.path.append(os.path.abspath(".."))
import xspf

class XspfTest(unittest.TestCase):
    def testBySpiff(self):
        x = xspf.Spiff()
        self.assertTrue(isinstance(x, xspf.Xspf))
        # self.assertEqual(sort.sorted_list(start), expected)

    def testEmptyPlaylist(self):
        x = xspf.Xspf()
        expected = """<ns0:playlist version="1" xmlns:ns0="http://xspf.org/ns/0/" />"""
        self.assertEqual(expected, x.toXml())

    def testTitle(self):
        x = xspf.Xspf()
        x.title = "title"
        expected = """<ns0:playlist version="1" xmlns:ns0="http://xspf.org/ns/0/"><ns0:title>title</ns0:title></ns0:playlist>"""
        self.assertEqual(expected, x.toXml())

    def testCreator(self):
        x = xspf.Xspf()
        x.creator = "creator"
        expected = """<ns0:playlist version="1" xmlns:ns0="http://xspf.org/ns/0/"><ns0:creator>creator</ns0:creator></ns0:playlist>"""
        self.assertEqual(expected, x.toXml())

    def testAnnotation(self):
        x = xspf.Xspf()
        x.annotation = "ann"
        expected = """<ns0:playlist version="1" xmlns:ns0="http://xspf.org/ns/0/"><ns0:annotation>ann</ns0:annotation></ns0:playlist>"""
        self.assertEqual(expected, x.toXml())

    def testInfo(self):
        x = xspf.Xspf()
        x.info = "info"
        expected = """<ns0:playlist version="1" xmlns:ns0="http://xspf.org/ns/0/"><ns0:info>info</ns0:info></ns0:playlist>"""
        self.assertEqual(expected, x.toXml())

    def testLocation(self):
        x = xspf.Xspf()
        x.location = "loc"
        expected = """<ns0:playlist version="1" xmlns:ns0="http://xspf.org/ns/0/"><ns0:location>loc</ns0:location></ns0:playlist>"""
        self.assertEqual(expected, x.toXml())

    def testIdentifier(self):
        x = xspf.Xspf()
        x.identifier = "id"
        expected = """<ns0:playlist version="1" xmlns:ns0="http://xspf.org/ns/0/"><ns0:identifier>id</ns0:identifier></ns0:playlist>"""
        self.assertEqual(expected, x.toXml())

    def testImage(self):
        x = xspf.Xspf()
        x.image = "image"
        expected = """<ns0:playlist version="1" xmlns:ns0="http://xspf.org/ns/0/"><ns0:image>image</ns0:image></ns0:playlist>"""
        self.assertEqual(expected, x.toXml())

    def testDate(self):
        x = xspf.Xspf()
        x.date = "date"
        expected = """<ns0:playlist version="1" xmlns:ns0="http://xspf.org/ns/0/"><ns0:date>date</ns0:date></ns0:playlist>"""
        self.assertEqual(expected, x.toXml())

    def testLicense(self):
        x = xspf.Xspf()
        x.license = "CC BY-SA"
        expected = """<ns0:playlist version="1" xmlns:ns0="http://xspf.org/ns/0/"><ns0:license>CC BY-SA</ns0:license></ns0:playlist>"""
        self.assertEqual(expected, x.toXml())

    def testKwargs(self):
        """ Test that all attribute names as kwargs works"""
        x = xspf.Xspf(title="my title"
                    , creator="creator"
                    , info="info"
                    , annotation="ann"
                    , location="location"
                    , identifier="id"
                    , image="image"
                    , date="date"
                    , license="license")

        self.assertEqual("my title", x.title)
        self.assertEqual("creator", x.creator)
        self.assertEqual("info", x.info)
        self.assertEqual("ann", x.annotation)
        self.assertEqual("location", x.location)
        self.assertEqual("id", x.identifier)
        self.assertEqual("image", x.image)
        self.assertEqual("date", x.date)
        self.assertEqual("license", x.license)

    def testDict(self):
        """ Test that attributes as a dictionary works """
        x = xspf.Xspf({"title": "atitle", "creator": "alastair"})
        self.assertEqual("atitle", x.title)
        self.assertEqual("alastair", x.creator)

    def testXspfParser(self):
        """ Test that a JSPF-like dict works """
        parse = {"playlist": {"title": "atitle"}}
        x = xspf.Xspf(parse)
        self.assertEqual("atitle", x.title)

