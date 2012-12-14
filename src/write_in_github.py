import sys

def do():
  for line in sys.stdin.readlines():
    sys.stdout.write(line)


if __name__=="__main__":
  do()

