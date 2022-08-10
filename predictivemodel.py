import pickle
import numpy as np
import streamlit as st
loaded_model=pickle.load(open('D:/pro/trained_model.pkl','rb'))

def diabetes_prediction(input_data):
    
   numpy_array=np.asarray(input_data)
   reshaped=numpy_array.reshape(1,-1)
   prediction=loaded_model.predict(reshaped)
   print(prediction)
   if(prediction[0]==0):
       return 'non diabetic person'
   else:
       return 'diabetic person'
   
    
def main():
    st.title('DIABETES PREDICTION UNIT')

    Pregnencies=st.text_input('no. of pregnencies')
    Glucose=st.text_input('no. of glucose')
    Bp=st.text_input('no. of bp')
    skinthickness=st.text_input('no. of skinthickness')
    insulin=st.text_input('no. of insulin')
    bmi=st.text_input('no. of bmi')
    DPF=st.text_input('no. of dpf')
    Age=st.text_input('enter age')
    diagnosis=''
    if st.button('result'):
        diagnosis=diabetes_prediction([Pregnencies,Glucose,Bp,skinthickness,insulin,bmi,DPF,Age])
    st.success(diagnosis)

if __name__=='__main__':
    main()    
