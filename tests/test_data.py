import os
import pytest
import tarfile
import zipfile
import data.break_his.break_his_dataset_creation as break_his_dataset_creation
from data.break_his.break_his_dataset_creation import benign, malignant
import data.nct_crc_he_100k.nct_crc_he_100k_dataset_creation as nct_crc_he_100k_dataset_creation


def create_breakhis_dummy_archive(tmpdir):
    benign_dir = os.path.join(tmpdir, 'BreaKHis_v1/histology_slides/breast/benign/SOB/')
    for cancer_subtype in benign:
        os.makedirs(os.path.join(benign_dir, cancer_subtype))
    malignant_dir = os.path.join(tmpdir, 'BreaKHis_v1/histology_slides/breast/malignant/SOB/')
    for cancer_subtype in malignant:
        os.makedirs(os.path.join(malignant_dir, cancer_subtype))
    dummy_archive = os.path.join(tmpdir, 'break_his.tar.gz')
    with tarfile.open(dummy_archive, "w:gz") as tar:
        for cancer_subtype in benign:
            tar.add(os.path.join(benign_dir, cancer_subtype))
        for cancer_subtype in malignant:
            tar.add(os.path.join(malignant_dir, cancer_subtype))
    return dummy_archive


def test_break_his_dataset_creation(tmpdir):
    dummy_archive = create_breakhis_dummy_archive(tmpdir)
    assert break_his_dataset_creation.main(dummy_archive, tmpdir) == 0


def create_nctcrche100k_dummy_archive(tmpdir):
    nct_crc_he_100k_dir = os.path.join(tmpdir, 'NCT-CRC-HE-100K')
    os.makedirs(nct_crc_he_100k_dir)
    dummy_archive = os.path.join(tmpdir, 'nct_crc_he_100k.zip')
    zip = zipfile.ZipFile(dummy_archive, "w")
    zip.write(nct_crc_he_100k_dir)
    zip.close()
    return dummy_archive


def test_nct_crc_he_100k_dataset_creation(tmpdir):
    dummy_archive = create_nctcrche100k_dummy_archive(tmpdir)
    assert nct_crc_he_100k_dataset_creation.main(dummy_archive, tmpdir) == 0
