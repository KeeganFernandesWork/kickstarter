# Kickstarter Project
## Introduction
The goal of this project is to build a model that predicts the success or failure of a publicly funded Kickstarter project. The data for this project can be found [here](https://medium.com/r/?url=https%3A%2F%2Fwww.kaggle.com%2Fkemical%2Fkickstarter-projects). To view the full project, visit the [GitHub page](https://medium.com/r/?url=https%3A%2F%2Fgithub.com%2FAristotle609%2Fkickstarter). The notebooks that I will be sharing here can be viewed in Kaggle.

## The Problem
Every year thousands of projects are crowdfunded on the platform https://www.kickstarter.com/ which is a public platform to publish your projects and obtain public funding. Every year, thousands of projects on this platform fail and don't receive funding. Our goal is to make an application that can predict whether a project will succeed or not.

## The Process
As with all projects, I started with my [EDA](https://medium.com/r/?url=https%3A%2F%2Fwww.kaggle.com%2Faristotle609%2Fkickstarter-project-eda) and found some interesting information
![](https://cdn-images-1.medium.com/max/800/1*HF-N2Vt7V_Dz9Kp-R9cQTg.png)
The category with the most projects seems to be Films and Video the category with the highest number of relative successes is Music and Theater and the category with the most relative failures is Technology. Most Liberal arts seem to do well in Kickstarter, which makes sense since they require little capital compared to technology kickstarters that require equipment and more experienced employees.

![Considering the Sample size, the number of successes isn't that bad.](https://cdn-images-1.medium.com/max/800/1*cGhXKrxiFK4u1fm5IYuTfQ.png)

I then began making the model for the data. I always start by making a baseline model, which is the least complicated that way I can compare it to other models. While making the notebooks, I used a subset of the total training data and later ran the whole dataset on a remote notebook (on Kaggle) I started with a Logistic Regression Baseline model and gained excellent results. I obtained similar results with decision trees only with XGBoost did I get slightly better results. However, with the whole dataset, linear regression performed the worst, while Random Forest classifiers and XGBoost Classifiers retained their scores. In the end, I went with the [XGBoost model](https://medium.com/r/?url=https%3A%2F%2Fwww.kaggle.com%2Faristotle609%2Fkickstarter-project-xgboost) since it had the best results.

![](https://cdn-images-1.medium.com/max/800/1*3dV5lbEO8TpqAWMRmeiz1Q.png)
## The Application
I built a simple application using streamlit and deployed it using streamlit share. The application can be viewed [here](https://medium.com/r/?url=https%3A%2F%2Fshare.streamlit.io%2Faristotle609%2Fkickstarter%2Fmain%2Fmain.py).
![](https://cdn-images-1.medium.com/max/800/1*6dlUg0M4ZI95sagoDMn8QA.png)
## Endnote
This project is a part of my series 25 projects challenge. If you want to see more of these or want to take part yourself, please visit the [introduction page](https://medium.com/r/?url=https%3A%2F%2Fkeeganfdes03.medium.com%2Ff2150afe053%3Fsource%3Dfriends_link%26sk%3D5ae10ad6072aa80c0f1ed3865a0196a8).
Thank you for reading this far.

 
