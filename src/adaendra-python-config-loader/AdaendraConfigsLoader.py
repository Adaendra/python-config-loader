import yaml
from AdaendraConfigs import AdaendraConfigs

# TODO :
# - [ ] create a config loader
# - [ ] make sure its executed on start python project
# - [ ] make default value on the project files to load and their type
# - [ ] let some env variable available to update project files to load and their type
# - [ ] Faire en sorte qu'on puisse charger les fichiers comme dans Spring (application.yaml par défaut, application-env.yaml si il y a un environnement de défini...)


def load_configs():
    config_dict = {}
    with open('../../tests/test.yaml') as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        tmp_config_dict = yaml.load(file, Loader=yaml.FullLoader)

        config_dict = config_dict | tmp_config_dict

    print(config_dict)
    AdaendraConfigs(config_dict)

    #print('>>>>>>>>>>>')
    print(AdaendraConfigs.configs.abc)


if __name__ == "__main__":
    load_configs()
