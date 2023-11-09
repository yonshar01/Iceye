def processing(file_path):
    import subprocess
    import sys

    process = subprocess.Popen([sys.executable, file_path])
    process.communicate()
