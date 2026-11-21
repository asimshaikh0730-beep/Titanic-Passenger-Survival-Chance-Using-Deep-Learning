# Titanic-Passenger-Survival-Chance-Using-Deep-Learning
Live link:-https://titanic-passenger-survival-chance-using-deep-learning-5sctk4zx.streamlit.app/
This Application Predicts That Whether If a Passenger is going to Survive the titanic Journey or not Using Deep Learning ANN.
# Detail Explanation:-
Hi everyone, my name is Asim.
So, I recently built a project called Titanic Survival Predictor, and I want to quickly share how I made it.
I used Python, TensorFlow, Keras, scikit-learn, Pandas and Streamlit.
First, the data. I worked with around one million rows. The data had text columns, so I converted them into numbers. I used label encoding for gender and one-hot encoding for the port where the passenger boarded. Then I scaled the number columns. I saved all of these with pickle, so the app can use the same steps later.
Next, the model. I built a simple neural network in Keras with two hidden layers, 64 neurons and 32 neurons. I split the data into train, validation and test. I also used early stopping, so the model stops when it is not improving. I got around 85 percent validation accuracy.
Then I deployed it on Streamlit Cloud, and honestly, this part taught me the most. I faced a lot of errors with the environment, packages and deployment. I fixed them one by one, and that is where I learned real debugging.
Right now, I am working on my next project, a GenAI RAG app.
You can try the live app from the link below. Thank you so much for watching!
