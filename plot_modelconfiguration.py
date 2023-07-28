#import os, sys
import pandas as pd
import cartopy
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import shapely.geometry as sgeom
import numpy as np
from cartopy.geodesic import Geodesic
from cartopy.io import shapereader
import cartopy.feature as cfeature
import cartopy.io.img_tiles as cimgt
import matplotlib.patches as mpatches
import matplotlib.ticker as mticker
import shapely

if __name__ == '__main__':

    #stn = pd.read_csv('obs_station.csv')
    lat = 23.99
    lon = 121.62
    lat2 = 25.0728
    lon2 = 121.7728
    gd = Geodesic()
    stamen_terrain = cimgt.Stamen('terrain-background')

    # This is long-lat coordinate system for use in ..
    # .. coordinate transformation options
    src_crs = ccrs.LambertConformal()
    #src_crs = ccrs.NearsidePerspective(central_longitude=121.0, central_latitude=25.0, satellite_height=35785831)

    lcc = ccrs.LambertConformal(central_longitude=121., central_latitude=23.5,standard_parallels=(10, 40))
    #lcc = ccrs.NearsidePerspective(central_longitude=121.0, central_latitude=25.0, satellite_height=35785831)
    fig = plt.figure(figsize=(7,7))
    ax = fig.add_subplot(111, projection=lcc)
    geoms = []
    shape_project=ccrs.PlateCarree()
    
    ax.add_image(stamen_terrain, 5)
    ax.set_extent([99.8954,142.405,5.366,41.5538], crs=ccrs.PlateCarree())
    ax.coastlines(lw=1, color='k')
    #shp = shapereader.Reader("D:\Program Files\MATLAB\R2019b\\toolbox\m_map\gadm41_TWN_shp\gadm41_TWN_0")
    #for record, geometry in zip(shp.records(), shp.geometries()):
    #    ax.add_geometries([geometry], shape_project,facecolor="none",
    #              edgecolor='black',lw=0.5)
    
    lat_corners = np.array([15.5066,  15.5066, 31.1679, 31.1679])
    lon_corners = np.array([ 112.426, 128.425, 129.44,111.102 ])
    
    poly_corners = np.zeros((len(lat_corners), 2), np.float64)
    poly_corners[:,0] = lon_corners
    poly_corners[:,1] = lat_corners
    
    poly = mpatches.Polygon(poly_corners, closed=True, ec='k', fill=False, lw=2, fc=None, transform=ccrs.Geodetic())
    ax.add_patch(poly)  
    
    lat_corners = np.array([18.8978,  18.8978, 28.1668,  28.1668])
    lon_corners = np.array([ 115.907, 125.565, 125.919,115.512 ])
    
    poly_corners = np.zeros((len(lat_corners), 2), np.float64)
    poly_corners[:,0] = lon_corners
    poly_corners[:,1] = lat_corners
    
    poly = mpatches.Polygon(poly_corners, closed=True, ec='k', fill=False, lw=2,zorder=2.5, fc=None, transform=ccrs.Geodetic())
    ax.add_patch(poly)  

    
    plt.text(98, 39, 'd01',
         horizontalalignment='right',fontsize=12,fontweight='bold',
         transform=ccrs.Geodetic())
    plt.text(115, 30, 'd02',
         horizontalalignment='right',fontsize=12,fontweight='bold',
         transform=ccrs.Geodetic())
    plt.text(119, 27, 'd03',
         horizontalalignment='right',fontsize=12,fontweight='bold',
         transform=ccrs.Geodetic())
    
    plt.scatter(lon2,lat2,color="r", s=20,marker='s',
        #s=statewise_store_count.Count,
        alpha=1, zorder=2.5,
        transform=ccrs.PlateCarree())
    plt.scatter(120.9072,24.8189,color="r", s=20,marker='s',
        #s=statewise_store_count.Count,
        alpha=1, zorder=2.5,
        transform=ccrs.PlateCarree())
    plt.scatter(120.0858,23.1467,color="r", s=20,marker='s',
        #s=statewise_store_count.Count,
        alpha=1, zorder=2.5,
        transform=ccrs.PlateCarree())
    plt.scatter(121.0140,24.8281,color="r", s=20,marker='s',
        #s=statewise_store_count.Count,
        alpha=1, zorder=2.5,
        transform=ccrs.PlateCarree())
    
    plt.text(125.5, 25, 'RCWF',
        horizontalalignment='right',fontsize=8,fontweight='bold',
        transform=ccrs.Geodetic())
    
    circle_points = cartopy.geodesic.Geodesic().circle(lon=lon2, lat=lat2, radius=460000, endpoint=False)
    geom = shapely.geometry.Polygon(circle_points)
    #ax.add_geometries((geom,), crs=cartopy.crs.PlateCarree(), facecolor='none', hatch='xx', edgecolor='brown', linewidth=3)
    ax.add_geometries((geom,), crs=cartopy.crs.PlateCarree(), facecolor='gray', edgecolor='k',alpha=0.3, linewidth=3)
    
    #plt.text(125.5, 25, 'RCWF',
    #    horizontalalignment='right',fontsize=8,fontweight='bold',
    #    transform=ccrs.Geodetic())
    
    circle_points = cartopy.geodesic.Geodesic().circle(lon=120.9072, lat=24.8189, radius=460000, endpoint=False)
    geom = shapely.geometry.Polygon(circle_points)
    #ax.add_geometries((geom,), crs=cartopy.crs.PlateCarree(), facecolor='none', hatch='++', edgecolor='brown', linewidth=3)
    ax.add_geometries((geom,), crs=cartopy.crs.PlateCarree(), facecolor='gray', edgecolor='k',alpha=0.3, linewidth=3)
    
    circle_points = cartopy.geodesic.Geodesic().circle(lon=120.0858, lat=23.1467, radius=460000, endpoint=False)
    geom = shapely.geometry.Polygon(circle_points)
    #ax.add_geometries((geom,), crs=cartopy.crs.PlateCarree(), facecolor='none', hatch='++', edgecolor='brown', linewidth=3)
    ax.add_geometries((geom,), crs=cartopy.crs.PlateCarree(), facecolor='gray', edgecolor='k',alpha=0.3, linewidth=3)

#'//', '\\\\', '||', '--', '++', 'xx', 'oo', 'OO', '..', '**']

    g1=ax.gridlines(draw_labels=True, dms=True, x_inline=False, y_inline=False, color='gray',linestyle='--')
    g1.top_labels=False
    g1.right_labels=False 
    g1.xlocator = mticker.FixedLocator([105,110,115,120,125,130,135,140])
    g1.ylocator = mticker.FixedLocator([5,10,15,20,25,30,35,40,45])
    g1.xlabel_style = {'size': 12, 'color': 'black'}
    g1.ylabel_style = {'size': 12, 'color': 'black'}
    
    plt.title("20180908 domain configuration", fontsize=15,fontweight='bold')
    #plt.savefig("K:\\201809rain\\thesis\\python20180908domainconfigurationcombine",dpi=300)

    plt.show()