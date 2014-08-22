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
        expected = b"""<playlist xmlns="http://xspf.org/ns/0/" version="1" />"""
        self.assertEqual(expected, x.toXml(pretty_print=False))

    def testTitle(self):
        x = xspf.Xspf()
        x.title = "title"
        expected = b"""<playlist xmlns="http://xspf.org/ns/0/" version="1"><title>title</title></playlist>"""
        self.assertEqual(expected, x.toXml(pretty_print=False))

    def testCreator(self):
        x = xspf.Xspf()
        x.creator = "creator"
        expected = b"""<playlist xmlns="http://xspf.org/ns/0/" version="1"><creator>creator</creator></playlist>"""
        self.assertEqual(expected, x.toXml(pretty_print=False))

    def testAnnotation(self):
        x = xspf.Xspf()
        x.annotation = "ann"
        expected = b"""<playlist xmlns="http://xspf.org/ns/0/" version="1"><annotation>ann</annotation></playlist>"""
        self.assertEqual(expected, x.toXml(pretty_print=False))

    def testInfo(self):
        x = xspf.Xspf()
        x.info = "info"
        expected = b"""<playlist xmlns="http://xspf.org/ns/0/" version="1"><info>info</info></playlist>"""
        self.assertEqual(expected, x.toXml(pretty_print=False))

    def testLocation(self):
        x = xspf.Xspf()
        x.location = "loc"
        expected = b"""<playlist xmlns="http://xspf.org/ns/0/" version="1"><location>loc</location></playlist>"""
        self.assertEqual(expected, x.toXml(pretty_print=False))

    def testIdentifier(self):
        x = xspf.Xspf()
        x.identifier = "id"
        expected = b"""<playlist xmlns="http://xspf.org/ns/0/" version="1"><identifier>id</identifier></playlist>"""
        self.assertEqual(expected, x.toXml(pretty_print=False))

    def testImage(self):
        x = xspf.Xspf()
        x.image = "image"
        expected = b"""<playlist xmlns="http://xspf.org/ns/0/" version="1"><image>image</image></playlist>"""
        self.assertEqual(expected, x.toXml(pretty_print=False))

    def testDate(self):
        x = xspf.Xspf()
        x.date = "date"
        expected = b"""<playlist xmlns="http://xspf.org/ns/0/" version="1"><date>date</date></playlist>"""
        self.assertEqual(expected, x.toXml(pretty_print=False))

    def testLicense(self):
        x = xspf.Xspf()
        x.license = "CC BY-SA"
        expected = b"""<playlist xmlns="http://xspf.org/ns/0/" version="1"><license>CC BY-SA</license></playlist>"""
        self.assertEqual(expected, x.toXml(pretty_print=False))

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

    def testDictTracks(self):
        """ Test that tracks from a dict work """
        x = xspf.Xspf({"title": "atitle", "track": [{"title": "tr1"}, {"title": "tr2"}]})
        self.assertEqual("atitle", x.title)
        self.assertEqual(2, len(x.track))
        self.assertEqual("tr1", x.track[0].title)
        self.assertEqual("tr2", x.track[1].title)

    def testXspfParser(self):
        """ Test that a JSPF-like dict works """
        parse = {"playlist": {"title": "atitle"}}
        x = xspf.Xspf(parse)
        self.assertEqual("atitle", x.title)

    def testMeta(self):
        """ Test that adding a meta tag works """

        x = xspf.Xspf()
        x.add_meta("key", "value")
        expected = b"""<playlist xmlns="http://xspf.org/ns/0/" version="1"><meta rel="key">value</meta></playlist>"""
        self.assertEqual(expected, x.toXml(pretty_print=False))

        x.add_meta("secondkey", "secondvalue")
        expected = b"""<playlist xmlns="http://xspf.org/ns/0/" version="1"><meta rel="key">value</meta><meta rel="secondkey">secondvalue</meta></playlist>"""
        self.assertEqual(expected, x.toXml(pretty_print=False))

        m = x.meta
        self.assertEqual("value", m["key"])
        self.assertEqual("secondvalue", m["secondkey"])

        x.del_meta("key")
        expected = b"""<playlist xmlns="http://xspf.org/ns/0/" version="1"><meta rel="secondkey">secondvalue</meta></playlist>"""
        self.assertEqual(expected, x.toXml(pretty_print=False))

    def testLink(self):
        """ Test adding a link tag """

        x = xspf.Xspf()
        x.add_link("http://somehref/namespace", "http://somepath/here")
        expected = b"""<playlist xmlns="http://xspf.org/ns/0/" version="1"><link rel="http://somehref/namespace">http://somepath/here</link></playlist>"""
        self.assertEqual(expected, x.toXml(pretty_print=False))
