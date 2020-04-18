import os
import pytest
import tarfile
import zipfile
import data.break_his.break_his_dataset_creation as break_his_dataset_creation
import data.nct_crc_he_100k.nct_crc_he_100k_dataset_creation as nct_crc_he_100k_dataset_creation


@pytest.mark.xfail
def test_break_his_dataset_creation(tmpdir):
    dummy_archive = os.path.join(tmpdir, 'break_his.tar.gz')
    tar = tarfile.open(dummy_archive, "w:gz")
    tar.close()
    assert break_his_dataset_creation.main(dummy_archive) == 0


@pytest.mark.xfail
def test_nct_crc_he_100k_dataset_creation(tmpdir):
    dummy_archive = os.path.join(tmpdir, 'nct_crc_he_100k.zip')
    zip = zipfile.ZipFile(dummy_archive, "w")
    zip.close()
    assert nct_crc_he_100k_dataset_creation.main(dummy_archive) == 0
