# -*- coding: utf-8 -*-
import logging
from pathlib import Path

import kaggle

KAGGLE_DATASET = 'wordsforthewise/lending-club'


def main(project_path):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')

    # download the file and unzip using the Kaggle API
    dataset_path = project_path / 'data' / 'raw'
    kaggle.api.dataset_download_files(KAGGLE_DATASET, dataset_path,
                                  quiet=False, unzip=True)


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    main(project_dir)
