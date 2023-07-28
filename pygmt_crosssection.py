import pygmt
import numpy as np
import pandas as pd

def main():
    
    pygmt.config(FONT_LABEL="auto")
    
    # Define Lambert Conformal Conic projection parameters
    central_longitude = 121.0
    central_latitude = 23.5
    standard_parallels = (10, 40)

    # Create the Lambert Conformal Conic projection in PyGMT
    projection = f"L{central_longitude}/{central_latitude}/{'/'.join(map(str, standard_parallels))}/10c"
    #projection="M5c"
    
    grid = pygmt.datasets.load_earth_relief(resolution="15s",region=[120.3,122.2,24.3,26.])
    fig = pygmt.Figure()
    fig.grdimage(grid=grid, projection=projection, frame=["a","+tCross Section"], cmap="geo")
    fig.colorbar(frame=["a1000", "x+lElevation", "y+lm"])
    
    #-----------------------
    sta= pd.read_excel(r"K:\201809rain\ground observation\highres\station_auto_name.xlsx", header=None)
    sta=sta.rename(columns={0: "stno", 1: "stna", 2: "alt", 3: "lon", 4: "lat", 5:"city", 6:"address", 7:"startd", 8:"endd", 9:"ori", 10:"new"})

    
    mask = (sta['startd'] <= '2018-9-8')
    sta=sta.loc[mask]   
    sta.endd=sta.endd.fillna(pd.to_datetime('2018-9-8'))
    mask = (sta['endd'] >= '2018-9-8')
    sta=sta.loc[mask]
    print(sta)    
    
    fig.plot(x=sta["lon"][:], y=sta["lat"][:], style="c0.1c", fill="black")

    #--------------------------------------------------
    
    
    fig.plot(
        x=[ 121, 122, 122, 121, 121],  # longitude
        y=[ 24.5,  24.5, 25.5, 25.5, 24.5],  # latitude
        projection=projection,  # projection is an alias for '-J'
        pen="3,gray,12_8:8p",  # pen is an alias for '-W'
        frame="g30",  # frame is an alias for '-B'
    )
    fig.plot(
        x=[121.1, 121.8],  # longitude
        y=[25.8, 25.2],  # latitude
        projection=projection,  # projection is an alias for '-J'
        pen="3,12_4:4p",  # pen is an alias for '-W'
        frame="g30",  # frame is an alias for '-B'
    )
    fig.plot(
        x=[121.375, 121.8],  # longitude
        y=[25.1, 24.775],  # latitude
        projection=projection,  # projection is an alias for '-J'
        pen="3,12_4:4p",  # pen is an alias for '-W'
        frame="g30",  # frame is an alias for '-B'
    )
    fig.plot(
        x=[120.45, 121.25],  # longitude
        y=[25.75, 24.95],  # latitude
        projection=projection,  # projection is an alias for '-J'
        pen="3,12_4:4p",  # pen is an alias for '-W'
        frame="g30",  # frame is an alias for '-B'
    )
    fig.text(text=["B line", "A line","C line"], x=[121.75, 120.7,121.7 ], y=[25.5, 25.3, 25.],font="16p,Helvetica-Bold,black" )

    fig.text(text="Snow Mountain Range", x=121.45, y=24.7,font="16p,Helvetica-Bold,white", angle=35, transparency=30)
    fig.text(text="Yilan", x=121.75, y=24.7,font="8p,Helvetica-Bold,white", angle=0, transparency=30)
    fig.text(text="Taipei Basin", x=121.5, y=25.,font="8p,Helvetica-Bold,white", angle=35, transparency=30)
    
    fig.savefig(r"K:\pygmt\Crosssection_300.png",dpi=500)
    fig.show()

if __name__ == "__main__":
    main()