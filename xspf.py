#!/usr/bin/python

import xml.etree.ElementTree as ET

class Xspf(object):
    def __init__(self, obj={}, **kwargs):
        self.NS = "http://xspf.org/ns/0/"
        self.version = "1"

        self._title = ""
        self._creator = ""
        self._info = ""
        self._annotation = ""
        self._location = ""
        self._identifier = ""
        self._image = ""
        self._date = ""
        self._license = ""

        self._trackList = []

        if len(obj):
            if "playlist" in obj:
                obj = obj["playlist"]
            for k, v in obj.items():
                setattr(self, k, v)

        if len(kwargs):
            for k, v in kwargs.items():
                setattr(self, k, v)

    @property
    def title(self):
        """A human-readable title for the playlist. Optional"""
        return self._title
    @title.setter
    def title(self, title):
        self._title = title

    @property
    def creator(self):
        """Human-readable name of the entity (author, authors, group, company, etc)
           that authored the playlist. Optional"""
        return self._creator
    @creator.setter
    def creator(self, creator):
        self._creator = creator

    @property
    def annotation(self):
        """A human-readable comment on the playlist. This is character data,
           not HTML, and it may not contain markup. Optional"""
        return self._annotation
    @annotation.setter
    def annotation(self, annotation):
        self._annotation = annotation

    @property
    def info(self):
        """URI of a web page to find out more about this playlist. Optional"""
        return self._info
    @info.setter
    def info(self, info):
        self._info = info

    @property
    def location(self):
        """Source URI for this playlist. Optional"""
        return self._location
    @location.setter
    def location(self, location):
        self._location = location

    @property
    def identifier(self):
        """Canonical ID for this playlist. Likely to be a hash or other
           location-independent name. Optional"""
        return self._identifier
    @identifier.setter
    def identifier(self, identifier):
        self._identifier = identifier

    @property
    def image(self):
        """URI of an image to display in the absence of a trackList/image
           element. Optional"""
        return self._image
    @image.setter
    def image(self, image):
        self._image = image

    @property
    def date(self):
        """Creation date (not last-modified date) of the playlist. Optional"""
        return self._date
    @date.setter
    def date(self, date):
        self._date = date

    @property
    def license(self):
        """URI of a resource that describes the license under which this
           playlist was released. Optional"""
        return self._license
    @license.setter
    def license(self, license):
        self._license = license

    # Todo: Attribution, Link, Meta, Extension

    def add_track(self, track):
        if isinstance(track, Track):
            self._trackList.append(track)

    def _addElementIfNotEmpty(self, parent, name, value):
        if value:
    	    el = ET.SubElement(parent, "{{{0}}}{1}".format(self.NS, name))
            el.text = value            

    def toXml(self, encoding="utf-8"):
        root = ET.Element("{{{0}}}playlist".format(self.NS))
        root.set("version", self.version)
        
        self._addElementIfNotEmpty(root, "title", self.title)
        self._addElementIfNotEmpty(root, "info", self.info)
        self._addElementIfNotEmpty(root, "creator", self.creator)
        self._addElementIfNotEmpty(root, "annotation", self.annotation)
        self._addElementIfNotEmpty(root, "location", self.location)
        self._addElementIfNotEmpty(root, "identifier", self.identifier)
        self._addElementIfNotEmpty(root, "image", self.image)
        self._addElementIfNotEmpty(root, "date", self.date)
        self._addElementIfNotEmpty(root, "license", self.license)

        if len(self._trackList):
            track_list = ET.SubElement(root, "{{{0}}}trackList".format(self.NS))
            for track in self._trackList:
                track_list = track.getXmlObject(track_list)
        return ET.tostring(root, encoding)

class Track(object):
    def __init__(self, obj={}, **kwargs):
        self.NS = "http://xspf.org/ns/0/"

        self._location = ""
        self._identifier = ""
        self._title = ""
        self._creator = ""
        self._annotation = ""
        self._info = ""
        self._image = ""
        self._album = ""
        self._trackNum = ""
        self._duration = ""

        if len(obj):
            for k, v in obj.items():
                setattr(self, k, v)

        if len(kwargs):
            for k, v in kwargs.items():
                setattr(self, k, v)

    @property
    def location(self):
        """URI of resource to be rendered. Probably an audio resource, but MAY be any type of
           resource with a well-known duration. Zero or more"""
        return self._location
    @location.setter
    def location(self, location):
        self._location = location

    @property
    def identifier(self):
        """ID for this resource. Likely to be a hash or other location-independent name,
           such as a MusicBrainz identifier.  MUST be a legal URI. Zero or more"""
        return self._identifier
    @identifier.setter
    def identifier(self, identifier):
        self._identifier = identifier

    @property
    def title(self):
        """Human-readable name of the track that authored the resource which defines the
           duration of track rendering. Optional"""
        return self._title
    @title.setter
    def title(self, title):
        self._title = title

    @property
    def creator(self):
        """Human-readable name of the entity (author, authors, group, company, etc) that authored
           the resource which defines the duration of track rendering."""
        return self._creator
    @creator.setter
    def creator(self, creator):
        self._creator = creator

    @property
    def annotation(self):
        """A human-readable comment on the track. This is character data, not HTML,
           and it may not contain markup."""
        return self._annotation
    @annotation.setter
    def annotation(self, annotation):
        self._annotation = annotation

    @property
    def info(self):
        """URI of a place where this resource can be bought or more info can be found. Optional"""
        return self._info
    @info.setter
    def info(self, info):
        self._info = info

    @property
    def image(self):
        """URI of an image to display for the duration of the track. Optional"""
        return self._image
    @image.setter
    def image(self, image):
        self._image = image

    @property
    def album(self):
        """Human-readable name of the collection from which the resource which defines
           the duration of track rendering comes. Optional"""
        return self._album
    @album.setter
    def album(self, album):
        self._album = album

    @property
    def trackNum(self):
        """Integer with value greater than zero giving the ordinal position of the media
           on the album. Optional"""
        return self._trackNum
    @trackNum.setter
    def trackNum(self, trackNum):
        self._trackNum = trackNum

    @property
    def duration(self):
        """The time to render a resource, in milliseconds. Optional"""
        return self._duration
    @duration.setter
    def duration(self, duration):
        self._duration = duration

    # Todo: Link, Meta, Extension

    def _addElementIfNotEmpty(self, parent, name, value):
        if value:
    	    el = ET.SubElement(parent, "{{{0}}}{1}".format(self.NS, name))
            el.text = value

    def getXmlObject(self, parent):
        track = ET.SubElement(parent, "{{{0}}}track".format(self.NS))
        self._addElementIfNotEmpty(track, "location", self.location)
        self._addElementIfNotEmpty(track, "identifier", self.identifier)
        self._addElementIfNotEmpty(track, "title", self.title)
        self._addElementIfNotEmpty(track, "creator", self.creator)
        self._addElementIfNotEmpty(track, "annotation", self.annotation)
        self._addElementIfNotEmpty(track, "info", self.info)
        self._addElementIfNotEmpty(track, "image", self.image)
        self._addElementIfNotEmpty(track, "album", self.album)
        self._addElementIfNotEmpty(track, "trackNum", self.trackNum)
        self._addElementIfNotEmpty(track, "duration", self.duration)
        return parent

Spiff = Xspf
