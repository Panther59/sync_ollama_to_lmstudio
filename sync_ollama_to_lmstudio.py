import os
import shutil
import json
from pathlib import Path

# Prompt user for base and target directories
base_dir = Path(input("Enter the base directory (e.g., F:/ollama_models): ").strip())
publicmodels_dir = Path(input("Enter the target directory for LM Studio models (e.g., F:/Models/llm_studio): ").strip())

manifest_dir = base_dir / "manifests/registry.ollama.ai"
blob_dir = base_dir / "blobs"

# Remove existing files in the public models directory
if publicmodels_dir.exists():
    shutil.rmtree(publicmodels_dir)
publicmodels_dir.mkdir(parents=True, exist_ok=True)

print("Starting iteration...")
print(f"Manifest directory: {manifest_dir}")

# Traverse all 'latest' files recursively in manifest directory
for latest_file in manifest_dir.rglob("latest"):
    print(f"Processing: {latest_file}")

    # Extract user, model, tag from path
    try:
        parts = latest_file.parts
        registry_index = parts.index("registry.ollama.ai")
        user = parts[registry_index + 1]
        model = parts[registry_index + 2]
        tag = parts[registry_index + 3]

            # Load JSON and extract digest with mediaType
        try:
            with open(latest_file, "r") as f:
                data = json.load(f)

            digest = None
            for layer in data.get("layers", []):
                if layer.get("mediaType") == "application/vnd.ollama.image.model":
                    digest = layer.get("digest")
                    break

            if not digest:
                print(f"No valid digest found in {latest_file}")
                continue

            digest = digest.replace("sha256:", "")

            # Create destination directory and create a symlink to the blob
            dest_dir = publicmodels_dir 
            dest_dir.mkdir(parents=True, exist_ok=True)

            blob_path = blob_dir / f"sha256-{digest}"
            symlink_path = dest_dir / user/ model/ f"{model}-{tag}.gguf"
            symlink_path.parent.mkdir(parents=True, exist_ok=True)

            if blob_path.exists():
                if not symlink_path.exists():
                    print(f"Creating symlink: {symlink_path}")
                    os.symlink(blob_path, symlink_path)
            else:
                print(f"Blob file not found: {blob_path}")


        except Exception as e:
            print(f"Error processing {latest_file}: {e}")

    except (IndexError, ValueError):
        print(f"Skipping malformed path: {latest_file}")
        continue

