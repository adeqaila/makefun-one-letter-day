"""One-letter entry writer.

Writes a single ASCII byte to /output/entry.txt and verifies the result.
Deterministic: every run produces the identical one-byte file.
"""

import os

ENTRY_BYTE = b"Y"
OUTPUT_PATH = "/output/entry.txt"


def verify_entry(path):
    """Fail hard unless the file at path holds exactly one byte."""
    with open(path, "rb") as fh:
        data = fh.read()
    if len(data) != 1:
        raise SystemExit(f"entry must be exactly 1 byte, got {len(data)}")
    return data


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as fh:
        fh.write(ENTRY_BYTE)
    verify_entry(OUTPUT_PATH)


if __name__ == "__main__":
    main()
