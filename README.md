# Sequence Delivery Tool

## CODE ARCHITECTURE, WRITING, AND PROBLEM SOLVING

Design and implement an example tool using Python3 and Pyside2 that sorts and formats delivery files for a client. You may use whatever libraries you think are needed, but they should be available to a client for free. It should run on Windows 10.

Required _user controls:_
1) A text box and file browser button for the user to select which directory to format.
2) A text box and file browser button for the user to select which directory to move the delivery output to.
3) An execute button.
4) A cancel button.

_File Format Input:_
A single directory containing an image sequence of unknown length in multiple file formats. The naming of the sequence images is consistent, and all frames will be present.

_Output:_
Using parsed information from the filename, reformat the image sequences into the provided delivery format.

_Examples:_
The following are examples only. You should provide your own input and output files with your own naming for testing.

    Example Input:
    delivery01/
        PROJECTNAME_SHOTNAME_TASKNAME.0001.dpx
        PROJECTNAME_SHOTNAME_TASKNAME.0002.dpx
        PROJECTNAME_SHOTNAME_TASKNAME.0003.dpx
        PROJECTNAME_SHOTNAME_TASKNAME.0001.exr
        PROJECTNAME_SHOTNAME_TASKNAME.0002.exr
        PROJECTNAME_SHOTNAME_TASKNAME.0003.exr
        PROJECTNAME_SHOTNAME_TASKNAME.0001.jpg
        PROJECTNAME_SHOTNAME_TASKNAME.0002.jpg
        PROJECTNAME_SHOTNAME_TASKNAME.0003.jpg

        Example Output:
        PROJECTNAME/
            DATE/
                PROJECTNAME_SHOTNAME/
                    TASKNAME/
                        EXR/
                            PROJECTNAME_SHOTNAME_TASKNAME.0001.exr
                            PROJECTNAME_SHOTNAME_TASKNAME.0002.exr
                            PROJECTNAME_SHOTNAME_TASKNAME.0003.exr
                        DPX/
                            PROJECTNAME_SHOTNAME_TASKNAME.0001.dpx
                            PROJECTNAME_SHOTNAME_TASKNAME.0002.dpx
                            PROJECTNAME_SHOTNAME_TASKNAME.0003.dpx
                        JPG/
                            PROJECTNAME_SHOTNAME_TASKNAME.0001.jpg
                            PROJECTNAME_SHOTNAME_TASKNAME.0002.jpg
                            PROJECTNAME_SHOTNAME_TASKNAME.0003.jpg

_Notes:_
* The filenames will consistently be in the format of "PROJECTNAME_SHOTNAME_TASKNAME.FRAMENUMBER.FILETYPE" with the following constraints:
* There can be any filetype.
* Each section of the filename can be any length.
* Only letter characters will be used in PROJECTNAME, SHOTNAME and TASK NAME and these sections will always be separated by underscores ("_").
* Only numbers with a padding of four will be used in the FRAMENUMBER section and the frame number will always be surrounded by periods ('.')
* Format of the date folder should be as follows: YYYYMMDDHHMM
* Please use reStructuredText and PEP-8 compliant code

_Extra Credit:_
* Put in a progress bar for processing the files.
* Output a JSON manifest file containing the structure of the formatted delivery.
* Design the system to support multiple input directories.
