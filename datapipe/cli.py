# datapipe/cli.py
import argparse
import sys

from datapipe.pipeline import Pipeline


def build_parser():
    parser = argparse.ArgumentParser(prog="datapipe")
    sub = parser.add_subparsers(dest="command")

    run = sub.add_parser("run", help="run a pipeline described by flags")
    run.add_argument("--source", required=True)
    run.add_argument("--source-kind", default="auto")
    run.add_argument("--sink", required=True)
    run.add_argument("--sink-kind", default="csv")
    run.add_argument("--filter", dest="filter_expr", default=None)

    sub.add_parser("version", help="print the version")
    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command == "version":
        from datapipe import __version__
        print(__version__)
        return 0
    if args.command == "run":
        pipe = Pipeline("cli")
        rows = pipe.source(args.source, args.source_kind)
        if args.filter_expr:
            code = compile(args.filter_expr, "<filter>", "eval")
            rows = pipe.filter(rows, predicate=lambda r, _c=code: eval(_c, {}, dict(r)))
        pipe.sink(rows, args.sink, args.sink_kind)
        pipe.run()
        return 0
    parser.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
