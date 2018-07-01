import subprocess
import sys

def main():
    if len(sys.argv) > 1:
        subprocess.call(['bundle', 'update'])
    subprocess.call(['bundle', 'exec', 'jekyll', 'serve'])

main()