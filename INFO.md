# Report
Initial approach was to read the doc about the structure in the Content index
files and ascertain then how to process the text

Once understood the 1st step was to dowload the actual file. In order to do that
there were several possibilities,
  - urllib
  - urllib2
  - requests

For this particular case there was not much information to go by for chosing any
of them, therefore I just chose 'requests' for simplicity

Then the next stage was to decide about the parameter validation, in this case it
seemed clear that a list of possible options was a good choice, also for simplicity
reasons, although later on it was a little more complicated with the addition
of the 'udeb-<arch>' files.

The validation was accomplished with a series of if statements rather than a try
and catch, as it was not needed to throw expecifics of the errors

Parameters are passed just the usual way via importing the sys module and using
the argv lib from it.

The next import used was
  - gzip
which it is the standard librery used to process gunzip files. The processing
works in a similar fashion than processing files, but however, becuase the list
of files sometimes contained two packages names separated by a command, this also
needed to be sorted.

After this processing the actual "counting" the files per packages etc, was done
via importing:
  - collections

It seemed very simple to accomplish the counting and processing of the output
with it.

The script is not by no means a performance oriented approach but a KISS one. It
was clear that there could have been more improvement with more research and
specific requirements.

Simple functions where created to help with the possible troubleshooting and
maintinance of the script as well as basic isolation of parts the code.

It took around 3/4 hours to write and research and around and hour to do the
writing.
