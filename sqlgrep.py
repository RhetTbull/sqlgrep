#!/usr/bin/env python3

""" grep for values in sqlite database file """

import re
import sqlite3
from pathlib import Path
from typing import List

import typer
from rich import print


def cli(
    ignore_case: bool = typer.Option(
        None, "-i", "--ignore-case", is_flag=True, help="Ignore case"
    ),
    no_filename: bool = typer.Option(
        None,
        "-h",
        "--no-filename",
        is_flag=True,
        help="Never print filename headers (i.e. filenames) with output lines.",
    ),
    pattern: str = typer.Argument(
        ...,
        metavar="PATTERN",
        help="pattern to search for, may be a regular expression",
    ),
    files: List[Path] = typer.Argument(
        ..., metavar="FILES ...", help="sqlite file(s) to search"
    ),
):
    """ grep for sqlite databases

        searchs every field of every row in every table for PATTERN

        prints out matching table, column, row number, field value
    """
    flags = re.IGNORECASE if ignore_case else 0

    for filename in files:
        if not filename.is_file():
            typer.echo(f"{filename} is not a valid file")
            raise typer.Exit(1)
        try:
            with sqlite3.connect(f"file:{filename}?mode=ro", uri=True) as conn:
                regex = re.compile(r"(" + pattern + r")", flags=flags)
                filename_header = f"{filename}: " if not no_filename else ""
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
                for tablerow in cursor.fetchall():
                    table = tablerow[0]
                    cursor.execute("SELECT * FROM {t}".format(t=table))
                    for row_num, row in enumerate(cursor):
                        for field in row.keys():
                            field_value = row[field]
                            if not field_value or type(field_value) == bytes:
                                # don't search binary blobs
                                next
                            field_value = str(field_value)
                            if re.search(pattern, field_value, flags=flags):
                                row_str = regex.sub(r"[bold]\1[/bold]", field_value)
                                print(
                                    f"{filename_header}{table}, {field}, {row_num}, {row_str}"
                                )
        except sqlite3.DatabaseError as e:
            typer.echo(f"{filename}: {e}")
            raise typer.Exit(1)


if __name__ == "__main__":
    typer.run(cli)
