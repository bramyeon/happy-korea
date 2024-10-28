# Korean Happiness Score: Analysis, Interpretation, and Modeling with Extended Features
__SICSS-Korea 2024 Team Project Extension__  
Bryan Nathanael Wijaya<sup>1</sup>, Ju Hee Jeung<sup>2,3,4</sup>, Kyungmin Lee<sup>5</sup>, and Yumi Park<sup>2</sup> *(in ABC order)*  

<sup>1</sup> School of Computing, Korea Advanced Institute of Science and Technology (KAIST)  
<sup>2</sup> Korea Development Institute (KDI) School of Public Policy and Management  
<sup>3</sup> UNESCO International Centre for Water Security and Sustainable Management (i-WSSM)  
<sup>4</sup> Korea Water Resource Corporation (K-water)  
<sup>5</sup> Energy and Environmental Policy, University of Delaware  

## Datasets

Preprocessed datasets are made available in [this Google Drive link](https://drive.google.com/drive/folders/1aMIsi4qyBsFqeDbfwHUyE2JTEv06U1YO?usp=drive_link) due to their large file size. The original datasets are not uploaded to prevent any copyright issues. Some explanations:
- `nocat` datasets are those that exclude categorical columns, while those with no `nocat` maintain the categorical columns in one-hot vector representations.
- `shuffled` datasets have their rows shuffled randomly, while those with no `shuffled` name are not shuffled.
- `train` datasets are dedicated for model training. For `shuffled` datasets, this composes of the first 90% of the complete dataset. For non-`shuffled` datasets, this composes of the data from years 2020, 2021, and 2022.
- `test` datasets are dedicated for model inference and testing. For `shuffled` datasets, this composes of the latter 10% of the complete dataset. For non-`shuffled` datasets, this composes of the data from year 2023.
