import subprocess

class Executor:
    def launch(self, path):
        subprocess.Popen(path)
        
