import pytest
import utils.save_model as save_model
from experiments.hyperparameter_tuning import fine_tune_cnn_simple, fine_tune_vgg19_simple


def dummy_save_model(*args, **kwargs):
    pass


@pytest.mark.slow
def test_hyperparameter_tuning_cnn(monkeypatch):
    dummy_dict= {'model_number': 1,
                'learning_rate': [2e-5],
                'optimizer': ['rmsprop'],
                'epochs': [1]}

    monkeypatch.setattr(save_model, 'save_model', dummy_save_model, raising=True)

    assert fine_tune_cnn_simple(dummy_dict) == 0


@pytest.mark.slow
def test_hyperparameter_tuning_vgg19(monkeypatch):
    dummy_dict = {'model_number': 1,
                  'learning_rate': [1e-4],
                  'optimizer': ['rmsprop'],
                  'epochs': [1],
                  'first_trainable_block': [5],
                  'fine_tune_learning_rate': [1e-4],
                  'fine_tune_epochs': [1]}

    monkeypatch.setattr(save_model, 'save_model', dummy_save_model, raising=True)

    assert fine_tune_vgg19_simple(dummy_dict) == 0
