# Vertical Slice Placeholder Tracker

This file keeps track of the blank methods added while the project is being reorganized into feature-oriented slices.

## Priority order
- P1: import flow safety, validation, and tests
- P2: copy/delete file handling, drag-and-drop, file dialog import, and threading
- P3: duplicate detection, disk removal policy, and optional `library.index` / database indexing

## Current placeholders
- `src/core/main_window.py`
  - main window shell class is intentionally empty
- `src/features/library_manager/library_panel.py`
  - library UI component class is intentionally empty
- `src/features/playlist_manager/playlist_panel.py`
  - playlist UI component class is intentionally empty
- `src/features/music_player/player_bar.py`
  - player bar UI component class is intentionally empty
- `src/features/library_manager/library.py`
  - `import_files(file_paths)`
  - `remove_song_from_disk(song)`
  - `validate_import(file_path)`
  - `is_duplicate(file_path)`
  - `search_songs(query)`
  - `filter_songs(predicate)`
  - `sort_songs(key=None, reverse=False)`
- `src/features/library_manager/file_handler.py`
  - `copy_into_music_folder(source_path)`
  - `delete_from_music_folder(file_path)`
  - `get_safe_target_path(source_path)`
  - `calculate_checksum(file_path)`
- `src/features/library_manager/metadata_parser.py`
  - `validate_import(file_path)` (extracted from `Library` so parsing/validation can evolve separately)
- `src/features/playlist_manager/playlist.py`
  - `sort_songs(key=None, reverse=False)`
- `src/features/music_player/audio_manager.py`
  - `skip_next()`
  - `skip_previous()`

## Notes on unfamiliar tasks
- Drag-and-drop and file-dialog import can both feed the same `import_files(...)` method.
- Threads are useful for file copying and metadata parsing so the UI does not freeze.
- Duplicate detection can start simple with filename checks and later move to checksum-based comparison.
- `library.index` would be a lightweight lookup structure or saved index, not necessarily a full database.
- `MetadataParser.validate_import(...)` now owns import validation/parsing checks and can evolve into richer format-specific parsing later.
- Tests should focus first on library import/search behavior and file-handler helpers.

## Notes
- These are intentionally left as blanks for later implementation.
- The moved modules keep their existing class names so the refactor stays focused on structure first.