# Korean Happiness Score: Analysis, Interpretation, and Modeling with Extended Socioeconomic and Environmental Features
__SICSS-Korea 2024 Team Project Extension__  
Bryan Nathanael Wijaya<sup>a,b</sup>, Yumi Park<sup>c</sup>, Ju Hee Jeung<sup>c</sup>, Kyungmin Lee<sup>d,</sup>*  

<sup>a</sup> School of Computing, Korea Advanced Institute of Science and Technology (KAIST), Daejeon, South Korea  
<sup>b</sup> Max Planck Institute of Security and Privacy (MPI-SP), Bochum, Germany  
<sup>c</sup> Korea Development Institute (KDI) School of Public Policy and Management, Sejong, South Korea  
<sup>d</sup> Biden School of Public Policy and Administration, University of Delaware, Newark, DE, USA  
\* Corresponding author ([kmlee@udel.edu](mailto:kmlee@udel.edu))  

## Remarks

The original datasets have not been uploaded to prevent any potential copyright issues. Only the preprocessed test split examples are made available here to accommodate the analysis of happiness ladder factors in the `analysis.ipynb` notebook and the SHAP analysis in the `shap.ipynb` notebook. You can run the Jupyter Notebooks directly in Google Colab. Note that we considered the datasets from 2020 to 2021 only.

There are 5 dataset versions based on the number of features considered.

- `korea-all`: All relevant Korean Happiness Survey (KHS) features + 12 socioeconomic and environmental (SE) features (308 indep. feat.)
- `korea-complex`: KHS features with a correlation value of at least 0.05 w.r.t. the happiness ladder + 12 SE features (141 indep. feat.)
- `korea-medium`: KHS features with a correlation value of at least 0.10 w.r.t. the happiness ladder + 12 SE features (85 indep. feat.)
- `korea-base`: KHS features with a correlation value of at least 0.15 w.r.t. the happiness ladder + 12 SE features (58 indep. feat.)
- `korea-simple`: KHS features with a correlation value of at least 0.25 w.r.t. the happiness ladder + 12 SE features (39 indep. feat.)

Among these, the `korea-complex` dataset is mainly covered in our paper, as the ANN model with four weight layers trained on this dataset shows the best performance on the test split (cf. `train-logs`). 
