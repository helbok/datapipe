"""datapipe: a composable data transformation and pipeline library."""

from datapipe.config import load_config, merge_config
from datapipe.core import Dataset, Graph, Node, identity
from datapipe.errors import DataPipeError, PipelineError, ValidationError
from datapipe.executor import Executor
from datapipe.pipeline import Pipeline
from datapipe.registry import registry
from datapipe.schema import Field, Schema, infer_schema

__version__ = "0.3.0"

__all__ = [
    "Dataset",
    "Executor",
    "Field",
    "Graph",
    "Node",
    "Pipeline",
    "Schema",
    "identity",
    "infer_schema",
    "load_config",
    "merge_config",
    "registry",
    "DataPipeError",
    "PipelineError",
    "ValidationError",
    "__version__",
]
