# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 15 Feb 2020
email: sabbir@rokomari.com, sabbiramin.cse11ruet@gmail.com

"""

import argparse
import sys

choices = ["init", "serve", "listen"]

from taskmongr.serving import run_server
from taskmongr.scripts import create_db
from taskmongr.executor import executor_serving


def main():
    parser = argparse.ArgumentParser(
        description="A Simple Task Scheduling and Queueing in Python.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "source",
        type=str,
        choices=choices,
        help="""\
- init    : Start the Db Preparation, Drops Existing One.
- serve   : Start the Server.
- listen  : Start the Listener.
- about   : About the Author.

"""
    )
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()
    source = args.source.lower()

    if source not in choices:
        vals = ", ".join(["'{}'".format(c) for c in choices])
        parser.error(
            "Unrecognized source '{}'. Valid entries are {}.".format(args.source, vals)
        )
    elif source == "init":
        create_db()
    elif source == "serve":
        run_server()
    elif source == "listen":
        executor_serving()


if __name__ == "__main":
    main()
