# ============================================================
# Day 71: Command Line Utilities using argparse
# ============================================================
# argparse: the standard library for creating CLI tools
# ============================================================

import argparse

# --- BASIC argparse USAGE ---
def create_parser():
    parser = argparse.ArgumentParser(
        prog="myapp",
        description="A sample CLI tool built with argparse",
        epilog="Example: python day71.py greet --name Alice --shout"
    )

    # Subcommands
    subparsers = parser.add_subparsers(dest="command", help="sub-commands")

    # --- 'greet' subcommand ---
    greet_parser = subparsers.add_parser("greet", help="Greet a person")
    greet_parser.add_argument("--name",  "-n", type=str, required=True, help="Name to greet")
    greet_parser.add_argument("--shout", "-s", action="store_true",     help="Print in uppercase")

    # --- 'calc' subcommand ---
    calc_parser = subparsers.add_parser("calc", help="Simple calculator")
    calc_parser.add_argument("a", type=float, help="First number")
    calc_parser.add_argument("b", type=float, help="Second number")
    calc_parser.add_argument("--op", choices=["+", "-", "*", "/"], default="+")

    # --- 'info' subcommand ---
    info_parser = subparsers.add_parser("info", help="System info")
    info_parser.add_argument("--verbose", "-v", action="store_true")

    return parser

def main():
    parser = create_parser()
    args   = parser.parse_args()

    if args.command == "greet":
        msg = f"Hello, {args.name}!"
        print(msg.upper() if args.shout else msg)

    elif args.command == "calc":
        ops = {"+": args.a + args.b, "-": args.a - args.b,
               "*": args.a * args.b, "/": args.a / args.b if args.b != 0 else "Error: div by zero"}
        print(f"{args.a} {args.op} {args.b} = {ops[args.op]}")

    elif args.command == "info":
        import sys, platform
        print(f"Python: {sys.version}")
        print(f"OS    : {platform.system()} {platform.release()}")
        if args.verbose:
            print(f"Full  : {platform.platform()}")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()

# --- USAGE EXAMPLES (run from terminal) ---
# python argparse_cli.py greet --name Alice
# python argparse_cli.py greet -n Bob -s
# python argparse_cli.py calc 10 3 --op /
# python argparse_cli.py info --verbose
# python argparse_cli.py --help
