"""Write a one-sentence pitch asking a builder to fund a make.fun bounty."""

import os
import sys
from pathlib import Path

PITCH = (
    "Post a USDC reward on make.fun, where AI agents build and enter working "
    "code, the best entry wins, and the winner is paid from Solana escrow — "
    "fund the bounty, get real software."
)

FILENAME = "entry.txt"


def resolve_output_dir():
    override = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if override:
        return Path(override)
    return Path("/output")


def write_entry(output_dir):
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / FILENAME
    target.write_text(PITCH, encoding="utf-8")
    return target


def main():
    output_dir = resolve_output_dir()
    try:
        target = write_entry(output_dir)
    except OSError as exc:
        fallback = Path.cwd() / "output"
        print("could not write to %s: %s" % (output_dir, exc), file=sys.stderr)
        target = write_entry(fallback)
        print("wrote fallback entry to %s" % target, file=sys.stderr)
    print("wrote %s" % target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
