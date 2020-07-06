import pickle, joblib



def deriveSentiment(statement):
    pipeline = joblib.load('model.pkl')
    return pipeline.predict([statement])[0]