import sys
import subprocess

for i in range(1,6):
    daily_process = subprocess.Popen(['python3', 'daily.py', str(i)])
    daily_process.wait()
