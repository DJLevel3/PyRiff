# PyRiff
## A simple Python library for writing data to RIFF files

This was written in one day by me (DJ_Level_3), and it should be compliant to the RIFF specification in terms of how data is marked and stored. This hasn't been checked 100%, however, as I can't find a specification that is comprehensive enough but still readable. Specifically, the potential issue is with padding. I'm pretty sure that I wrote it correctly, as supposedly chunks should be padded to the next 16-bit boundary, but I'm not sure if the padding is supposed to be contained in the chunk or after it. I assumed the latter.

------------

There is currently NO functionality to read or interpret RIFF files, as I pretty much developed this just to write some data to a file so I could then use it later in a separate Java program. If you're wondering what program that is, it's [osci-render](https://github.com/jameshball/osci-render). The functionality may or may not be actually pushed to the main branch, however, as I'm working in my own repository and I'll make a PR when it's done.