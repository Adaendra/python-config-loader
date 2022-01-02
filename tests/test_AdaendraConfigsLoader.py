import os
from unittest import mock

from adaendra_python_config_loader import load_configs
from adaendra_python_config_loader.AdaendraConfigsLoader import get_config_folder, get_config_project_name, \
    get_config_file_extension, get_config_environment, get_file_list

from src.adaendra_python_config_loader.AdaendraConfigs import AdaendraConfigs
from src.adaendra_python_config_loader.Constants import DEFAULT_CONFIG_FOLDER, ENV_CONFIG_FOLDER, \
    DEFAULT_CONFIG_PROJECT_NAME, ENV_CONFIG_PROJECT_NAME, DEFAULT_CONFIG_FILE_EXTENSION, ENV_CONFIG_FILE_EXTENSION, \
    FILE_EXT_YAML, FILE_EXT_YML, FILE_EXT_JSON, ENV_CONFIG_ENVIRONMENT


# ----- get_config_folder ----- #
def test_get_config_folder_ok():
    result = get_config_folder()

    assert result == DEFAULT_CONFIG_FOLDER


@mock.patch.dict(os.environ, {ENV_CONFIG_FOLDER: "/src"})
def test_get_config_folder_ok_with_custom_value():
    result = get_config_folder()

    assert result == "/src"


# ----- get_config_project_name ----- #
def test_get_config_project_name_ok():
    result = get_config_project_name()

    assert result == DEFAULT_CONFIG_PROJECT_NAME


@mock.patch.dict(os.environ, {ENV_CONFIG_PROJECT_NAME: "new_project"})
def test_get_config_project_name_ok_with_custom_value():
    result = get_config_project_name()

    assert result == "new_project"


# ----- get_config_file_extension ----- #
def test_get_config_file_extension_ok():
    result = get_config_file_extension()

    assert result == DEFAULT_CONFIG_FILE_EXTENSION


@mock.patch.dict(os.environ, {ENV_CONFIG_FILE_EXTENSION: FILE_EXT_YAML})
def test_get_config_file_extension_ok_yaml():
    result = get_config_file_extension()

    assert result == FILE_EXT_YAML


@mock.patch.dict(os.environ, {ENV_CONFIG_FILE_EXTENSION: FILE_EXT_YML})
def test_get_config_file_extension_ok_yml():
    result = get_config_file_extension()

    assert result == FILE_EXT_YML


@mock.patch.dict(os.environ, {ENV_CONFIG_FILE_EXTENSION: FILE_EXT_JSON})
def test_get_config_file_extension_ok_json():
    result = get_config_file_extension()

    assert result == FILE_EXT_JSON


@mock.patch.dict(os.environ, {ENV_CONFIG_FILE_EXTENSION: ".yolo"})
def test_get_config_file_extension_nok():
    result = get_config_file_extension()

    assert result == FILE_EXT_YAML


# ----- get_config_environment ----- #
def test_get_config_environment_ok():
    result = get_config_environment()

    assert result is None


@mock.patch.dict(os.environ, {ENV_CONFIG_ENVIRONMENT: "local"})
def test_get_config_environment_ok_with_custom_value():
    result = get_config_environment()

    assert result == "local"


# ----- get_file_list ----- #
def test_get_file_list_ok():
    result = get_file_list()

    assert len(result) == 1
    assert result.__contains__(DEFAULT_CONFIG_FOLDER + "/" + DEFAULT_CONFIG_PROJECT_NAME +
                               DEFAULT_CONFIG_FILE_EXTENSION)


@mock.patch.dict(os.environ, {ENV_CONFIG_FOLDER: "/app"})
def test_get_file_list_ok_with_custom_folder():
    result = get_file_list()

    assert len(result) == 1
    assert result.__contains__("/app/" + DEFAULT_CONFIG_PROJECT_NAME + DEFAULT_CONFIG_FILE_EXTENSION)


@mock.patch.dict(os.environ, {ENV_CONFIG_PROJECT_NAME: "app"})
def test_get_file_list_ok_with_custom_project():
    result = get_file_list()

    assert len(result) == 1
    assert result.__contains__(DEFAULT_CONFIG_FOLDER + "/app" + DEFAULT_CONFIG_FILE_EXTENSION)


@mock.patch.dict(os.environ, {ENV_CONFIG_FILE_EXTENSION: ".json"})
def test_get_file_list_ok_with_custom_extension():
    result = get_file_list()

    assert len(result) == 1
    assert result.__contains__(DEFAULT_CONFIG_FOLDER + "/" + DEFAULT_CONFIG_PROJECT_NAME + ".json")


@mock.patch.dict(os.environ, {ENV_CONFIG_ENVIRONMENT: "local"})
def test_get_file_list_ok_with_custom_local():
    result = get_file_list()

    assert len(result) == 2
    assert result.__contains__(DEFAULT_CONFIG_FOLDER + "/" + DEFAULT_CONFIG_PROJECT_NAME
                               + DEFAULT_CONFIG_FILE_EXTENSION)
    assert result.__contains__(DEFAULT_CONFIG_FOLDER + "/" + DEFAULT_CONFIG_PROJECT_NAME + "-local"
                               + DEFAULT_CONFIG_FILE_EXTENSION)


@mock.patch.dict(os.environ, {ENV_CONFIG_ENVIRONMENT: "local", ENV_CONFIG_FOLDER: "/app",
                              ENV_CONFIG_PROJECT_NAME: "svc", ENV_CONFIG_FILE_EXTENSION: ".json"})
def test_get_file_list_ok_with_full_custom():
    result = get_file_list()

    assert len(result) == 2
    assert result.__contains__("/app/svc.json")
    assert result.__contains__("/app/svc-local.json")

