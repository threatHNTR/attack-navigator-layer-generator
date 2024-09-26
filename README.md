# ATT&CK Navigator Layer Generator

This Python script generates a MITRE ATT&CK Navigator layer JSON file based on user input and a list of techniques. It enables customization of the layer's settings, including name, description, sorting, and more, and outputs a ready-to-use JSON file for ATT&CK Navigator visualization.

## Features
- **Input List of Techniques**: Provide a list of ATT&CK techniques in a text file.
- **Layer Customization**: Set the name, description, sorting method, and other layer properties.
- **User Prompts**: Interactive prompts for input and output file names, as well as optional display of technique IDs.
- **JSON Export**: Outputs the generated ATT&CK Navigator layer as a JSON file.
  
## Prerequisites
- Python 3.x

## Installation
Clone this repository:

```bash
git clone https://github.com/threatHNTR/attack-navigator-layer-generator.git
```

Navigate into the project directory:

```bash
cd attack-navigator-layer-generator
```

## Usage
Prepare a text file containing a list of ATT&CK technique IDs (one per line):

```txt
T1110
T1053
T1098
```

Run the script:

```bash
python generate_attack_json.py
```

The script will prompt you to:

- Enter the layer name.
- Optionally provide a description.
- Choose the sorting method (default is 0: ascending by technique name).
- Specify whether to show the technique IDs in the Navigator.
- Provide the input file (text file with technique IDs).
- Provide the output file name for the generated JSON.

After running the script, the generated JSON file can be used in the [MITRE ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/) to visualize your coverage.

