import pygmt
import numpy as np

def calculate_circle_points(center_lat, center_lon, radius_km, n_points=100):
    # Convert radius from km to degrees
    radius_deg = radius_km / 111.32

    # Create an array of angles from 0 to 360 degrees
    angles = np.linspace(0, 360, n_points)

    # Convert angles to radians
    radians = np.radians(angles)

    # Calculate circle coordinates
    circle_lat = center_lat + radius_deg * np.cos(radians)
    circle_lon = center_lon + radius_deg * np.sin(radians)

    return circle_lat, circle_lon

def main():
    
    # Define Lambert Conformal Conic projection parameters
    central_longitude = 121.0
    central_latitude = 23.5
    standard_parallels = (10, 40)

    # Create the Lambert Conformal Conic projection in PyGMT
    projection = f"L{central_longitude}/{central_latitude}/{'/'.join(map(str, standard_parallels))}/15c"
    
    grid = pygmt.datasets.load_earth_relief(resolution="30s",region=[91.9617, 150.038, 5.366, 45])
    fig = pygmt.Figure()
    fig.grdimage(grid=grid, projection=projection, region="99.8954/5.366/150.038/41.5538+r", frame=["ag","+t201809 Model Configuration"], cmap="geo")
    fig.colorbar(frame=["a2000", "x+lElevation", "y+lm"])
    fig.plot(
        x=[112.377, 111.102, 129.44, 128.425, 112.377],  # longitude
        y=[15.5066, 31.1679, 31.1679, 15.5066, 15.5066],  # latitude
        projection=projection,  # projection is an alias for '-J'
        pen="3",  # pen is an alias for '-W'
        frame="g30",  # frame is an alias for '-B'
    )
    fig.plot(
        x=[115.907, 115.512, 125.919, 125.565, 115.907],  # longitude
        y=[18.8978, 28.1668,  28.1668,  18.8978,  18.8978],  # latitude
        projection=projection,  # projection is an alias for '-J'
        pen="3",  # pen is an alias for '-W'
        frame="g30",  # frame is an alias for '-B'
    )

    # Add the 460 km circle
    center_lat = 25.07
    center_lon = 121.77
    radius_km = 460.0
    circle_lat, circle_lon = calculate_circle_points(center_lat, center_lon, radius_km)

    # Plot the circle with a red outline
    fig.plot(x=circle_lon, y=circle_lat, pen="5p,brown", projection=projection)
    fig.plot(x=121.77, y=25.07, style='d0.3c', fill="brown", projection=projection)
    fig.text(text=["d01", "d02", "d03"], x=[98, 113, 118], y=[40, 33, 30], font="20p,Helvetica-Bold,black")
    fig.text(text=["RCWF"], x=[122.5], y=[26], font="10p,Helvetica-Bold,black")
    fig.savefig(r"K:\pygmt\modelconfiguration_300.png",dpi=500)
    fig.show()

if __name__ == "__main__":
    main()