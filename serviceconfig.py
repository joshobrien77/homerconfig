import yaml

def read_yaml_config(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def write_yaml_config(file_path, config):
    with open(file_path, 'w') as file:
        yaml.dump(config, file, sort_keys=False)

def find_or_create_category(config, category_name, category_icon):
    for category in config['services']:
        if category.get("name") == category_name:
            return category
    # If category not found, create it
    new_category = {"name": category_name, "icon": category_icon, "items": []}
    config['services'].append(new_category)
    return new_category

def add_service_to_config(file_path):
    # Collecting input for category and service
    category_name = input("Enter the category name (e.g., 'Apps'): ")
    category_icon = input("Enter the category icon (leave blank for default 'fas fa-cloud'): ")
    category_icon = category_icon if category_icon else "fas fa-cloud"

    service_name = input("Enter the service name: ")
    url = input("Enter the URL: ")
    logo = input("Enter the logo URL or path (leave blank for default logo): ")
    logo = logo if logo else "assets/tools/sample2.png"
    tags = input("Enter tags (comma-separated, leave blank if none): ").split(',')
    tags = None if tags == [''] else tags
    keywords = input("Enter keywords (comma-separated, leave blank if none): ").split(',')
    keywords = None if keywords == [''] else keywords

    # Read the existing configuration
    config = read_yaml_config(file_path)

    # Make sure 'services' key exists
    if 'services' not in config:
        config['services'] = []

    # Find the category or create a new one
    category = find_or_create_category(config, category_name, category_icon)

    # Creating the configuration dictionary for the new service
    new_service = {
        "name": service_name,
        "url": url,
        "logo": logo,
        "tags": tags,
        "keywords": keywords
    }

    # Add the new service to the category
    category['items'].append(new_service)

    # Write the updated configuration back to the file
    write_yaml_config(file_path, config)
    print("Configuration updated successfully!")

# Path to your Homer configuration file
config_file_path = 'path/to/your/homer/config.yml'
add_service_to_config(config_file_path)
