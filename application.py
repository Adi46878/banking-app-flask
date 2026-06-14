import pickle
import pandas as pd
from flask import Flask, render_template, request

# Load model
model = pickle.load(open('RF_model_exaple.pkl', 'rb'))

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction_text = None

    if request.method == 'POST':
        try:
            form_inputs = pd.DataFrame(request.form.to_dict(), index=[0])

            prediction = model.predict(form_inputs.astype(float))

            if prediction[0] == 1:
                prediction_text = "⚠️ High Risk of Default"
            else:
                prediction_text = "✅ Low Risk of Default"

        except Exception as e:
            prediction_text = f"Error: {str(e)}"

    return render_template('index.html', prediction=prediction_text)

if __name__ == "__main__":
    app.run(debug=True)
