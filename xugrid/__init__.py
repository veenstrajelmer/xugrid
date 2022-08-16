import pkg_resources

from . import data
from .plot import plot
from .ugrid import Ugrid1d, Ugrid2d, UgridRolesAccessor
from .ugrid_dataset import (
    UgridDataArray,
    UgridDataArrayAccessor,
    UgridDataset,
    UgridDatasetAccessor,
    concat,
    full_like,
    merge,
    ones_like,
    open_dataarray,
    open_dataset,
    open_mfdataset,
    open_zarr,
    zeros_like,
)

try:
    __version__ = pkg_resources.get_distribution(__name__).version
except pkg_resources.DistributionNotFound:
    # package is not installed
    pass
