"""datapipe: a composable data transformation and pipeline library."""

from datapipe.cache import Cache
from datapipe.config import load_config, merge_config
from datapipe.core import Dataset, Graph, Node, identity
from datapipe.errors import DataPipeError, PipelineError, ValidationError
from datapipe.executor import Executor
from datapipe.metrics import Metrics, metrics
from datapipe.pipeline import Pipeline
from datapipe.registry import registry
from datapipe.schema import Field, Schema, infer_schema

__version__ = "0.6.0"

__all__ = [
    "Cache",
    "Dataset",
    "Executor",
    "Field",
    "Graph",
    "Metrics",
    "Node",
    "Pipeline",
    "Schema",
    "identity",
    "infer_schema",
    "load_config",
    "merge_config",
    "metrics",
    "registry",
    "DataPipeError",
    "PipelineError",
    "ValidationError",
    "__version__",
]
