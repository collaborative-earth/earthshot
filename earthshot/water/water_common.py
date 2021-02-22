import ee


def bboxes() -> dict:
    """A dictionary of common bounding boxes."""
    return {
        "n_america": ee.Geometry.BBox(-178.2, 6.6, -49.0, 83.3),
        "world": ee.Geometry.BBox(-180.0, -90, 180, 90),
        "conus": ee.Geometry.BBox(-124.8, 24.8, -67.0, 49.4),
        "roi_or_1": ee.Geometry.BBox(-124.1, 42.88, -123.6, 43.38),
        "neom": ee.Geometry.BBox(34.52778, 27.72417, 35.96528, 29.14139),
    }
