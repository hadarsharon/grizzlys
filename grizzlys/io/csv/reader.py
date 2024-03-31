from pathlib import Path

from grizzlys.utils.decorators import julia_using


@julia_using(["DataFrames", "CSV"])
def read_csv(filepath: str | Path): ...
