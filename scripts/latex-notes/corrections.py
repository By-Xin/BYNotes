"""Apply a reviewed, source-hash-bound correction ledger without editing originals."""
import hashlib


def apply_corrections(raw, ledger):
    if hashlib.sha256(raw.encode()).hexdigest() != ledger["source_sha256"]:
        raise ValueError("Source changed: review/rebase the correction ledger before rebuilding")
    corrected = raw
    for entry in ledger["changes"]:
        before, after = entry["before"], entry["after"]
        if not before or before == after or corrected.count(before) != entry.get("count", 1):
            raise ValueError(f"Correction context mismatch: {entry['id']}")
        corrected = corrected.replace(before, after)
    return corrected
