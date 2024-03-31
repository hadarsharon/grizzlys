import juliacall

jl = juliacall.newmodule("grizzlys.interchange.dataframe")

df = jl.DataFrame(jl.CSV.File("/Users/hadars/Downloads/adjust_skad_libi.csv"))
print(dir(df))
