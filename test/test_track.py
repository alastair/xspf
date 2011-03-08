import unittest
import os
import sys
sys.path.append(os.path.abspath(".."))
import xspf
import xml.etree.ElementTree as ET

class TrackTest(unittest.TestCase):
    def testLocation(self):
        root = ET.Element("{http://xspf.org/ns/0/}x")
        t = xspf.Track()
        t.location = "location"
        root = t.getXmlObject(root)
        expected = """<ns0:x xmlns:ns0="http://xspf.org/ns/0/"><ns0:track><ns0:location>location</ns0:location></ns0:track></ns0:x>"""
        xml = ET.tostring(root, "utf-8")
        self.assertEqual(expected, xml)

    def testIdentifier(self):
        root = ET.Element("{http://xspf.org/ns/0/}x")
        t = xspf.Track()
        t.identifier = "id"
        root = t.getXmlObject(root)
        expected = """<ns0:x xmlns:ns0="http://xspf.org/ns/0/"><ns0:track><ns0:identifier>id</ns0:identifier></ns0:track></ns0:x>"""
        xml = ET.tostring(root, "utf-8")
        self.assertEqual(expected, xml)

    def testTitle(self):
        root = ET.Element("{http://xspf.org/ns/0/}x")
        t = xspf.Track()
        t.title = "title"
        root = t.getXmlObject(root)
        expected = """<ns0:x xmlns:ns0="http://xspf.org/ns/0/"><ns0:track><ns0:title>title</ns0:title></ns0:track></ns0:x>"""
        xml = ET.tostring(root, "utf-8")
        self.assertEqual(expected, xml)

    def tesCreator(self):
        root = ET.Element("{http://xspf.org/ns/0/}x")
        t = xspf.Track()
        t.creator = "creator"
        root = t.getXmlObject(root)
        expected = """<ns0:x xmlns:ns0="http://xspf.org/ns/0/"><ns0:track><ns0:creator>creator</ns0:creator></ns0:track></ns0:x>"""
        xml = ET.tostring(root, "utf-8")
        self.assertEqual(expected, xml)

    def testAnnotation(self):
        root = ET.Element("{http://xspf.org/ns/0/}x")
        t = xspf.Track()
        t.annotation = "ann"
        root = t.getXmlObject(root)
        expected = """<ns0:x xmlns:ns0="http://xspf.org/ns/0/"><ns0:track><ns0:annotation>ann</ns0:annotation></ns0:track></ns0:x>"""
        xml = ET.tostring(root, "utf-8")
        self.assertEqual(expected, xml)

    def testInfo(self):
        root = ET.Element("{http://xspf.org/ns/0/}x")
        t = xspf.Track()
        t.info = "info"
        root = t.getXmlObject(root)
        expected = """<ns0:x xmlns:ns0="http://xspf.org/ns/0/"><ns0:track><ns0:info>info</ns0:info></ns0:track></ns0:x>"""
        xml = ET.tostring(root, "utf-8")
        self.assertEqual(expected, xml)

    def testImage(self):
        root = ET.Element("{http://xspf.org/ns/0/}x")
        t = xspf.Track()
        t.image = "image"
        root = t.getXmlObject(root)
        expected = """<ns0:x xmlns:ns0="http://xspf.org/ns/0/"><ns0:track><ns0:image>image</ns0:image></ns0:track></ns0:x>"""
        xml = ET.tostring(root, "utf-8")
        self.assertEqual(expected, xml)

    def testAlbum(self):
        root = ET.Element("{http://xspf.org/ns/0/}x")
        t = xspf.Track()
        t.album = "album"
        root = t.getXmlObject(root)
        expected = """<ns0:x xmlns:ns0="http://xspf.org/ns/0/"><ns0:track><ns0:album>album</ns0:album></ns0:track></ns0:x>"""
        xml = ET.tostring(root, "utf-8")
        self.assertEqual(expected, xml)

    def testTrackNum(self):
        root = ET.Element("{http://xspf.org/ns/0/}x")
        t = xspf.Track()
        t.trackNum = "1"
        root = t.getXmlObject(root)
        expected = """<ns0:x xmlns:ns0="http://xspf.org/ns/0/"><ns0:track><ns0:trackNum>1</ns0:trackNum></ns0:track></ns0:x>"""
        xml = ET.tostring(root, "utf-8")
        self.assertEqual(expected, xml)

    def testDuration(self):
        root = ET.Element("{http://xspf.org/ns/0/}x")
        t = xspf.Track()
        t.duration = "1000"
        root = t.getXmlObject(root)
        expected = """<ns0:x xmlns:ns0="http://xspf.org/ns/0/"><ns0:track><ns0:duration>1000</ns0:duration></ns0:track></ns0:x>"""
        xml = ET.tostring(root, "utf-8")
        self.assertEqual(expected, xml)

    def testKwargs(self):
        """ Test that all attribute names as kwargs works"""
        t = xspf.Track(location="loc"
                    , identifier="id"
                    , title="atitle"
                    , creator="cre"
                    , annotation="annotation"
                    , info="info"
                    , image="image"
                    , album="analbum"
                    , trackNum="1"
                    , duration="1000")

        self.assertEqual("loc", t.location)
        self.assertEqual("id", t.identifier)
        self.assertEqual("atitle", t.title)
        self.assertEqual("cre", t.creator)
        self.assertEqual("annotation", t.annotation)
        self.assertEqual("info", t.info)
        self.assertEqual("image", t.image)
        self.assertEqual("analbum", t.album)
        self.assertEqual("1", t.trackNum)
        self.assertEqual("1000", t.duration)

    def testDict(self):
        """ Test that attributes as a dictionary works """
        t = xspf.Track({"title": "atitle", "creator": "alastair"})
        self.assertEqual("atitle", t.title)
        self.assertEqual("alastair", t.creator)

    def testAddTrack(self):
        """ Add a track and check the XML """
        x = xspf.Xspf(title="my title")
        t = xspf.Track(title="title", creator="artist")
        x.add_track(t)

        expected = """<ns0:playlist version="1" xmlns:ns0="http://xspf.org/ns/0/"><ns0:title>my title</ns0:title><ns0:trackList><ns0:track><ns0:title>title</ns0:title><ns0:creator>artist</ns0:creator></ns0:track></ns0:trackList></ns0:playlist>"""
        self.assertEqual(expected, x.toXml())
