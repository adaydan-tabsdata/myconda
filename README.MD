# td-sync

A tiny helper that **registers/updates your Tabsdata functions** without boilerplate.

Drop `sync_with_server()` into any publisher/transformer file, call it once, and it will:

- Connect to your Tabsdata server
- List existing collections (pick by number) or create a new one
- Detect the Tabsdata-decorated function in the **calling file** (prefers a function named after the file; otherwise prompts)
- Build the proper `--path` (`/abs/path/to/your_file.py::your_func`)
- **Register** or **update** the function

---

## Install (from GitHub)

```bash
pip install git+https://github.com/adaydan-tabsdata/td-sync.git
