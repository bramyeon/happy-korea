# Exploring the Relationship Between Air Quality and Happiness in South Korea Using Artificial Neural Networks

__Manuscript submitted to Environmental Impact Assessment Review (2025)__  
Bryan Nathanael Wijaya<sup>1,2</sup>, Yumi Park<sup>3</sup>, Ju Hee Jeung<sup>3</sup>, Kyungmin Lee<sup>4,</sup>*  

<sup>1</sup> School of Computing, Korea Advanced Institute of Science and Technology (KAIST), Daejeon, South Korea  
<sup>2</sup> Max Planck Institute of Security and Privacy (MPI-SP), Bochum, Germany  
<sup>3</sup> Korea Development Institute (KDI) School of Public Policy and Management, Sejong, South Korea  
<sup>4</sup> Biden School of Public Policy and Administration, University of Delaware, Newark, DE, USA  
\* Corresponding author ([kmlee@udel.edu](mailto:kmlee@udel.edu))

## Remarks

The original datasets have not been uploaded to prevent any potential copyright issues. Only the preprocessed test split examples are made available here to accommodate the analysis of happiness ladder factors in the `analysis.ipynb` notebook and the SHAP analysis in the `shap.ipynb` notebook. You can run the Jupyter Notebooks directly in Google Colab. Note that we considered the datasets from 2020 to 2021 only.

There are 5 dataset versions based on the number of features considered.

- `korea-all`: All relevant Korean Happiness Survey (KHS) features + 12 socioeconomic and environmental (SE) features (308 indep. feat.)
- `korea-complex`: KHS features with a correlation value of at least 0.05 w.r.t. the happiness ladder + 12 SE features (141 indep. feat.)
- `korea-medium`: KHS features with a correlation value of at least 0.10 w.r.t. the happiness ladder + 12 SE features (85 indep. feat.)
- `korea-basic`: KHS features with a correlation value of at least 0.15 w.r.t. the happiness ladder + 12 SE features (58 indep. feat.)
- `korea-simple`: KHS features with a correlation value of at least 0.25 w.r.t. the happiness ladder + 12 SE features (39 indep. feat.)

Among these, the `korea-complex` dataset is mainly covered in our paper, as the ANN model with four weight layers trained on this dataset shows the best performance on the test split (cf. `train-logs`). 
