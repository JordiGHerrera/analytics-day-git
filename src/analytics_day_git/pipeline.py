"""
This is a boilerplate pipeline
generated using Kedro 0.18.5
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import filter_data


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=filter_data,
                inputs="example_iris_data",
                outputs="filtered_iris_data",
                name="filter",
            )
        ]
    )
