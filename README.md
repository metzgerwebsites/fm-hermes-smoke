# fm-hermes-smoke

Disposable smoke project for firstmate Hermes port acceptance tests.

## Tests

The suite is stdlib `unittest` only, with no third-party dependencies and no install step.

Run it from the repository root:

```sh
./run_tests.sh
```

Or run the same discovery command directly:

```sh
python3 -m unittest discover -s tests -v
```
