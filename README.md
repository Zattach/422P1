# This program was created for project 1 of CIS 422,Software Methodologies

## Brief description: 
This Cold-Caller software takes in the Roster.tsv file as input, generate a list of randomly chosen students to be cold-called on, display those students on the screen, and record the students' performance which will be exported in a daily log file.

## Authors: 
Nick Bonat, Jerry Xie, Vu Vo, Qi Han, Zach Domke

## Creation date: 
April 1, 2019

## Target OS: 
MacOS 10.13 and above

## Usage: 
- Try the existing .app in the dist/ folder
- If the .app does not work then run the install.sh shell script. This will:
	- install py2app
	- use py2app to create a cold-call application in the dist/ folder

## Dependencies: 
To run this program, you will need Python 3.6 or higher.

## Misc
- In the subdirectory 'importFolder', there is a Roster.tsv file that will be used as input.
- In the subdirectory 'Resources', there are 4 .png files that are used for user interface. 
- There are also two subdirectories 'Photos' which includes the profile pictures of students in the roster in .png format, and 'Photos(JPG)' which have those pictures in .jpg format.
- To support the display of pictures in JPG format, you might want to use a third party library called [PIL](https://pillow.readthedocs.io/en/stable/)

