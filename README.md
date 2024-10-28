# Korean Happiness Score: Analysis, Interpretation, and Modeling with Extended Features
__SICSS-Korea 2024 Team Project Extension__  
Bryan Nathanael Wijaya<sup>1</sup>, Ju Hee Jeung<sup>2,3,4</sup>, Kyungmin Lee<sup>5</sup>, and Yumi Park<sup>2</sup> *(in ABC order)*  

<sup>1</sup> School of Computing, Korea Advanced Institute of Science and Technology (KAIST)  
<sup>2</sup> Korea Development Institute (KDI) School of Public Policy and Management  
<sup>3</sup> UNESCO International Centre for Water Security and Sustainable Management (i-WSSM)  
<sup>4</sup> Korea Water Resource Corporation (K-water)  
<sup>5</sup> Energy and Environmental Policy, University of Delaware  

## Datasets

Preprocessed datasets are made available in [this Google Drive link](https://drive.google.com/drive/folders/1aMIsi4qyBsFqeDbfwHUyE2JTEv06U1YO?usp=drive_link) due to their large file size. The original datasets are not uploaded to prevent any copyright issues. We considered the datasets from year 2020 to 2021 only.


all_in_dict = {
    'korea-all': 309,
    'korea-complex': 142,
    'korea-medium': 86,
    'korea-basic': 59,
    'korea-simple': 40
}

There are 5 dataset versions based on the number of features considered.

- `korea-all`: All relevant Korean Happiness Survey features + 12 socioeconomic and environmental features (308 indep. feat.)
- `korea-complex`: Korean Happiness Survey features with a correlation value of at least 0.05 w.r.t. the happiness ladder + 12 socioeconomic and environmental features (141 indep. feat.)
- `korea-medium`: Korean Happiness Survey features with a correlation value of at least 0.10 w.r.t. the happiness ladder + 12 socioeconomic and environmental features (85 indep. feat.)
- `korea-base`: Korean Happiness Survey features with a correlation value of at least 0.15 w.r.t. the happiness ladder + 12 socioeconomic and environmental features (58 indep. feat.)
- `korea-simple`: Korean Happiness Survey features with a correlation value of at least 0.25 w.r.t. the happiness ladder + 12 socioeconomic and environmental features (39 indep. feat.)
