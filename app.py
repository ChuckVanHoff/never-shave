import flask
import pickle
import pandas as pd
from sklearn.externals import joblib

# Use pickle to load in the pre-trained model
# with open(f'model/earninings_cost_debt_type.pkl',"rb") as f:
#     model = pickle.load(f)
model = joblib.load("earninings_cost_debt_type.pkl")
# Initialise the Flask app
app = flask.Flask(__name__, template_folder='templates')

# Set up the main route
@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        # Just render the initial form, to get input
        return(flask.render_template('main.html'))
    
    if flask.request.method == 'POST':
        # Extract the input
        cost = flask.request.form['cost']
        earnings = flask.request.form['earnings']
        debt = flask.request.form['debt']

        # Make DataFrame for model
        input_variables = pd.DataFrame([[cost, earnings, debt]],
                                       columns=['Average_Cost_Of_Attendance_By_Academic_Year', 'Median_earn_10yr_postgrad', 'Med_Student_Debt_Non_First_Gen'],
                                       dtype=float,
                                       index=['input'])

        # Get the model's prediction
        prediction = model.predict(input_variables)[0]
    
        # Render the form again, but add in the prediction and remind user
        # of the values they input before
        return flask.render_template('main.html',
                                     original_input={'cost':cost,
                                                     'earnings':earnings,
                                                     'debt':debt},
                                     result=prediction,
                                     )

if __name__ == '__main__':
    app.run()