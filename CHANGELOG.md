# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [0.3.0] - 2020-12-01

### Added

- JSON configuration helpers.
- Package exports for executor and config.

### Changed

- Unified source and sink factory dispatch.


## [0.2.0] - 2020-10-12

### Added

- HTTP source (requests).
- SQL source (SQLAlchemy).
- Parquet sink (pyarrow).
- Parallel branch executor.

### Fixed

- Blank rows are no longer emitted by CSV sources.


## [0.1.0] - 2020-02-26

### Added

- Lazy graph execution (Node, Dataset, Graph).
- Pipeline builder with map, filter, select, aggregate and sort.
- CSV and JSON sources and sinks.
- Schema model with inference and validation.

