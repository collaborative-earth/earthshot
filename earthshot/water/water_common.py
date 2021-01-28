import ee


def bboxes():
    return {
        'n_america': ee.Geometry.BBox(-178.2, 6.6, -49.0, 83.3),
        'world': ee.Geometry.BBox(-180.0, -90, 180, 90),
        'conus': ee.Geometry.BBox(-124.8, 24.8, -67.0, 49.4)}