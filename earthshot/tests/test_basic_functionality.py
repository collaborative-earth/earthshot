import ee
import json
import pytest


def test_read_public_image_col(authenticate_gee):
    assert isinstance(ee.ImageCollection("LANDSAT/LC08/C01/T1_SR"), ee.ImageCollection)


def test_read_public_feature_col(authenticate_gee):
    assert isinstance(ee.FeatureCollection("TIGER/2016/States"), ee.FeatureCollection)
