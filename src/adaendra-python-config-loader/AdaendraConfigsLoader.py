import os
import yaml
from AdaendraConfigs import AdaendraConfigs

config_folder = "./app/resources"  # TODO : Constantes
if os.getenv('CONFIG_FOLDER') is not None:
    config_folder = os.getenv('CONFIG_FOLDER')

config_project_name = "application" # TODO : Constantes
if os.getenv('CONFIG_PROJECT_NAME') is not None:
    config_project_name = os.getenv('CONFIG_PROJECT_NAME')

config_file_extension = ".yaml" # TODO : Constantes
if os.getenv('CONFIG_FILE_EXTENSION') is not None:
    config_file_extension = os.getenv('CONFIG_FILE_EXTENSION')

config_environment = None # TODO : Constantes
if os.getenv('CONFIG_ENVIRONMENT') is not None:
    config_environment = os.getenv('CONFIG_ENVIRONMENT')


def get_file_list() -> list:
    # The common config file
    file_list = [config_folder + "/" + config_project_name + config_file_extension]

    # The environment config file
    if config_environment is not None:
        file_list.append(config_folder + "/" + config_project_name + "-" + config_environment + config_file_extension)

    return file_list


def load_configs():
    config_dict = {}
    for file_path in get_file_list():
        try:
            with open(file_path) as file:
                # The FullLoader parameter handles the conversion from YAML
                # scalar values to Python the dictionary format
                tmp_config_dict = yaml.load(file, Loader=yaml.FullLoader)

                config_dict = config_dict | tmp_config_dict
        except FileNotFoundError:
            print('File not found : ' + file_path)

    AdaendraConfigs(config_dict)


if __name__ == "__main__":
    load_configs()
