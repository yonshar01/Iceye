# -*- UTF-8 -*-
"""
Script created for the Iceye assessment.
@author: Yonatan Shahar 
"""


def processing(file_path):
    import subprocess
    import sys

    process = subprocess.Popen([sys.executable, file_path])
    process.communicate()
