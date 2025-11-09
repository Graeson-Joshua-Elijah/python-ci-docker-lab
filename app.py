# app.py
import argparse

def multiply(a: int, b: int) -> int:
    """Return product of two integers."""
    return a * b

def main():
    parser = argparse.ArgumentParser(prog="python-ci-lab")
    parser.add_argument("--a", type=int, default=2, help="first integer")
    parser.add_argument("--b", type=int, default=3, help="second integer")
    parser.add_argument("--quiet", action="store_true", help="only print result")
    args = parser.parse_args()

    result = multiply(args.a, args.b)
    if args.quiet:
        print(result)
    else:
        print(f"{args.a} * {args.b} = {result}")

if __name__ == "__main__":
    main()
