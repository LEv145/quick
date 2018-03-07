# GUICK

This project is inspired by [Gooey](https://github.com/chriskiehl/Gooey),
which generate GUI for a classical python `argparse`-based command line
program.

## Install

```
python setup.py install
```

## Usage

### Basic usage

This package could draw the gui for a click-based CLI program with a very
simple function `gui_it`. The usage is wrapping the command function
`example_cmd()`  like `gui_it(example_cmd)`. The full example is like
this.

```python
from guick import gui_it
import click

from guick import gui_it
import click

@click.command()
@click.option("--hello", default="world", help="say hello")
@click.option("--add", type=int, help="input an integer number",\
              hide_input=True)
@click.option("--minus", type=float, help="input two numbers", nargs=2)
@click.option("--flag", is_flag=True)
@click.option('--shout/--no-shout', default=True)
@click.option('--language', type=click.Choice(['c', 'c++']))
@click.option('-v', '--verbose', count=True)
def example_cmd(**argvs):
    for k, v in argvs.items():
        print(k, v, type(v))


if __name__ == "__main__":
    # example_cmd()
    gui_it(example_cmd)
```

###  Add `--gui` option to your command

A common case is not changing all your command into a gui version, but just
add a `--gui` option to it. Then you can do this.

```python
from guick import gui_option
import click

@gui_option
@click.group()
@click.option('--debug/--no-debug', default=False)
def cli(debug):
    print(debug)


@cli.command()
@click.argument("arg", nargs=-1)
@click.option("--hello", default="world", help="say hello")
@click.option('-v', '--verbose', count=True)
def example_cmd(**argvs):
    for k, v in argvs.items():
        print(k, v, type(v))


@cli.command()
@click.option("--hello")
def sync(hello):
    print('Synching', hello)


@cli.command()
def func(**argvs):
    pass

if __name__ == "__main__":
    cli()
```

### Writing you own widget


## Copyright
see LICENCE
