# Shadowdark.py

shadowdark.py walks you through generating a single character.

SD-Four-Zeroes.py generates random Zero Level characters in bulk.

These programs generate characters for the Shadowdark RPG, the quickstart rules are availble at;

https://www.drivethrurpg.com/product/413713/Shadowdark-RPG-Quickstart-Set

I wrote these programs with Python 3.11.2, they should work fine with any 3.x version, I will probably ignore the problem if it doesn't work on versions of Python other than what I am using. You will need Python to run this program, Python is free and open software, it is availble for download at Python.org. If you are not familar with Python, here is a quick guide on getting it installed in Windows. If you use Linux or Mac OS, it is already installed.

https://www.howtogeek.com/197947/how-to-install-python-on-windows/

If you are completely unfamilar with Python, it is a fairly easy programing language to learn. There are many good tutorials on the internet for learning the basics of Python. Below is an hour long Youtube video that gives you pretty much everything you need to know about Python to understand how this program works so you can start modifing it for you own purposes. One of my goals here was to build a simple enough code base where even someone with no Python experience can add thier own Ancestries and Classes just by looking at the code and doing a bit of copy/paste and modify work. I encourage everyone to copy this program, modify it and make it your own.

https://www.youtube.com/watch?v=kqtD5dpn9C8&t=1882s

These are commandline, text only programs, there is no fancy Windows GUI, this will not change anytime soon. This is an offshoot project from a Basic program I wrote to make Shadowdark characters, which itself was an offshoot of a program I wrote in the early 90's for making D&D characters. I am no longer working on that code and I made the repository private, all further work in this area will be done on this project.

This project is not meant to be a full fledged character manager, the sole purpose of these programs is to generate Zero level or 1st level characters. The use cases being quick NPC generator, pregenerated characters and lazy players. If you are looking for a more advanced program, I suggest https://shadowdarklings.net/ or https://www.shadowdork.com/welcome-component.

I was going to add functionality to the program to generate 4 random Zero level characters for Gauntlet style play, but I decided it was just easier to break that out into a seperate program. When run, the program will ask you the name of the file you want to save your Zero level characters to and how many you wish to generate. This program does not care if the character has at least one attribute above 14 or not, my suggestion is to have it create double the number of characters you need for your game and then choose the ones you want use. If you are going to print these out, For the best results, seperate each character into its own file and save them seperately. This way when printed each character is on its own piece of paper.

Thank you to Kelsey Dionne for creating the Shadowdark RPG, your hard work and creativity is appreciated.

https://www.thearcanelibrary.com/

Legal Statement: This Shadowdark Character Generator is an independent product published under the Shadowdark RPG Third-Party License and is not affiliated with The Arcane Library, LLC. Shadowdark RPG © 2023 The Arcane Library, LLC."

MIT License:
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

If Python is not your thing and you want a stand alone program, I have ported the program to C++ and compiled it for Windows 10/11. Both the binary and the source code is available here;

https://github.com/cjstoddard/Shadowdark.cpp