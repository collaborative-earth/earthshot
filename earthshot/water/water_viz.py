from bokeh.io import output_notebook
from bokeh.plotting import figure, output_file, show
from bokeh.palettes import brewer, colorblind
import ee
import folium
from .water_common import bboxes
from IPython.display import Image

_ = output_notebook()


def add_ee_layer(self, ee_image_object, vis_params, name):
    """A method for displaying or layering Earth Engine image tiles to folium map."""
    map_id_dict = ee.Image(ee_image_object).getMapId(vis_params)
    folium.raster_layers.TileLayer(
        tiles=map_id_dict["tile_fetcher"].url_format,
        attr='Map Data &copy; <a href="https://earthengine.google.com/">Google Earth Engine</a>',
        name=name,
        overlay=True,
        control=True,
    ).add_to(self)


# Add EE drawing method to folium.
folium.Map.add_ee_layer = add_ee_layer


def legend(
    palette: tuple,
    title: str = "Legend Title (-)",
    plot_width: int = 500,
    plot_height: int = 75,
    minimum: float = 0,
    maximum: float = 1,
) -> None:
    """Create a stand-alone legend.
    Args:
        palette: tuple of colors
        title: str for title
        plot_width: int
        plot_height: int
        minimum: float of values to include
        maximum: float of values to include
    Returns:
        None but displays a legend bar in a Jupyter Notebook.
    """
    pal_len = len(palette)
    pal_dist = maximum - minimum
    width_color = pal_dist / pal_len
    x_locs = [
        minimum + 0.5 * width_color * ((2 * ii) - 1)
        for ii in range(pal_len + 1)
        if ii != 0
    ]
    # print(width_color)
    # print(x_locs)

    legend = figure(title=title, plot_width=plot_width, plot_height=plot_height)

    _ = legend.vbar(
        x=x_locs,
        top=[0] * pal_len,
        bottom=[1] * pal_len,
        width=width_color,
        color=palette,
    )
    show(legend)
    return None


# hmpf, no real gain
def folium_map(**kwargs) -> folium.Map:
    folium_map = folium.Map(**kwargs)
    return folium_map


def folium_display(the_map) -> None:
    """Display a folium map with layer control."""
    the_map.add_child(folium.LayerControl())
    display(the_map)
    return None
