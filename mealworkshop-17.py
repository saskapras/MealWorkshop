# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: MealWorkshop
def _dry_run_mode():
    import sys, json
    if "--no-dry-run" in sys.argv: return False
    dry = "DRY_RUN" in os.environ
    if not dry and len(sys.argv) > 1 and sys.argv[1] == "--dry-run": dry = True
    if dry: print("[DRY RUN]")
    def mock_write(path, content):
        if dry:
            print(f"[SKIP WRITE] {path}")
            return False
        with open(path, "w", encoding="utf-8") as f: f.write(content)
        return True
    return mock_write
