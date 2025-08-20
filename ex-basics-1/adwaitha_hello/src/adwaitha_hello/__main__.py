import sys
from . import hello

def main() -> None:
    name = sys.argv[1] if len(sys.argv) > 1 else None
    print(hello(name))

if __name__ == "__main__":
    main()
