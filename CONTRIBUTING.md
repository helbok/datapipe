# Contributing

Thanks for your interest in contributing to `datapipe`. This project is a
synthetic educational example, but the same workflow applies to any real
project.

## Workflow

1. Open an issue describing the bug or feature.
2. Create a branch from `main`.
3. Make focused, atomic commits with conventional messages.
4. Add or update tests for any behaviour change.
5. Open a pull request and keep it small.

## Commit messages

Use the [Conventional Commits](https://www.conventionalcommits.org/) format:

- `feat:` new behaviour
- `fix:` a bug fix
- `refactor:` code restructuring with no behaviour change
- `test:` adding or changing tests
- `docs:` documentation only
- `build:` dependency and packaging changes
- `ci:` continuous-integration changes

## Testing

```console
$ pip install -e ".[test]"
$ pytest
```

