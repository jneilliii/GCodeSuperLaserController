# coding=utf-8
from __future__ import absolute_import
import octoprint.plugin
import pigpio
import time
import os
import sys
import re

INVERT = False
DEBUG  = False
PCIO_ID  = "18"
PIGS_CMD = "pigs p " + PCIO_ID + " "


class GCodeSuperLaserController(octoprint.plugin.StartupPlugin,
                            octoprint.plugin.TemplatePlugin,
                            octoprint.plugin.AssetPlugin,
                            octoprint.plugin.SettingsPlugin):

    pigClient = None

    def __init__(self):
        self.pigClient = pigpio.pi()

    def hook_gcode_queuing(self, comm_instance, phase, cmd, cmd_type, gcode, *args, **kwargs):
        regM = re.compile('M\d+')
        commandNumbers = regM.findall(cmd)

        if len(commandNumbers) > 0:
            commandNumber = commandNumbers[0]
        # ------------------------------------------------------

            if commandNumber == "M3":
                regS = re.compile('S\d+')
                commandValue = regS.findall(cmd)[0]
                finalValue = 0

                if INVERT:
                    finalValue = 255 - int(commandValue[1:])
                else:
                    finalValue = int(commandValue[1:])

                self.pigClient.set_PWM_dutycycle(18, finalValue)

                if DEBUG:
                    myCmd = PIGS_CMD + str(finalValue)
                    print myCmd

        # ------------------------------------------------------

            if commandNumber == "M4" or commandNumber == "M5":
                finalValue = 0
                if INVERT:
                    finalValue = 255

                self.pigClient.set_PWM_dutycycle(18, finalValue)

                if DEBUG:
                    myCmd = PIGS_CMD + str(finalValue)
                    print myCmd

        # ------------------------------------------------------


    def get_update_information(self):
        return dict(
            GCodeSuperLaserController=dict(
                displayName="GSLC Config",
                displayVersion=self._plugin_version,
            )
        )

__plugin_name__ = "GCodeSuperLaserController"

def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = GCodeSuperLaserController()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.comm.protocol.gcode.queuing": __plugin_implementation__.hook_gcode_queuing,
    }
