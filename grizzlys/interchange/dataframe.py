import juliacall

jl = juliacall.newmodule("grizzlys.interchange.dataframe")
jl.seval("using DataFrames, CSV")

dir(jl)
