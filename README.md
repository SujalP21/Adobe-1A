# PDF Outline Extractor – Adobe Hackathon 1A

## Overview
This solution provides a robust, generic, and offline PDF outline extractor for the Adobe India Hackathon Problem 1A. It processes all PDF files in a specified input directory and generates corresponding JSON outline files in an output directory, strictly following the required schema and handling all edge cases (forms, event/flyer, technical, RFP, pathways, large/complex PDFs).

## Features
- **Generic & Non-Hardcoded:** No filename-based logic; all extraction is content-based.
- **Offline & Lightweight:** No external ML models; only PyMuPDF, langdetect, and standard Python libraries.
- **Strict Schema Compliance:** Output matches the required JSON schema for all document types.
- **Edge Case Handling:** Special logic for forms, event/flyer, technical, RFP, pathways, and large/complex PDFs.
- **Multilingual Support:** Automatically detects the document language and applies heading detection for English and Spanish (template for further languages). English logic is preserved for all current outputs.
- **Fast:** Efficient block-level extraction for quick processing, even for large PDFs.

## Directory Structure
```
├── Dockerfile
├── main.py
├── requirements.txt
├── input/
│   └── <your PDFs here>
├── output/
│   └── <generated JSONs>
```

## How to Build and Run (Docker)

### 1. Build the Docker Image
```
docker build --platform linux/amd64 -t mysolutionname:somerandomidentifier .
```

### 2. Run the Solution
```
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none mysolutionname:somerandomidentifier
```
- **Note:** On Windows PowerShell, use `${PWD}` instead of `$(pwd)`.

### 3. Output
- For every `filename.pdf` in `/app/input`, a `filename.json` will be created in `/app/output`.
- Output strictly follows the required schema:
  ```json
  {
    "title": "<document title>",
    "outline": [
      { "level": "H1", "text": "...", "page": 0 },
      ...
    ]
  }
  ```

## File Descriptions
- `main.py`: Main extraction script. Processes all PDFs in `/app/input` and writes JSONs to `/app/output`. Handles multilingual documents (English, Spanish, and template for more).
- `requirements.txt`: Python dependencies (PyMuPDF, langdetect).
- `Dockerfile`: Containerizes the solution for reproducible, isolated execution.
- `input/`: Place your PDF files here (mounted as a volume).
- `output/`: Extracted JSON outlines will appear here (mounted as a volume).

## Notes
- No internet/network access is required or used by the container.
- The solution is robust to all edge cases and document types as per the hackathon requirements.
- Multilingual support: English (full), Spanish (basic demo), and template for further languages. English outputs are unchanged.
- If you wish to run locally (without Docker), ensure you have Python 3.11+ and install dependencies with `pip install -r requirements.txt`.

## Contact
For any issues or clarifications, please refer to the code comments or contact the author.
