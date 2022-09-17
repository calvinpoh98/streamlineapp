
# Code to post the user inputs to the API and get the predictions
# Paste the URL to your GCP Cloud Run API here!
api_url = 'https://grad-school-admission-setncat3kq-as.a.run.app'
api_route = '/predict'

response = requests.post(f'{api_url}{api_route}', json=json.dumps(user_input)) # json.dumps() converts dict to JSON
predictions = response.json()

# Add a submit button
if st.button("Submit"): 
    st.write(f"Prediction: {predictions['predictions'][0]}")

# Code to post the user inputs to the API and get the predictions
# Paste the URL to your GCP Cloud Run API here!
api_url = 'https://grad-school-admission-setncat3kq-as.a.run.app'
api_route = '/predict'

response = requests.post(f'{api_url}{api_route}', json=json.dumps(user_input)) # json.dumps() converts dict to JSON
predictions = response.json()

# Add a submit button
if st.button("Submit"): 
    st.write(f"Prediction: {predictions['predictions'][0]}")
