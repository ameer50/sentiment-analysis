from flask import Flask
from flask_restful import Resource, Api
from SentimentAnalysis import deriveSentiment
from transformation import predictors, my_tokenizer

app = Flask(__name__)
api = Api(app)


class SentimentAnalysis(Resource):
    def get(self, phrase):
        sentiment = int(str(deriveSentiment(phrase)))

        return {'Sentiment': sentiment}


api.add_resource(SentimentAnalysis, '/analyze/<string:phrase>')

if __name__ == '__main__':
    app.run(debug=True)
