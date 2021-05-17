import subprocess

subprocess.check_output(['pyuic5', 'cartoonify_gui.ui', '-o', 'gui.py'])