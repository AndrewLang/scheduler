import subprocess

class Executor:
    def launch(self, path, args):
        process = subprocess.Popen([path, args], shell=True, stdout=subprocess.PIPE)
        process.wait()
        
