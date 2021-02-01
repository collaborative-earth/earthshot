import ee
import numpy as np
import scipy.special

from .. import water

bboxes = water.water_common.bboxes

from bokeh.layouts import gridplot
from bokeh.plotting import figure, output_file, show

## A different way of finding the min max. Found after the fact of the below.
## Not that different, but maybe more efficient on the server.
## https://gis.stackexchange.com/questions/313394/normalization-in-google-earth-engine
def img_range(img, area_of_interest=None, scale_m: int = 1) -> list:
    """Get the [min, max] of an image given optional
    area of interest and scale (meters)."""
    if area_of_interest is None:
        area_of_interest = bboxes()["world"]

    min = (
        img.reduceRegion(
            ee.Reducer.min(), area_of_interest, bestEffort=True, scale=scale_m
        )
        .values()
        .getInfo()
    )
    max = (
        img.reduceRegion(
            ee.Reducer.max(), area_of_interest, bestEffort=True, scale=scale_m
        )
        .values()
        .getInfo()
    )

    # probably not the best way to handle this
    if len(min) > 1 or len(max) > 1:
        raise ValueError("Passed image has multiple bands")

    return [min[0], max[0]]


def img_col_range(img_col, area_of_interest=None, scale_m: int = 1) -> list:
    """Get the [min, max] of an image Collection given optional
    area of interest and scale (meters)."""
    if area_of_interest is None:
        area_of_interest = bboxes()["world"]

    min = img_range(img_col.min(), area_of_interest)[0]
    max = img_range(img_col.max(), area_of_interest)[1]

    return [min, max]


def distribution_plot(title, hist, edges, x, pdf, cdf):
    p = figure(title=title, tools="", background_fill_color="#fafafa")
    p.quad(
        top=hist,
        bottom=0,
        left=edges[:-1],
        right=edges[1:],
        fill_color="navy",
        line_color="white",
        alpha=0.5,
    )
    p.line(x, pdf, line_color="#ff8888", line_width=4, alpha=0.7, legend_label="PDF")
    p.line(x, cdf, line_color="orange", line_width=2, alpha=0.7, legend_label="CDF")

    p.y_range.start = 0
    p.legend.location = "center_right"
    p.legend.background_fill_color = "#fefefe"
    p.xaxis.axis_label = "x"
    p.yaxis.axis_label = "Pr(x)"
    p.grid.grid_line_color = "white"
    return p


def normal_dist_plot(data, n_bins: int = 50, n_dist: int = 1000) -> None:
    # Normal Distribution
    # data = np.random.normal(mu, sigma, 1000)
    mu = np.mean(data)
    sigma = np.std(data)
    hist, edges = np.histogram(data, density=True, bins=n_bins)

    x = np.linspace(data.min(), data.max(), n_dist)
    pdf = 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-((x - mu) ** 2) / (2 * sigma ** 2))
    cdf = (1 + scipy.special.erf((x - mu) / np.sqrt(2 * sigma ** 2))) / 2 * hist.max()

    title = "Normal Distribution (μ=" + str(mu) + ", σ=" + str(sigma) + ")"
    p1 = distribution_plot(title, hist, edges, x, pdf, cdf)
    show(p1)
    return None


def img_scale(img, min=None, max=None, area_of_interest=None, scale_m: int = 1):
    if min is None or max is None:
        min_max_list = img_range(
            img, area_of_interest=area_of_interest, scale_m=scale_m
        )
        if min is None:
            min = min_max_list[0]
        if max is None:
            max = min_max_list[1]
    img_scaled = img.unitScale(ee.Number(min), ee.Number(max))
    return img_scaled
