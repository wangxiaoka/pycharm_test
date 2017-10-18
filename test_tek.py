# -*- coding: utf-8 -*-

import visa

SCOPE_VISA_ADDRESS = "USB0::0x0957::0x1783::MY47050006::0::INSTR"
ta = visa.ResourceManager('C:\\Windows\\System32\\visa32.dll')
KsInfiniiVisionX = ta.open_resource(SCOPE_VISA_ADDRESS)
KsInfiniiVisionX.timeout = 1000
