# AI & Machine Learning Basics Quiz

### Q1. What does “AI” stand for?

- [x] Artificial Intelligence
- [ ] Automated Integration
- [ ] Applied Innovation
- [ ] Algorithmic Index

**Explanation:** AI refers to machines designed to mimic human intelligence.

### Q2. Which of the following is an example of supervised learning?

- [ ] K-Means Clustering
- [x] Linear Regression
- [ ] Principal Component Analysis
- [ ] DBSCAN

**Explanation:** Linear regression is a supervised learning algorithm because it learns from labeled data.

### Q3. What is overfitting in machine learning?

- [ ] When the model is too simple
- [x] When the model performs well on training data but poorly on new data
- [ ] When the data is corrupted
- [ ] When the algorithm runs too slowly

**Explanation:** Overfitting occurs when the model learns noise from the training data instead of general patterns.

### Q4. Which of these is a common activation function in neural networks?

- [ ] Mean Squared Error
- [ ] Gradient Descent
- [x] ReLU
- [ ] Random Forest

**Explanation:** ReLU (Rectified Linear Unit) is widely used in neural networks as an activation function.

### Q5. What is the difference between AI and ML?

- [x] ML is a subset of AI focused on learning from data
- [ ] AI is a subset of ML
- [ ] AI and ML are the same
- [ ] ML refers to hardware, AI to software

**Reference:** [Intro to AI & ML](https://www.ibm.com/cloud/learn/what-is-artificial-intelligence)

I'll analyze the existing quiz and provide two additional questions while maintaining the same format:

### Q6. What is Deep Learning?

- [x] A subset of machine learning using neural networks with multiple layers
- [ ] A type of database management system
- [ ] A programming language for AI
- [ ] A method of storing large datasets

**Explanation:** Deep Learning is a specialized subset of machine learning that uses neural networks with multiple (deep) layers to progressively extract higher-level features from raw input. It's particularly powerful for complex tasks like image and speech recognition.

Source: [Deep Learning - MIT Press](https://www.deeplearningbook.org/)

### Q7. Which of these is NOT a common type of machine learning?

- [ ] Supervised Learning
- [ ] Unsupervised Learning
- [ ] Reinforcement Learning
- [x] Perpetual Learning

**Explanation:** While Supervised, Unsupervised, and Reinforcement Learning are the three main types of machine learning, "Perpetual Learning" is not a standard classification. The main categories are:

- Supervised Learning (learns from labeled data)
- Unsupervised Learning (finds patterns in unlabeled data)
- Reinforcement Learning (learns through trial and error with rewards/penalties)

Source: [Types of Machine Learning - Stanford University CS229](https://stanford.edu/~shervine/teaching/cs-229/cheatsheet-machine-learning-tips-and-tricks)

### Q8. What is the main goal of reinforcement learning?

- [ ] To learn from labeled data  
- [ ] To reduce dimensionality of data  
- [x] To learn optimal actions through rewards and penalties  
- [ ] To predict continuous values  

**Explanation:** RL agents learn to take actions that maximize cumulative reward through feedback loops.

**Reference:** [Reinforcement Learning - Sutton & Barto](http://incompleteideas.net/book/the-book.html)

### Q9. Which algorithm is commonly used for classification tasks?

- [x] Decision Tree  
- [ ] K-Means  
- [ ] Apriori  
- [ ] DBSCAN  

**Explanation:** Decision Trees are popular for classification because they split data based on feature values to predict labels.

**Reference:** [Decision Tree Classifier - Scikit-learn](https://scikit-learn.org/stable/modules/tree.html)

### Q10. What is the purpose of “gradient descent” in training neural networks?

- [ ] To increase the loss function  
- [x] To minimize the loss function  
- [ ] To normalize input data  
- [ ] To calculate feature importance  

**Explanation:** Gradient Descent minimizes the loss by updating model parameters opposite to the gradient direction.

**Reference:** [Gradient Descent Explained - Coursera](https://www.coursera.org/lecture/machine-learning/gradient-descent-intuition-Ijufg)

### Q11. In which situation would you most likely use clustering algorithms?

- [ ] When you have labeled data  
- [x] When you want to group similar data points without labels  
- [ ] When you want to perform regression analysis  
- [ ] When predicting future prices  

**Explanation:** Clustering is an unsupervised learning method used to group unlabeled data by similarity.

### Q12. What does a confusion matrix show?

- [ ] Model loss over time  
- [x] True positives, false positives, true negatives, and false negatives  
- [ ] Feature correlations  
- [ ] Decision boundaries  

**Explanation:** A confusion matrix summarizes prediction outcomes for classification models.

### Q13. What is the purpose of feature scaling?

- [x] To ensure all features contribute equally to model training  
- [ ] To remove irrelevant features  
- [ ] To encode categorical variables  
- [ ] To reduce overfitting  

**Explanation:** Feature scaling standardizes numerical ranges, helping algorithms like gradient descent converge efficiently.

### Q14. What does “bias-variance tradeoff” refer to?

- [x] The balance between model simplicity and its ability to generalize  
- [ ] The difference between input and output bias  
- [ ] The trade between accuracy and recall  
- [ ] The time-memory tradeoff  

**Explanation:** Low bias can cause overfitting, while high bias leads to underfitting — good models find balance.

### Q15. What metric is best for imbalanced classification problems?

- [ ] Accuracy  
- [ ] MSE  
- [x] F1-Score  
- [ ] R² Score  

**Explanation:** F1-Score balances precision and recall, making it ideal for imbalanced datasets.

### Q16. What is the main purpose of a validation set?

- [ ] To train the model  
- [x] To tune hyperparameters and evaluate performance  
- [ ] To test model performance on unseen data  
- [ ] To normalize the input features  

**Explanation:** Validation sets help in model selection and hyperparameter tuning before final testing.

### Q17. Which algorithm is best suited for dimensionality reduction?

- [ ] KNN  
- [ ] Naive Bayes  
- [x] PCA (Principal Component Analysis)  
- [ ] Random Forest  

**Explanation:** PCA transforms high-dimensional data into fewer dimensions while retaining variance.

### Q18. Which type of neural network is best for sequence data?

- [ ] CNN  
- [x] RNN  
- [ ] GAN  
- [ ] DBN  

**Explanation:** RNNs (Recurrent Neural Networks) are designed for sequential inputs like text or time series.

### Q19. What is the purpose of regularization in machine learning?

- [x] To prevent overfitting by adding penalty terms to the loss function  
- [ ] To normalize inputs  
- [ ] To improve data quality  
- [ ] To increase model complexity  

**Explanation:** Regularization methods like L1/L2 reduce overfitting by constraining model weights.

### Q20. Which of the following is NOT a type of ensemble method?

- [ ] Random Forest  
- [ ] Gradient Boosting  
- [ ] Bagging  
- [x] Dropout  

**Explanation:** Dropout is a regularization technique in neural networks, not an ensemble method.

### Q21. What is the main advantage of using cross-validation?

- [x] Provides a more reliable estimate of model performance  
- [ ] Reduces the need for a validation set  
- [ ] Speeds up training  
- [ ] Simplifies the model  

**Explanation:** Cross-validation uses multiple folds to reduce variance in performance estimates.

### Q22. Which statement best describes unsupervised learning?

- [x] Algorithms find patterns in data without predefined labels  
- [ ] Algorithms require labeled input  
- [ ] Models are trained with rewards and penalties  
- [ ] It’s only used for classification problems  

**Explanation:** Unsupervised learning discovers hidden structures in unlabeled data.
