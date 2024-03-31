from pathlib import Path

from grizzlys.utils.decorators import julia_using_modules


@julia_using_modules(["DataFrames", "CSV"])
def read_csv(filepath: str | Path): ...
