from flask import Flask, redirect, request, render_template, url_for
from TextSummarizer.exception import CustomException
import os
from TextSummarizer.pipeline.prediction import PredictionPipeline

app = Flask(__name__)


@app.route("/", methods = ["GET", "POST"])
def homePage():
    return render_template("index.html")

@app.route("/train")
def train(): #To train the model , i.e. to invoke training pipeline(main.py)
    try:
        os.system("python main.py")
        return "Training successful!!!"

    except Exception as e:
        raise CustomException(e)

@app.route("/predict", methods = ["GET", "POST"])
def predict():
    if request.method == "POST":
        try:
            obj = PredictionPipeline()
            text = request.form.get["input_text"]
            summary = obj.predict(text)
            return summary

        except Exception as e:
            raise CustomException(e)
    else : return render_template("predict.html")




if __name__ == "__main__":
    app.run(debug=True)