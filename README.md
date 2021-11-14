## This fork is only here to allow users to install from OctoPrint Plugin Repo, looking for maintainer. https://github.com/OctoPrint/plugins.octoprint.org/issues/961

GCodeSuperLaserController
=========================
This is a basic plugin to work with a Laser Engraver.
Printing from the OctoPrint interface with this plugin can turn your 3D printer into a laser engraver!

Commands
--------
- **M3 \<p\>**:  Turns ON the laser with power \<p\>
- **M4 \<p\>**:  Turns ON the laser with power 255-\<p\>
- **M5**:  Turn OFF the laser

The laser power can go from 1 (min) to 255 (MAX)

**NOTE:** It's highly suggested to add an [**M400** - Finish Moves](http://marlinfw.org/docs/gcode/M400.html) before the M3, M4 and M5 commands.

How to Use
----------

Step 0) Install the plugin<br/>
Step 1) Connect the Laser driver to pins GPIO18 and GND<br/>
Step 2) Create a GCode using the described commands<br/>
Step 3) Print **using Octoprint**


**Have fun :)**<br/>
Oh, almost forgot, I'm not responsible for you hurting yourself with your cool laser, but please use it with caution.
