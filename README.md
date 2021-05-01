# sqlgrep

Grep for text in sqlite databases

## Synopsis

```txt
Usage: sqlgrep [OPTIONS] PATTERN FILES ...

  grep for sqlite databases

  searchs every field of every row in every table for PATTERN

  prints out matching table, column, row number, field value

Arguments:
  PATTERN    pattern to search for, may be a regular expression  [required]
  FILES ...  sqlite file(s) to search  [required]

Options:
  -i, --ignore-case               Ignore case
  -h, --no-filename               Never print filename headers (i.e.
                                  filenames) with output lines.

  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.

  --help                          Show this message and exit.
```

## Requires

- [typer](https://github.com/tiangolo/typer)
- [rich](https://github.com/willmcgugan/rich)

