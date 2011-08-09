XSPF
----
A simple [xspf](http://xspf.org) generator for python.

To install, either run
    python setup.py install
or copy xspf.py into your project.

Use
---
    import xspf
    x = xspf.Xspf()

    x.title = "my playlist"
    x.info = "http://example.org"
    # You can set these attributes:
    # title, creator, annotation, info, location, identifier, image, date, license

    # Add attributes at creation:
    y = xspf.Xspf(title="playlist", creator="alastair")
    # Or, with a dictionary
    z = xspf.Xspf({"title": "playlist", "creator": "alastair"})

    # Add tracks by creating a Track object
    tr1 = xspf.Track()
    tr1.title = ""
    tr1.creator = ""
    tr2 = xspf.Track(title="", creator="")
    tr3 = xspf.Track({"title": "", "creator": ""})
    x.add_track(tr1)
    x.add_tracks([tr2, tr3])

    # Or by passing the track information directly into add_track:
    x.add_track(title="", creator="")
    x.add_track({"title": "", "creator": ""})

    # Finally, get the XML contents
    print x.toXml()

If you don't like typing Xspf, we've helpfully aliased 'Spiff' to the same thing:

    from xspf import Spiff
    x = Spiff()
    ... etc

Reading xspf?
-------------
You might want to use [xspfparser](https://github.com/jwheare/xspfparser)

You can load a playlist parsed with xspfparser, modify it, then write it out again.

    result = xspfparser.parse(url)
    x = Xspf(result['playlist'])
    # we also support if you forget to deference playlist:
    y = Xspf(result)
    x.title = "New title"

    print x.toXml()

License
-------
Copyright 2011 Alastair Porter. All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are
permitted provided that the following conditions are met:

   1. Redistributions of source code must retain the above copyright notice, this list of
      conditions and the following disclaimer.

   2. Redistributions in binary form must reproduce the above copyright notice, this list
      of conditions and the following disclaimer in the documentation and/or other materials
      provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS ``AS IS'' AND ANY EXPRESS OR IMPLIED
WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

