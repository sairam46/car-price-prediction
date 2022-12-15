import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))

df = pd.read_csv('cleaned_spinny.csv')


def main():
    st.title("car Price Predictor 🚗")
    st.markdown("##### Are you planning to sell your car !?\n##### So let's try evaluating the price.. 🤖 ")

    # @st.cache(allow_output_mutation=True)
    # def get_model():
    #     model = pickle.load(open('RF_price_predicting_model.pkl','rb'))
    #     return model

    st.write('car price predictor')
    st.write('')

    car_make = st.selectbox('Select the make of the car',df.make.unique())
    modell = df[(df['make'] == car_make)]
    car_model = st.selectbox('Select the model of the car',sorted(modell['model'].unique()))
    variant1 = df[(df['model'] == car_model)]
    variant = st.selectbox('Select the variant of the car',sorted(variant1['variant'].unique()))
    bt=df[(df['variant'] == variant)]
    bodytype1 = st.selectbox('select body type:',(bt['body_type'].unique()))

    mileage= st.slider('mileage', min_value=1000, max_value=1000000, value=1000, step=5)

    fuel_type= st.radio("Select Fuel type",
    ('petrol', 'diesel', 'cng', 'electric', 'lpg'),horizontal=True)

    transmission= st.radio("Select transmission type",
    ('manual','automatic'),horizontal=True)


    car_years = st.number_input('In which year car was purchased ?', 1995, 2022, step=2, key='year')

    city = st.selectbox('Select the make of the car',df.city.unique())


    # st.write(car_make,car_model,car_years,city,fuel_type,transmission,bodytype,variant,mileage)
    if st.button("Estimate Price", key='predict'):
        try:
            M = model  # get_model()
            prediction = M.predict(pd.DataFrame([[car_make,car_model,variant,bodytype1,mileage,fuel_type,transmission,car_years,city]],
                         columns=['make','model','variant','body_type','mileage','fuel_type','transmission','year','city']))
            output = round(prediction[0], 2)
            if output < 0:
                st.warning("You will be not able to sell this car !!")
            else:
                st.success("You can sell the car for {} lakhs 🙌".format(output))
        except:
            st.warning("Opps!! Something went wrong\nTry again")
if __name__ == "__main__":
    main()
