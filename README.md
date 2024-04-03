# Homer Service Configuration Tool README

## Overview
This tool is designed to help manage and update the Homer service configuration file. It automates the process of adding new services to the Homer dashboard.

## Prerequisites
- Python installed on your system.
- An existing Homer service configuration file (usually in YAML format).
- Basic familiarity with running Python scripts and editing YAML files.

## Installation
1. Ensure Python is installed on your machine.
2. Install the `PyYAML` library, necessary for the script. Use the following command:
```
pip install pyyaml
```

## Usage
1. Place `serviceconfig.py` in a convenient location on your computer.
2. Open a terminal or command prompt.
3. Navigate to the directory where `serviceconfig.py` is located.
4. Run the script using Python:

```
python3 serviceconfig.py
```
5. Follow the on-screen prompts to input details for the new service.

### Inputs
When running `serviceconfig.py`, you will be prompted to enter:
- **Category Name**: The name of the category under which the service will be listed (e.g., 'Apps').
- **Category Icon**: The icon for the category (leave blank for default 'fas fa-cloud').
- **Service Name**: The name of the new service.
- **URL**: The URL for the new service.
- **Logo URL or Path**: The URL or path to the logo for the new service (leave blank for default logo).
- **Tags**: Tags for the new service, separated by commas (leave blank if none).
- **Keywords**: Keywords for the new service, separated by commas (leave blank if none).

The script will update your Homer service configuration file with the provided details.

## Configuration File Path
Before running the script, make sure to update the `config_file_path` variable in `serviceconfig.py` to point to your actual Homer configuration file. Replace `'path/to/your/homer/config.yml'` with the correct path.

## Backup Your Configuration
It's advised to back up your existing Homer configuration file before running this script to prevent any accidental loss of data. Create a backup of your configuration file using this command:

```
cp path/to/your/homer/config.yml path/to/your/homer/config.yml.bkup
```
