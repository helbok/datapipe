# datapipe/errors.py

class DataPipeError(Exception):
    """Base class for all datapipe errors."""


class ValidationError(DataPipeError):
    """Raised when a value fails schema or rule validation."""


class SchemaError(DataPipeError):
    """Raised when a schema is malformed or inconsistent."""


class PipelineError(DataPipeError):
    """Raised when a pipeline is constructed or executed incorrectly."""


class StepNotFoundError(PipelineError):
    """Raised when a named step cannot be resolved."""


class SourceError(DataPipeError):
    """Raised when a data source cannot be read."""


class SinkError(DataPipeError):
    """Raised when a data sink cannot be written."""


class ConfigurationError(DataPipeError):
    """Raised for invalid configuration values."""


class RegistryError(DataPipeError):
    """Raised when the step registry is misused."""
