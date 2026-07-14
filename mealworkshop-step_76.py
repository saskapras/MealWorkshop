# === Stage 76: Add graceful keyboard interrupt handling in the CLI entry point ===
# Project: MealWorkshop
import sys


def handle_shutdown(signum, frame):
    """Gracefully exit on Ctrl+C / SIGINT."""
    print("\n\nMealWorkshop interrupted — exiting cleanly.", file=sys.stderr)
    sys.exit(0)


if __name__ == "__main__":
    import signal

    # Install a handler for keyboard interrupt (SIGINT = Ctrl+C).
    signal.signal(signal.SIGINT, handle_shutdown)

    # Optional: also catch SIGTERM if running under Docker / Kubernetes.
    try:
        signal.signal(signal.SIGTERM, handle_shutdown)
    except OSError:
        pass  # Windows ignores SIGTERM — nothing to do there

    # Now run the rest of your CLI logic normally.
    # Example (replace with your actual entry-point code):
    # from mealworkshop.cli import main
    # main()
