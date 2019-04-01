# Amazon-Review-Analyser
Comparative Study of Machine Learning Approaches for Amazon Reviews
<br>
<br>
# Naive Bayes (NB) Classifier
It is the simplest and mainly used classifier (1). On the basis of allocation of the words in document, this categorization model calculates/computes the subsequent probability of a class. This model works with the BOWs feature extraction ignoring the position of words in the document. Bayes Theorem is used to calculate the probability that specified feature set is part of particular tag 
<br>
<br>
# Maximum Entropy (ME) Classifiers
This classifier is also known as a conditional exponential classifier, using encoding it translates labeled feature sets to vectors. This encoded vector after that is utilized to estimate weights of each feature that are united to choose the most liable label of the feature set. This classifier has parameters as a set of W{weights}, which combines joint features generated from feature-set by E{encoding}. The encoding maps each C{(featureset, label)} pair to a vector.
<br>
<br>
# Support Vector Machines (SVM) Classifiers
It is among the trendy classification techniques. SVM lies on the principle of determining linear separators in the search space that can finest divide the diverse classes. For SVM classification test data is well suited due to bare nature of text, in which some aspects can be unrelated, but are correlated with each other and are arranged into linearly divisible categories.
One of the important applications of SVM is to classify reviews according to their quality. Two multiclass SVM-based approaches were used by Chen and Tseng. Considering product reviews as a categorization problem, they have projected method for calculating quality/value of information in product reviews. To find information oriented feature set, on Iphone reviews, they have adopted an information quality (IQ) framework. They can accurately categorize reviews in provision of their quality.
Li used SVM as sentiment polarity classifier they said that opinion subjectivity and user credibility must be taken into concern. They proposed framework to provide compact numeric summarization of opinions on micro-blogs platforms (33). They have classified the opinions using SVM after recognizing and extracting the topics in opinions related with queries of the users. Twitter posts were used for their experiments. They proved that for aggregating micro-blog opinions the consideration of opinion subjectivity and user credibility is necessary. The libsvm library is used by us with linear kernel for our experiment. Two sets of vectors are included in input data each of size X. Every
entry in vector correlates to occurrence of a feature. When feature is present: value 1 is assigned but when it is not present value 0 is assigned. To speed up overall processing we have used feature presence in spite of count, therefore we do not need to range input data.

