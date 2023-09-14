from pathlib import Path
from typing import Any

import apsw.bestpractice
import apsw.shell
import typer
from typing_extensions import Annotated

apsw.bestpractice.apply(apsw.bestpractice.recommended)

app = typer.Typer()

ArgInputDB = Annotated[
    Path, typer.Argument(dir_okay=False, exists=True, help="Existing database")
]


@app.command()
def shell(dbpath: ArgInputDB):
    apsw.shell.Shell(db=(apsw.Connection(str(dbpath)))).cmdloop()


def main() -> Any:
    return app()
