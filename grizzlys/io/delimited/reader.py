from pathlib import Path

from grizzlys._utils.decorators import julia_using
from grizzlys.core.session import julia as jl


@julia_using(["DataFrames", "DelimitedFiles"])
def read_delimited(filepath: str | Path, delimiter: str):
    if len(delimiter) != 1:
        raise ValueError(rf"Delimiter must be a single character, got {delimiter!r}")
    data, header = jl.DelimitedFiles.readdlm(str(filepath), jl.only(delimiter), header=True)
    return jl.DataFrame(data, jl.vec(header))
