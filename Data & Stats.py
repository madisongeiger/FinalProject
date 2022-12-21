import streamlit as st
import pandas as pd
st.title("Data & Stats")


skyscrapers = pd.read_csv('/Users/madisongeiger/Desktop/Quiz1/Final Project/Pages/Skyscrapers2021.csv')
for i in skyscrapers.index:
    skyscrapers.at[i, "Feet"] = skyscrapers.loc[i, "Feet"].replace(' ft', '')
    skyscrapers.at[i, "Feet"] = skyscrapers.loc[i, "Feet"].replace(',', '')
    skyscrapers.at[i, "Feet"] = int(skyscrapers.loc[i, "Feet"])
skyscrapers.set_index("RANK", inplace=True)



cities = []
materials = []
functions = []
for i in skyscrapers.itertuples():
    if i.CITY not in cities:
        cities.append(i.CITY)
    if i.MATERIAL not in materials:
        materials.append(i.MATERIAL)
    if i.FUNCTION not in functions:
        functions.append(i.FUNCTION)
cities = sorted(cities)
materials = sorted(materials)
functions = sorted(functions)



def df_creator(filters):
    if "Location" in filters and "Material" not in filters and "Function" not in filters:
        newdf = skyscrapers[skyscrapers["CITY"].isin(list(location))]
        return newdf
    elif "Material" in filters and "Location" not in filters and "Function" not in filters:
        newdf = skyscrapers[skyscrapers["MATERIAL"].isin(list(material))]
        return newdf
    elif "Function" in filters and "Location" not in filters and "Material" not in filters:
        newdf = skyscrapers[skyscrapers["FUNCTION"].isin(list(function))]
        return newdf
    elif "Location" in filters and "Material" in filters and "Function" not in filters:
        newdf = skyscrapers[skyscrapers["CITY"].isin(list(location)) & skyscrapers["MATERIAL"].isin(list(material))]
        return newdf
    elif "Location" in filters and "Material" not in filters and "Function" in filters:
        newdf = skyscrapers[skyscrapers["CITY"].isin(list(location)) & skyscrapers["FUNCTION"].isin(list(function))]
        return newdf
    elif "Material" in filters and "Location" not in filters and "Function" in filters:
        newdf = skyscrapers[skyscrapers["MATERIAL"].isin(list(material)) & skyscrapers["FUNCTION"].isin(list(function))]
        return newdf
    elif "Function" in filters and "Location" in filters and "Material" in filters:
        newdf = skyscrapers[skyscrapers["FUNCTION"].isin(list(function)) & skyscrapers["CITY"].isin(list(location)) & skyscrapers["MATERIAL"].isin(list(material))]
        return newdf

def count_response(df):
    if len(df) == 1:
        st.write(f"There is {len(df)} result that match your search criteria.")
        st.write(df)
    elif len(df) >1:
        st.write(f"There are {len(df)} results that match your search criteria.")
        st.write(df)
    elif len(df) == 0:
        st.write(f"There are no results that match your search citeria. Please try again.")


def matching_format(df, calc):
    if len(df) == 0:
        st.write(f"There are no results that match your search citeria. Please try again.")
    if len(df) >= 1:
        st.write(f"There are {len(df)} results that match your search criteria.")
    if calc == "Minimum Height":
        min_height = df["Feet"].min()
        for i in df.itertuples():
            if i.Feet == min_height:
                st.write(f"The shortest skyscraper is {i.NAME} and it is {min_height:,} ft tall")
                if st.button(f"More information for {i.NAME}"):
                    st.write(f"More Information: \n")
                    adjust_location = '<p style="margin-left: 40px">Location: <em>'+i.CITY+'<em></p>'
                    st.markdown(adjust_location, unsafe_allow_html=True)
                    adjust_completion = '<p style="margin-left: 40px">Year of Completion: <em>'+str(i.COMPLETION)+'<em></p>'
                    st.markdown(adjust_completion, unsafe_allow_html=True)
                    adjust_floors = '<p style="margin-left: 40px">Number of Floors: <em>'+str(i.FLOORS)+'<em></p>'
                    st.markdown(adjust_floors, unsafe_allow_html=True)
                    adjust_material = '<p style="margin-left: 40px">Material: <em>'+str(i.MATERIAL)+'<em></p>'
                    st.markdown(adjust_material, unsafe_allow_html=True)
                    adjust_function = '<p style="margin-left: 40px">Function: <em>'+i.FUNCTION+'<em></p>'
                    st.markdown(adjust_function, unsafe_allow_html=True)
                    adjust_link = '<p style="margin-left: 40px"><em><a href="'+i.Link+'">Even More Information on '+i.NAME+'<em></a>'
                    st.markdown(adjust_link, unsafe_allow_html=True)
    elif calc == "Maximum Height":
        max_height = df["Feet"].max()
        for i in df.itertuples():
            if i.Feet == max_height:
                st.write(f"The tallest skyscraper is {i.NAME} and it is {max_height:,} ft tall")
                if st.button(f"More information for {i.NAME}"):
                    st.write(f"More Information: \n")
                    adjust_location = '<p style="margin-left: 40px">Location: <em>'+i.CITY+'<em></p>'
                    st.markdown(adjust_location, unsafe_allow_html=True)
                    adjust_completion = '<p style="margin-left: 40px">Year of Completion: <em>'+str(i.COMPLETION)+'<em></p>'
                    st.markdown(adjust_completion, unsafe_allow_html=True)
                    adjust_floors = '<p style="margin-left: 40px">Number of Floors: <em>'+str(i.FLOORS)+'<em></p>'
                    st.markdown(adjust_floors, unsafe_allow_html=True)
                    adjust_material = '<p style="margin-left: 40px">Material: <em>'+str(i.MATERIAL)+'<em></p>'
                    st.markdown(adjust_material, unsafe_allow_html=True)
                    adjust_function = '<p style="margin-left: 40px">Function: <em>'+i.FUNCTION+'<em></p>'
                    st.markdown(adjust_function, unsafe_allow_html=True)
                    adjust_link = '<p style="margin-left: 40px"><em><a href="'+i.Link+'">Even More Information on '+i.NAME+'<em></a>'
                    st.markdown(adjust_link, unsafe_allow_html=True)
    elif calc == "Average Height":
        if len(df) >= 1:
            st.write(f"There are {len(df)} results that match your search criteria.")
        avg_height = df["Feet"].mean()
        st.write(f"The average height of all skyscrapers that match your criteria is {avg_height:,.5} ft.")
    elif calc == "Oldest Skyscraper":
        if len(df) > 0:
            oldest = min(df["COMPLETION"])
            counter = 0
            for i in df.itertuples():
                if i.COMPLETION == oldest:
                    counter = counter+1
            if counter == 1:
                st.write(f"Out of the {len(df)} results that match your search criteria, only {counter} skyscraper was completed in the oldest year: {oldest}")
                for i in df.itertuples():
                    if i.COMPLETION == oldest:
                        st.write(f"The oldest skyscraper is {i.NAME} and it was completed in {oldest}")
                        if st.button(f"More information for {i.NAME}"):
                            st.write(f"More Information: \n")
                            adjust_location = '<p style="margin-left: 40px">Location: <em>'+i.CITY+'<em></p>'
                            st.markdown(adjust_location, unsafe_allow_html=True)
                            adjust_height = '<p style="margin-left: 40px">Height: <em>'+str(i.Feet)+' ft<em></p>'
                            st.markdown(adjust_height, unsafe_allow_html=True)
                            adjust_floors = '<p style="margin-left: 40px">Number of Floors: <em>'+str(i.FLOORS)+'<em></p>'
                            st.markdown(adjust_floors, unsafe_allow_html=True)
                            adjust_material = '<p style="margin-left: 40px">Material: <em>'+str(i.MATERIAL)+'<em></p>'
                            st.markdown(adjust_material, unsafe_allow_html=True)
                            adjust_function = '<p style="margin-left: 40px">Function: <em>'+i.FUNCTION+'<em></p>'
                            st.markdown(adjust_function, unsafe_allow_html=True)
                            adjust_link = '<p style="margin-left: 40px"><em><a href="'+i.Link+'">Even More Information on '+i.NAME+'<em></a>'
                            st.markdown(adjust_link, unsafe_allow_html=True)
            elif counter > 1:
                st.write(f"Out of the {len(df)} results that match your search criteria, {counter} skyscrapers were completed in the oldest year: {oldest}")
                for i in df.itertuples():
                    if i.COMPLETION == oldest:
                        st.write(f"{i.NAME}")
                        if st.button(f"More information for {i.NAME}"):
                            st.write(f"More Information: \n")
                            adjust_location = '<p style="margin-left: 40px">Location: <em>'+i.CITY+'<em></p>'
                            st.markdown(adjust_location, unsafe_allow_html=True)
                            adjust_status = '<p style="margin-left: 40px">Status: <em>'+i.STATUS+'<em></p>'
                            st.markdown(adjust_status, unsafe_allow_html=True)
                            adjust_height = '<p style="margin-left: 40px">Height: <em>'+str(i.Feer)+' ft<em></p>'
                            st.markdown(adjust_height, unsafe_allow_html=True)
                            adjust_floors = '<p style="margin-left: 40px">Number of Floors: <em>'+str(i.FLOORS)+'<em></p>'
                            st.markdown(adjust_floors, unsafe_allow_html=True)
                            adjust_material = '<p style="margin-left: 40px">Material: <em>'+str(i.MATERIAL)+'<em></p>'
                            st.markdown(adjust_material, unsafe_allow_html=True)
                            adjust_function = '<p style="margin-left: 40px">Function: <em>'+i.FUNCTION+'<em></p>'
                            st.markdown(adjust_function, unsafe_allow_html=True)
                            adjust_link = '<p style="margin-left: 40px"><em><a href="'+i.Link+'">Even More Information on '+i.NAME+'<em></a>'
                            st.markdown(adjust_link, unsafe_allow_html=True)
    elif calc == "Most Recent Skyscraper Completed":
        if len(df) > 0:
            recent = max(df["COMPLETION"])
            counter = 0
            for i in df.itertuples():
                if i.COMPLETION == recent:
                    counter = counter+1
            if counter == 1:
                st.write(f"Out of the {len(df)} results that match your search criteria, only {counter} skyscraper was completed in the most recent year: {recent}")
                for i in df.itertuples():
                    if i.COMPLETION == recent:
                        st.write(f"The most recently completed skyscraper is {i.NAME} and it was completed in {recent}")
                        if st.button(f"More information for {i.NAME}"):
                            st.write(f"More Information: \n")
                            adjust_location = '<p style="margin-left: 40px">Location: <em>'+i.CITY+'<em></p>'
                            st.markdown(adjust_location, unsafe_allow_html=True)
                            adjust_height = '<p style="margin-left: 40px">Height: <em>'+str(i.Feet)+' ft<em></p>'
                            st.markdown(adjust_height, unsafe_allow_html=True)
                            adjust_floors = '<p style="margin-left: 40px">Number of Floors: <em>'+str(i.FLOORS)+'<em></p>'
                            st.markdown(adjust_floors, unsafe_allow_html=True)
                            adjust_material = '<p style="margin-left: 40px">Material: <em>'+str(i.MATERIAL)+'<em></p>'
                            st.markdown(adjust_material, unsafe_allow_html=True)
                            adjust_function = '<p style="margin-left: 40px">Function: <em>'+i.FUNCTION+'<em></p>'
                            st.markdown(adjust_function, unsafe_allow_html=True)
                            adjust_link = '<p style="margin-left: 40px"><em><a href="'+i.Link+'">Even More Information on '+i.NAME+'<em></a>'
                            st.markdown(adjust_link, unsafe_allow_html=True)
            elif counter > 1:
                st.write(f"Out of the {len(df)} results that match your search criteria, {counter} skyscrapers were completed in the most recent year: {recent}")
                for i in df.itertuples():
                    if i.COMPLETION == recent:
                        st.write(f"{i.NAME}")
                        if st.button(f"More information for {i.NAME}"):
                            st.write(f"More Information: \n")
                            adjust_location = '<p style="margin-left: 40px">Location: <em>'+i.CITY+'<em></p>'
                            st.markdown(adjust_location, unsafe_allow_html=True)
                            adjust_height = '<p style="margin-left: 40px">Height: <em>'+str(i.Feet)+' ft<em></p>'
                            st.markdown(adjust_height, unsafe_allow_html=True)
                            adjust_floors = '<p style="margin-left: 40px">Number of Floors: <em>'+str(i.FLOORS)+'<em></p>'
                            st.markdown(adjust_floors, unsafe_allow_html=True)
                            adjust_material = '<p style="margin-left: 40px">Material: <em>'+str(i.MATERIAL)+'<em></p>'
                            st.markdown(adjust_material, unsafe_allow_html=True)
                            adjust_function = '<p style="margin-left: 40px">Function: <em>'+i.FUNCTION+'<em></p>'
                            st.markdown(adjust_function, unsafe_allow_html=True)
                            adjust_link = '<p style="margin-left: 40px"><em><a href="'+i.Link+'">Even More Information on '+i.NAME+'<em></a>'
                            st.markdown(adjust_link, unsafe_allow_html=True)




options = ["", "Stats", "Data Tables", "Pivot Table"]
stats_options = ["", "Minimum Height", "Maximum Height", "Average Height", "Oldest Skyscraper", "Most Recent Skyscraper Completed"]
data_table_options = [" ", "Location", "Material", "Function"]
pivot_table_grouping = ["Location", "Material", "Function"]
pivot_table_calc = [" ", "Count", "Unique Values", "Mean", "Sum"]
additional_filter_yn = ["", "Yes", "No"]
st.sidebar.header("Options")
selected_option = st.sidebar.selectbox("Please selection which option you would like", options)


if selected_option == "Data Tables":
    selected_option_dt_options = st.sidebar.multiselect("Please select the data filters", data_table_options)
    if len(selected_option_dt_options) == 0:
        st.write(skyscrapers)
    elif len(selected_option_dt_options) == 3:
        location = st.sidebar.multiselect("Please select the city", cities)
        material = st.sidebar.multiselect("Please select the material", materials)
        function = st.sidebar.multiselect("Please select the function", functions)
        count_response(df_creator(selected_option_dt_options))
    elif "Location" in selected_option_dt_options and "Material" in selected_option_dt_options and "Function" not in selected_option_dt_options:
        location = st.sidebar.multiselect("Please select the city", cities)
        material = st.sidebar.multiselect("Please select the material", materials)
        count_response(df_creator(selected_option_dt_options))
    elif "Location" in selected_option_dt_options and "Function" in selected_option_dt_options and "Material" not in selected_option_dt_options:
        location = st.sidebar.multiselect("Please select the city", cities)
        function = st.sidebar.multiselect("Please select the function", functions)
        count_response(df_creator(selected_option_dt_options))
    elif "Material" in selected_option_dt_options and "Function" in selected_option_dt_options and "Location" not in selected_option_dt_options:
        material = st.sidebar.multiselect("Please select the material", materials)
        function = st.sidebar.multiselect("Please select the function", functions)
        count_response(df_creator(selected_option_dt_options))
    elif "Location" in selected_option_dt_options and "Material" not in selected_option_dt_options and "Function" not in selected_option_dt_options:
        location = st.sidebar.multiselect("Please select the city", cities)
        count_response(df_creator(selected_option_dt_options))
    elif "Location" not in selected_option_dt_options and "Material" in selected_option_dt_options and "Function" not in selected_option_dt_options:
        material = st.sidebar.multiselect("Please select the material", materials)
        count_response(df_creator(selected_option_dt_options))
    if "Location" not in selected_option_dt_options and "Material" not in selected_option_dt_options and "Function" in selected_option_dt_options:
        function = st.sidebar.multiselect("Please select the function", functions)
        count_response(df_creator(selected_option_dt_options))
elif selected_option == "Stats":
    chosen_stat = st.sidebar.selectbox("Please select which stats you would like to view", stats_options)
    additional_filter = st.sidebar.selectbox(f"Would you like to add additional filters for {chosen_stat}", additional_filter_yn)
    if additional_filter == "No":
        matching_format(skyscrapers, chosen_stat)
    elif additional_filter == "Yes":
        selected_option_stats_options = st.sidebar.multiselect("Please select the stats filters", data_table_options)
        if len(selected_option_stats_options) == 3:
            location = st.sidebar.multiselect("Please select the city", cities)
            material = st.sidebar.multiselect("Please select the material", materials)
            function = st.sidebar.multiselect("Please select the function", functions)
            matching_format(df_creator(selected_option_stats_options), chosen_stat)
        elif "Location" in selected_option_stats_options and "Material" in selected_option_stats_options and "Function" not in selected_option_stats_options:
            location = st.sidebar.multiselect("Please select the city", cities)
            material = st.sidebar.multiselect("Please select the material", materials)
            matching_format(df_creator(selected_option_stats_options), chosen_stat)
        elif "Location" in selected_option_stats_options and "Function" in selected_option_stats_options and "Material" not in selected_option_stats_options:
            location = st.sidebar.multiselect("Please select the city", cities)
            function = st.sidebar.multiselect("Please select the function", functions)
            matching_format(df_creator(selected_option_stats_options), chosen_stat)
        elif "Material" in selected_option_stats_options and "Function" in selected_option_stats_options and "Location" not in selected_option_stats_options:
            material = st.sidebar.multiselect("Please select the material", materials)
            function = st.sidebar.multiselect("Please select the function", functions)
            matching_format(df_creator(selected_option_stats_options), chosen_stat)
        elif "Location" in selected_option_stats_options and "Material" not in selected_option_stats_options and "Function" not in selected_option_stats_options:
            location = st.sidebar.multiselect("Please select the city", cities)
            matching_format(df_creator(selected_option_stats_options), chosen_stat)
        elif "Location" not in selected_option_stats_options and "Material" in selected_option_stats_options and "Function" not in selected_option_stats_options:
            material = st.sidebar.multiselect("Please select the material", materials)
            matching_format(df_creator(selected_option_stats_options), chosen_stat)
        elif "Location" not in selected_option_stats_options and "Material" not in selected_option_stats_options and "Function" in selected_option_stats_options:
            function = st.sidebar.multiselect("Please select the function", functions)
            matching_format(df_creator(selected_option_stats_options), chosen_stat)
elif selected_option == "Pivot Table":
    chosen_grouping = st.sidebar.radio("Please select how you wish to group the Pivot Table", pivot_table_grouping)
    if chosen_grouping == "Location":
        location = st.sidebar.multiselect("Please select the city", cities)
        chosen_calc = st.sidebar.selectbox("Please select how they are calculated", pivot_table_calc)
        if chosen_calc == "Count":
            st.write(df_creator(chosen_grouping).groupby(by=["CITY"]).count())
        elif chosen_calc == "Unique Values":
            st.write(df_creator(chosen_grouping).groupby(by=["CITY"]).nunique())
        elif chosen_calc == "Mean":
            st.write(df_creator(chosen_grouping).groupby(by=["CITY"]).mean())
        elif chosen_calc == "Sum":
            st.write(df_creator(chosen_grouping).groupby(by=["CITY"]).mean())
    elif chosen_grouping == "Material":
        material = st.sidebar.multiselect("Please select the material", materials)
        chosen_calc = st.sidebar.selectbox("Please select how they are calculated", pivot_table_calc)
        if chosen_calc == "Count":
            st.write(df_creator(chosen_grouping).groupby(by=["MATERIAL"]).count())
        elif chosen_calc == "Unique Values":
            st.write(df_creator(chosen_grouping).groupby(by=["MATERIAL"]).nunique())
        elif chosen_calc == "Mean":
            st.write(df_creator(chosen_grouping).groupby(by=["MATERIAL"]).mean())
        elif chosen_calc == "Sum":
            st.write(df_creator(chosen_grouping).groupby(by=["MATERIAL"]).mean())
    elif chosen_grouping == "Function":
        function = st.sidebar.multiselect("Please select the function", functions)
        chosen_calc = st.sidebar.selectbox("Please select how they are calculated", pivot_table_calc)
        if chosen_calc == "Count":
            st.write(df_creator(chosen_grouping).groupby(by=["FUNCTION"]).count())
        elif chosen_calc == "Unique Values":
            st.write(df_creator(chosen_grouping).groupby(by=["FUNCTION"]).nunique())
        elif chosen_calc == "Mean":
            st.write(df_creator(chosen_grouping).groupby(by=["FUNCTION"]).mean())
        elif chosen_calc == "Sum":
            st.write(df_creator(chosen_grouping).groupby(by=["FUNCTION"]).mean())



