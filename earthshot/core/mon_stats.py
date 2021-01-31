import ee

month_numbers = [ii + 1 for ii in range(12)]
## ee dictionaries are sorted, so this motivates the leading 2digit number
month_names = [
    "01_Jan",
    "02_Feb",
    "03_Mar",
    "04_Apr",
    "05_May",
    "06_Jun",
    "07_Jul",
    "08_Aug",
    "09_Sep",
    "10_Oct",
    "11_Nov",
    "12_Dec",
]


def months_list():
    return ee.List(month_numbers)


def months_dict():
    return ee.Dictionary(dict(zip(month_names, month_numbers)))


# monthly averages for each band
def bands_avgs(bands, img_col):
    # Iterands
    ee_bands = ee.Dictionary(dict(zip(bands, bands)))

    # This one is not very useful as a dictionary as the
    # information is encoded in the object anyway, but do it
    # that way for consistency. Use values() to recover a list.
    # The default sorting by key is annoying
    # ee_months = ee.List.sequence(1, 12)
    ee_months = months_dict()

    # Iterators
    # Monthly averages
    def band_avgs(band_key, band):
        def mon_avg(month_key, month):
            img_mon = img_band.filter(ee.Filter.calendarRange(month, month, "month"))
            img_mon_mean = img_mon.mean().set("month", month).set("band", band)
            img_mon_len = img_mon.size()
            return img_mon_mean

        img_band = img_col.select([band])
        mon_avgs = ee.ImageCollection.fromImages(
            ee_months.map(mon_avg).values().flatten()
        )
        return ee.ImageCollection(mon_avgs)

    # What is the sample size? == len
    def band_lens(band_key, band):
        def mon_len(month_key, month):
            return img_band.filter(
                ee.Filter.calendarRange(month, month, "month")
            ).size()

        img_band = img_col.select([band])
        mon_lens = ee_months.map(mon_len).values().flatten()
        return mon_lens

    # the iteration
    bands_avgs = ee_bands.map(band_avgs)
    bands_lens = ee_bands.map(band_lens)

    return {"avgs": bands_avgs, "lens": bands_lens}
