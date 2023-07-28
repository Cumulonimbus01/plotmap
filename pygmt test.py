import pygmt


# Load sample earth relief data
grid = pygmt.datasets.load_earth_relief(resolution="15s",  region=[119, 123, 22, 26]  )
#grid = pygmt.datasets.load_earth_relief(resolution="15s",  region=[120.7,122.3,24.3,25.7]  )

fig = pygmt.Figure()
fig.grdview(
    grid=grid,
    perspective=[250, 15],
    frame=["xa", "yaf", "WSnE"],
    projection="M15c",
    zsize="1.5c",
    # Set the surftype to "surface"
    surftype="s",
    # Set the CPT to "geo"
    cmap="geo",
    region=[119, 123, 22, 26] 
    #region=[120.7,122.3,24.3,25.7]
)

fig.savefig(r"K:\pygmt\TWview.png",dpi=300)

fig.show()
