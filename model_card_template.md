# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
The model utilized in this project is a Logistic Regression classifier model which has been trained on the provided 1994 
census dataset. Many demographic features are utilized to train the model including but not limited to age, work class, 
education level, marital status, race, and sex.
## Intended Use
The intended use of this model is to assist in analysis and predictions of income based on common demographic 
information. These analyses and predictions could be used in a multitude of different settings such as politics or 
non profits (potential for donors based on income) or for market segmentation.
## Training Data
The training data consisted of 80% of the provided dataset.
## Evaluation Data
The evaluation data consisted of the 20% of the dataset that was not utilized in the training of the model. This 20% 
was used to assess the overall performance of the model as seen below.
## Metrics
The metrics utilized in the evaluation of the model include precision, recall, and F1 score. 
Precision is used to measure the accuracy of the predictions and represents the ratio of true positive predictions 
to total positive predictions. 
Recall is used to measure the model's ability to correctly identify all the positive instances within the dataset.
F1 score is the representation of the harmonic mean of precision and recall, which balances both metrics and gives a 
better overall view of the model performance.

#### Model Performance Metrics: 

Precision: 0.7217  

Recall: 0.2520

F1: 0.3736

#### Model Slice Performance:
The model's performance on slices of the data can be found in the slice_output.txt file

## Ethical Considerations
Due to the systemic changes that have occurred since this dataset was compiled (1994), it may contain biases about 
certain demographic groups. These biases can be learned by the model and applied to its predictions. Because of the 
potential for biases in the data, it may be advantageous to evaluate model fairness across different groups as to 
ensure that certain groups are not biased against.

## Caveats and Recommendations
One caveat to this model is that the information gleaned from it could be considered outdated. As the dataset is 30 
years old, it may not generalize well to more modern applications. In order to more successfully apply it to current 
political or business settings (as mentioned above), newer census data may provide more applicable results.