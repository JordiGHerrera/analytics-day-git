"""
This is a boilerplate pipeline
generated using Kedro 0.18.5
"""

import logging
from typing import Any, Dict, Tuple

import numpy as np
import pandas as pd


def filter_data(
    data: pd.DataFrame
) -> pd.DataFrame:
    """Selects only setosa observations within the iris dataset.

    Args:
        data: chosen dataset.
    Returns:
        Filtered dataset.
    """

    data_filtered = data.query("species == 'setosa'")

    return data_filtered
