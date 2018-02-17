from guick import gui_it
import click

@click.command()
@click.option("--hello", help="say hello")
@click.option("--add", type=int, help="input a number")
def example_cmd(hello, add):
    print("hello:", hello, type(hello))
    print("add:", add, type(add))


if __name__ == "__main__":
    gui_it(example_cmd)
