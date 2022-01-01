import os
import yaml
from AdaendraConfigs import AdaendraConfigs

# TODO : Tests unitaires
# TODO : Documentation (readme et tout)
# TODO : Commentaires + ménage code


def get_config_folder() -> str:
    config_folder = "./app/resources"  # TODO : Constantes
    if os.getenv('CONFIG_FOLDER') is not None:
        config_folder = os.getenv('CONFIG_FOLDER')
    return config_folder


def get_config_project_name() -> str:
    config_project_name = "application" # TODO : Constantes
    if os.getenv('CONFIG_PROJECT_NAME') is not None:
        config_project_name = os.getenv('CONFIG_PROJECT_NAME')
    return config_project_name


def get_config_file_extension() -> str:
    config_file_extension = ".yaml" # TODO : Constantes
    if os.getenv('CONFIG_FILE_EXTENSION') is not None:
        config_file_extension = os.getenv('CONFIG_FILE_EXTENSION')
    return config_file_extension


def get_config_environment() -> str:
    config_environment = None # TODO : Constantes
    if os.getenv('CONFIG_ENVIRONMENT') is not None:
        config_environment = os.getenv('CONFIG_ENVIRONMENT')
    return config_environment


def get_file_list() -> list:
    # The common config file
    file_list = [get_config_folder() + "/" + get_config_project_name() + get_config_file_extension()]

    # The environment config file
    if get_config_environment() is not None:
        file_list.append(get_config_folder() + "/" + get_config_project_name() + "-" + get_config_environment() + get_config_file_extension())

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
