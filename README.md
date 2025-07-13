# Carleton AI Society Documentation

This repository contains the documentation for the Carleton AI Society.

## Local Development

1. Install MkDocs:
   ```bash
   pip install mkdocs mkdocs-material
   ```

2. Run the development server:
   ```bash
   mkdocs serve
   ```

3. View the documentation at http://localhost:8000

## CuMind Documentation Sync

This repository automatically syncs documentation from the [CuMind repository](https://github.com/carletonai/CuMind). The sync happens:
- Every 6 hours automatically
- On push to main branch
- When manually triggered via GitHub Actions

To manually sync locally:
```bash
python3 scripts/sync-cumind-docs.py
```

## TODO

- Add pages/issues
- This readme (for local dev)
