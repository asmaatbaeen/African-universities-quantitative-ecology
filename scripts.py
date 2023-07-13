import geopandas as gpd
import matplotlib.pyplot as plt

 

def map_plot(africa_shapefile, program_df, title, fig_size=(10, 10)):
    """
    Plot the locations of quantitative statistical ecology programs in Africa on a map and save the plot.

        Inputs:
        - africa_shapefile (str): The file path to the shapefile or GeoJSON file containing African country boundaries.
        - program_df (pandas DataFrame): The DataFrame containing the program data, including latitude and longitude columns.
        - title (str): The title for the plot and filename when saving.
        - fig_size (tuple, optional): The size of the figure (plot) in inches. Default is (10, 10).

        Outputs:
        - None

    """

    # Load shapefile or GeoJSON file of African country boundaries
    africa_shapefile = africa_shapefile  # Replace with the actual file path

    longitudes = program_df["longitude"]
    latitudes = program_df["latitude"]
    # Create a GeoDataFrame from latitude and longitude values
    geometry = gpd.points_from_xy(longitudes, latitudes)
    program_gdf = gpd.GeoDataFrame(program_df, geometry=geometry)

    # Read shapefile of African country boundaries
    africa_gdf = gpd.read_file(africa_shapefile)

    # Spatial join to keep only points within Africa
    program_gdf = gpd.sjoin(program_gdf, africa_gdf, how="inner", op="within")

    # Plotting
    fig, ax = plt.subplots(figsize=fig_size)

    # Plot African country boundaries
    africa_gdf.plot(ax=ax, color="lightgray", edgecolor="black")

    # Plot quantitative statistical ecology program locations
    program_gdf.plot(ax=ax, color="red", markersize=50)

    # Set plot title and labels
    ax.set_title(title)
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")

    # Save the plot with the provided title as the filename
    filename = f"{title}.png"
    plt.savefig(filename)

    # Show the plot
    plt.show()
