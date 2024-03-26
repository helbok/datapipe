# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [1.3.0] - 2024-03-26

### Added

- Atomic file-write helper.
- Batching step.

### Changed

- JSON sinks now write atomically.


## [1.2.0] - 2023-08-28

### Added

- DOT export tests.

### Changed

- Dependency updates.

### Fixed

- Window step no longer mutates caller rows.


## [1.1.0] - 2023-05-12

### Added

- Windowed aggregation step.
- Graphviz DOT export.

### Changed

- Sort keys are now keyword-only.


## [1.0.0] - 2022-09-27

### Added

- Stable 1.0 API.

### Changed

- Polished factory dispatch and documentation.

### Fixed

- Deduplicate is stable for unhashable values.


## [0.6.0] - 2022-07-18

### Added

- Deduplicate and union steps.
- Scalar coercion helpers.

### Changed

- JSON sinks now use orjson when available.


## [0.5.0] - 2021-11-01

### Added

- Coverage reporting wired into the test suite.

### Changed

- Dependency updates across the board.

### Fixed

- Registry reports duplicate names clearly.


## [0.4.0] - 2021-09-08

### Added

- Disk-backed stage cache.
- Counters and timers.
- Built-in steps registered in the registry.
- CLI `nodes` command with rich output.

### Changed

- CI now reports coverage.


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

