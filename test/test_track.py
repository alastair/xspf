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
        expected = b"""<x xmlns="http://xspf.org/ns/0/"><track><location>location</location></track></x>"""
        xml = ET.tostring(root, "utf-8")
        self.assertEqual(expected, xml)

    def testIdentifier(self):
        root = ET.Element("{http://xspf.org/ns/0/}x")
        t = xspf.Track()
        t.identifier = "id"
        root = t.getXmlObject(root)
        expected = b"""<x xmlns="http://xspf.org/ns/0/"><track><identifier>id</identifier></track></x>"""
        xml = ET.tostring(root, "utf-8")
        self.assertEqual(expected, xml)

    def testTitle(self):
        root = ET.Element("{http://xspf.org/ns/0/}x")
        t = xspf.Track()
        t.title = "title"
        root = t.getXmlObject(root)
        expected = b"""<x xmlns="http://xspf.org/ns/0/"><track><title>title</title></track></x>"""
        xml = ET.tostring(root, "utf-8")
        self.assertEqual(expected, xml)

    def tesCreator(self):
        root = ET.Element("{http://xspf.org/ns/0/}x")
        t = xspf.Track()
        t.creator = "creator"
        root = t.getXmlObject(root)
        expected = b"""<x xmlns="http://xspf.org/ns/0/"><track><creator>creator</creator></track></x>"""
        xml = ET.tostring(root, "utf-8")
        self.assertEqual(expected, xml)

    def testAnnotation(self):
        root = ET.Element("{http://xspf.org/ns/0/}x")
        t = xspf.Track()
        t.annotation = "ann"
        root = t.getXmlObject(root)
        expected = b"""<x xmlns="http://xspf.org/ns/0/"><track><annotation>ann</annotation></track></x>"""
        xml = ET.tostring(root, "utf-8")
        self.assertEqual(expected, xml)

    def testInfo(self):
        root = ET.Element("{http://xspf.org/ns/0/}x")
        t = xspf.Track()
        t.info = "info"
        root = t.getXmlObject(root)
        expected = b"""<x xmlns="http://xspf.org/ns/0/"><track><info>info</info></track></x>"""
        xml = ET.tostring(root, "utf-8")
        self.assertEqual(expected, xml)

    def testImage(self):
        root = ET.Element("{http://xspf.org/ns/0/}x")
        t = xspf.Track()
        t.image = "image"
        root = t.getXmlObject(root)
        expected = b"""<x xmlns="http://xspf.org/ns/0/"><track><image>image</image></track></x>"""
        xml = ET.tostring(root, "utf-8")
        self.assertEqual(expected, xml)

    def testAlbum(self):
        root = ET.Element("{http://xspf.org/ns/0/}x")
        t = xspf.Track()
        t.album = "album"
        root = t.getXmlObject(root)
        expected = b"""<x xmlns="http://xspf.org/ns/0/"><track><album>album</album></track></x>"""
        xml = ET.tostring(root, "utf-8")
        self.assertEqual(expected, xml)

    def testTrackNum(self):
        root = ET.Element("{http://xspf.org/ns/0/}x")
        t = xspf.Track()
        t.trackNum = "1"
        root = t.getXmlObject(root)
        expected = b"""<x xmlns="http://xspf.org/ns/0/"><track><trackNum>1</trackNum></track></x>"""
        xml = ET.tostring(root, "utf-8")
        self.assertEqual(expected, xml)

    def testDuration(self):
        root = ET.Element("{http://xspf.org/ns/0/}x")
        t = xspf.Track()
        t.duration = "1000"
        root = t.getXmlObject(root)
        expected = b"""<x xmlns="http://xspf.org/ns/0/"><track><duration>1000</duration></track></x>"""
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

        expected = b"""<playlist xmlns="http://xspf.org/ns/0/" version="1"><title>my title</title><trackList><track><title>title</title><creator>artist</creator></track></trackList></playlist>"""
        self.assertEqual(expected, x.toXml(pretty_print=False))

    def testAddTrackByDict(self):
        """ Add a track via a dictionary and check the XML """
        x = xspf.Xspf(title="my title")
        t = xspf.Track()
        x.add_track({"title": "title", "creator": "artist"})

        expected = b"""<playlist xmlns="http://xspf.org/ns/0/" version="1"><title>my title</title><trackList><track><title>title</title><creator>artist</creator></track></trackList></playlist>"""
        self.assertEqual(expected, x.toXml(pretty_print=False))

    def testAddTrackByKwargs(self):
        """ Add a track via kwargs and check the XML """
        x = xspf.Xspf(title="my title")
        x.add_track(title="title", creator="artist")

        expected = b"""<playlist xmlns="http://xspf.org/ns/0/" version="1"><title>my title</title><trackList><track><title>title</title><creator>artist</creator></track></trackList></playlist>"""
        self.assertEqual(expected, x.toXml(pretty_print=False))

    def testAddTracks(self):
        """ Add more than 1 track at a time """
        x = xspf.Xspf(title="my title")
        t = xspf.Track(title="t", creator="c")
        u = xspf.Track(title="u", creator="d")
        x.add_tracks([t, u])
        self.assertEqual(2, len(x.track))
