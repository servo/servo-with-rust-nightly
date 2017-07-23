import time
import subprocess
import sys

def main(args):
    process = subprocess.Popen(args)
    while 1:
        for _ in range(5 * 60):
            result = process.poll()
            if result is not None:
                sys.exit(result)
            time.sleep(1)
        print("(Dummy output to convince Travis we're still working)")

if __name__ == "__main__":
    main(sys.argv[1:])
