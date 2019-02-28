from flask import Flask
from flask_restplus import fields, Api, Resource
from nltk_stopwords import Stopwords,Tfcompute
import json

app = Flask(__name__)
api = Api(app)

raw_text = api.model('Rawtext', {'Rawtext' : fields.String('Your Input.')})

@api.route('/Preprocessor')
class Preprocessor(Resource):
    @api.expect(raw_text)
    def post(self):
        #data received from post request
        input_text = api.payload
        #dumps the json object into an element
        json_str = json.dumps(input_text)
        #load the json to a string
        resp = json.loads(json_str)
        #Stopwords elimination begins here
        class1=Stopwords(resp['Rawtext'].lower())
        class2=Tfcompute(class1)
        tokenised_text=class1.nontrivial_words()
        wordfreqdict=class2.wordListToFreqDict()
        return {'tokens' : tokenised_text,'term frequencies': wordfreqdict}

if __name__ == '__main__':
    app.run(debug=True)
