
import streamlit as st
# title
st.title("unit converter")
# input
st.header("input")
num=st.number_input("Enter a number")
# unit options
st.header("select units")
col1,col2=st.columns(2)
with col1:
    from_unit=st.selectbox("from",["kilometers","meters","centimeters"])
    with col2:
        from_unit=st.selectbox("to",["kilometers","meters","centimeters","miles"])
        # conversion function
        def convert_units(num,from_unit,to_unit):
            if from_unit=="kilometers":
                if to_unit=="meters":
                    return num *1000
                elif to_unit=="centimeters":
                    return num*100000
                elif to_unit=="miles":
                    return num *0.621371
                elif from_unit=="meters":
                    if to_unit=="kilmeters":
                        return num/1000            
                    elif to_unit=="centimeters":
                        return num *100
                    elif to_unit=="miles":
                        return num *0.000621371
                    elif from_unit=="centimeters":
                        if to_unit=="kilometers":
                         return num/100000
                        elif to_unit=="meters":
                            return num/100
                        elif to_unit=="miles":
                            return num *0.00000621371
                        # Button
                        if st.button("convert"):
                            result=convert_units(num,from_unit,to_unit)
                            st.success(f"{num}{from_unit} is equal to{result}{to_unit}")
                            

                        
                    
                    





    
















