# kaggle-Backpack-Prediction-Challenge
This repo is for participating in [this](https://www.kaggle.com/competitions/playground-series-s5e2/overview) Kaggle competition.

*"**Your Goal**: Predict the price of backpacks given various attributes."*

### Evaluation
Submissions are scored on the <ins>root mean squared error (RMSE)<ins>.

For each id row in the test set, you must predict the continuous target Premium Amount. The file should contain a header and have the following format:
``` xml
id,Price
300000,81.411
300001,81.411
300002,81.411
etc.
```

## Setup
This repo uses a Conda environment configured in `environment.yml`. Here are the steps to set these up properly from this repos home folder:
1. Create an new Conda environment `conda env create -f environment.yml`
2. Activate the environment `conda activate kaggle-Backpack-Prediction-Challenge`

If changes are made to `environment.yml` then update by running `conda env update --file environment.yml --prune`

## Commiting
Please refer to the Conventional Commits specification located [here](https://www.conventionalcommits.org/en/v1.0.0/) for formatting your commit messages.

## Results
- Best Score:
- Kaggle Rank: