#!/usr/bin/env python3
"""Build a deterministic, verified Clink catalog for this collection."""
import hashlib
import json
import os
from pathlib import Path

root = Path(__file__).resolve().parents[1]
repository = os.environ.get("GITHUB_REPOSITORY", "stivy73/clink-duo")
inputs = []
for folder, extension, collection, limit in [("Layouts", ".clinklayout", "layouts", 512000), ("Themes", ".clinktheme", "themes", 128000), ("Profiles", ".clinkprofile", "profiles", 256000)]:
    for file in sorted((root / folder).glob("*" + extension)):
        raw = file.read_bytes()
        data = json.loads(raw)
        if collection == "profiles":
            # Native profile exports use a config envelope, without catalog metadata.
            assert data.get("clinkPackage") == 1 and data.get("kind") == "config", file
            data = {"id": file.stem, "name": file.stem.replace("-", " ").title()}
        else:
            assert data.get("name") and data.get("id"), file
        assert 0 < len(raw) <= limit, file
        inputs.append((file, raw, data, collection))
# Include the portable automation in the release identity too.
automation = root / "Automations/duo-automation.json"
identity = [(file.name, hashlib.sha256(raw).hexdigest()) for file, raw, _, _ in inputs]
identity.append((automation.name, hashlib.sha256(automation.read_bytes()).hexdigest()))
version = "duo-" + hashlib.sha256(json.dumps(identity, separators=(",", ":")).encode()).hexdigest()[:20]
manifest = {"version": version, "layouts": [], "themes": [], "profiles": []}
for file, raw, data, collection in inputs:
    manifest[collection].append({"id": file.stem, "name": data["name"], "version": version, "platform": "ios", "asset": {"path": file.name, "url": f"https://github.com/{repository}/releases/download/{version}/{file.name}", "sha256": hashlib.sha256(raw).hexdigest(), "byteCount": len(raw)}})
(root / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
print(version)
