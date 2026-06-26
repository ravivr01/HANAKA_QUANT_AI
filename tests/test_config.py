from hqai.core.config import config


def test_project_name():
    assert config.project_name == "Hanaka Quant AI"


def test_version():
    assert config.version == "0.1.0"


def test_max_workers():
    assert config.max_workers == 12


def test_data_directory():
    assert config.data_dir.exists()
