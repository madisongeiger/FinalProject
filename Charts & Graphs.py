import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
st.title("Charts & Graphs")



skyscrapers = pd.read_csv('/Users/madisongeiger/Desktop/Quiz1/Final Project/Pages/Skyscrapers2021.csv')


# Creating list of all cities, statuses, materials, and functions in the csv file with no duplicates, sorted alphabetically
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





# Function which needs takes at least two arguments primary (the initial input the user puts in that they way to see displayed) and the df (data frame of the filtered data based on the given input criteria)
# Function returns the list of primary input with no duplicates (ex. if primary is location and user only wants to see skyscrapers in New York and Dubai the list city count list will return [New York, Dubai]
# Function also returns the frequency of each primary input in a list (ex. if Dubai and New York appear in the data frame 5 and 2 times, respectivley, the function will return [5, 2]
# The only time it uses df2-df4 if it is for a line chart in which it will populate different count lists for each of the desired lines, a default value is given to df2-df4 for bar charts and if there is less than 4 different inputs for line charts

def list_and_count_creator(primary, df, df2="", df3=""):
    if primary == "Location":
        # Creating list of all cities
        cities = []
        for i in df.itertuples():
            if i.CITY not in cities:
                cities.append(i.CITY)
        sorted(cities)
        # Creating dictionary of each city and its frequency
        city_count = {}
        for i in cities:
            city_count[i] = 0
        for i in df.itertuples():
            for j in city_count:
                if i.CITY == j:
                    city_count[j] = city_count[j]+1
        # Turning dictionary into list so that it can be used later to make a plot
        city_count_list = [city_count[i] for i in city_count]
        return city_count_list, cities
    elif primary == "Material":
        # Creating list of all materials
        materials = []
        for i in df.itertuples():
            if i.MATERIAL not in materials:
                materials.append(i.MATERIAL)
        sorted(materials)
        # Creating dictionary of each material and its frequency
        material_count = {}
        for i in materials:
            material_count[i] = 0
        for i in df.itertuples():
            for j in material_count:
                if i.MATERIAL == j:
                    material_count[j] = material_count[j]+1
        # Turning dictionary into list so that it can be used later to make a plot
        material_count_list = [material_count[i] for i in material_count]
        return material_count_list, materials
    elif primary == "Function":
        # Creating list of all functions
        functions = []
        for i in df.itertuples():
            if i.FUNCTION not in functions:
                functions.append(i.FUNCTION)
        sorted(functions)
        # Creating dictionary of each function and its frequency
        function_count = {}
        for i in functions:
            function_count[i] = 0
        for i in df.itertuples():
            for j in function_count:
                if i.FUNCTION == j:
                    function_count[j] = function_count[j]+1
        # Turning dictionary into list so that it can be used later to make a plot
        function_count_list = [function_count[i] for i in function_count]
        return function_count_list, functions
    elif primary == "Years" and len(option_choice) == 1:
        years = []
        for i in df.itertuples():
            if i.COMPLETION not in years:
                years.append(i.COMPLETION)
        years.sort()
        year_count = {}
        for i in years:
            year_count[i] = 0
        for i in df.itertuples():
            for j in year_count:
                if i.COMPLETION == j:
                    year_count[j] = year_count[j]+1
        year_count_list = [year_count[i] for i in year_count]
        return year_count_list, years
    elif primary == "Years" and len(option_choice) == 2:
        years = []
        for i in df.itertuples():
            if i.COMPLETION not in years:
                years.append(i.COMPLETION)
        years.sort()
        year_count1 = {}
        for i in years:
            year_count1[i] = 0
        for i in df.itertuples():
            for j in year_count1:
                if i.COMPLETION == j:
                    year_count1[j] = year_count1[j]+1
        year_count_list1 = [year_count1[i] for i in year_count1]
        year_count2 = {}
        for i in years:
            year_count2[i] = 0
        for i in df2.itertuples():
            for j in year_count2:
                if i.COMPLETION == j:
                    year_count2[j] = year_count2[j]+1
        year_count_list2 = [year_count2[i] for i in year_count2]
        return year_count_list1, year_count_list2, years
    elif primary == "Years" and len(option_choice) == 3:
        years = []
        for i in df.itertuples():
            if i.COMPLETION not in years:
                years.append(i.COMPLETION)
        years.sort()
        year_count1 = {}
        for i in years:
            year_count1[i] = 0
        for i in df.itertuples():
            for j in year_count1:
                if i.COMPLETION == j:
                    year_count1[j] = year_count1[j]+1
        year_count_list1 = [year_count1[i] for i in year_count1]
        year_count2 = {}
        for i in years:
            year_count2[i] = 0
        for i in df2.itertuples():
            for j in year_count2:
                if i.COMPLETION == j:
                    year_count2[j] = year_count2[j]+1
        year_count_list2 = [year_count2[i] for i in year_count2]
        year_count3 = {}
        for i in years:
            year_count3[i] = 0
        for i in df3.itertuples():
            for j in year_count3:
                if i.COMPLETION == j:
                    year_count3[j] = year_count3[j]+1
        year_count_list3 = [year_count3[i] for i in year_count3]
        return year_count_list1, year_count_list2, year_count_list3, years


# Function only for bar and pie charts which takes two arguments Primary and a list of the filters the user decides to put on the data, if there are no filters chosen then the default is "" or nothing
# Instead of returning a physical value the function will filter the data frame based on the requirements and then run it through the list_and_count_creator function with the new df as the second argument

def filtered_data_creator(primary, filters=""):
    if "Location" == primary and len(filters) == 0:
        newdf = skyscrapers[skyscrapers["CITY"].isin(location_choice)]
        return list_and_count_creator(option_choice, newdf)
    elif "Material" == primary and len(filters) == 0:
        newdf = skyscrapers[skyscrapers["MATERIAL"].isin(material_choice)]
        return list_and_count_creator(option_choice, newdf)
    elif "Function" == primary and len(filters) == 0:
        newdf = skyscrapers[skyscrapers["FUNCTION"].isin(function_choice)]
        return list_and_count_creator(option_choice, newdf)
    elif "Location" == primary and "Material" in filters and "Function" not in filters:
        newdf = skyscrapers[skyscrapers["CITY"].isin(location_choice) & skyscrapers["MATERIAL"].isin(material_choice)]
        return list_and_count_creator(option_choice, newdf)
    elif "Location" == primary and "Material" not in filters and "Function" in filters:
        newdf = skyscrapers[skyscrapers["CITY"].isin(location_choice) & skyscrapers["FUNCTION"].isin(function_choice)]
        return list_and_count_creator(option_choice, newdf)
    elif "Location" == primary and "Material" in filters and "Function" in filters:
        newdf = skyscrapers[skyscrapers["CITY"].isin(location_choice) & skyscrapers["FUNCTION"].isin(function_choice) & skyscrapers["MATERIAL"].isin(material_choice)]
        return list_and_count_creator(option_choice, newdf)
    elif "Material" == primary and "Location" in filters and "Function" not in filters:
        newdf = skyscrapers[skyscrapers["MATERIAL"].isin(material_choice) & skyscrapers["CITY"].isin(location_choice)]
        return list_and_count_creator(option_choice, newdf)
    elif "Material" == primary and "Location" not in filters and "Function" in filters:
        newdf = skyscrapers[skyscrapers["MATERIAL"].isin(material_choice) & skyscrapers["FUNCTION"].isin(function_choice)]
        return list_and_count_creator(option_choice, newdf)
    elif "Material" == primary and "Location" in filters and "Function" in filters:
        newdf = skyscrapers[skyscrapers["MATERIAL"].isin(material_choice) & skyscrapers["CITY"].isin(location_choice) & skyscrapers["FUNCTION"].isin(function_choice)]
        return list_and_count_creator(option_choice, newdf)
    elif "Function" == primary and "Location" in filters and "Material" not in filters:
        newdf = skyscrapers[skyscrapers["FUNCTION"].isin(function_choice) & skyscrapers["CITY"].isin(location_choice)]
        return list_and_count_creator(option_choice, newdf)
    elif "Function" == primary and "Location" not in filters and "Material" in filters:
        newdf = skyscrapers[skyscrapers["FUNCTION"].isin(function_choice) & skyscrapers["MATERIAL"].isin(material_choice)]
        return list_and_count_creator(option_choice, newdf)
    elif "Function" == primary and "Location" in filters and "Material" in filters:
        newdf = skyscrapers[skyscrapers["FUNCTION"].isin(function_choice) & skyscrapers["CITY"].isin(location_choice) & skyscrapers["MATERIAL"].isin(material_choice)]
        return list_and_count_creator(option_choice, newdf)

# Function only for line charts which takes only one argument primaries which are the inputs from the user that they which to see a line of
# Function takes the primaries and produces filtered dataframes for each one
# If there is only one line on the chart requested then there will only be on df created, if there is two then two will be created, and so on
def filtered_data_creator_for_line(primaries):
    if "Location" in primaries and len(primaries) == 1:
        newdf = skyscrapers[skyscrapers["CITY"].isin(location_choice)]
        return list_and_count_creator("Years", newdf)
    elif "Material" in primaries and len(primaries) == 1:
        newdf = skyscrapers[skyscrapers["MATERIAL"].isin(material_choice)]
        return list_and_count_creator("Years", newdf)
    elif "Function" in primaries and len(primaries) == 1:
        newdf = skyscrapers[skyscrapers["FUNCTION"].isin(function_choice)]
        return list_and_count_creator("Years", newdf)
    elif "Location" in primaries and "Material" in primaries and "Function" not in primaries:
        newdf_loc = skyscrapers[skyscrapers["CITY"].isin(location_choice)]
        newdf_mat = skyscrapers[skyscrapers["MATERIAL"].isin(material_choice)]
        return list_and_count_creator("Years", newdf_loc, newdf_mat)
    elif "Location" in primaries and "Material" not in primaries and "Function" in primaries:
        newdf_loc = skyscrapers[skyscrapers["CITY"].isin(location_choice)]
        newdf_fun = skyscrapers[skyscrapers["FUNCTION"].isin(function_choice)]
        return list_and_count_creator("Years", newdf_loc, newdf_fun)
    elif "Location" not in primaries and "Material" in primaries and "Function" in primaries:
        newdf_mat = skyscrapers[skyscrapers["MATERIAL"].isin(material_choice)]
        newdf_fun = skyscrapers[skyscrapers["FUNCTION"].isin(function_choice)]
        return list_and_count_creator("Years", newdf_mat, newdf_fun)
    elif "Location" in primaries and "Material" in primaries and "Function" in primaries:
        newdf_loc = skyscrapers[skyscrapers["CITY"].isin(location_choice)]
        newdf_fun = skyscrapers[skyscrapers["FUNCTION"].isin(function_choice)]
        newdf_mat = skyscrapers[skyscrapers["MATERIAL"].isin(material_choice)]
        return list_and_count_creator("Years", newdf_loc, newdf_mat, newdf_fun)

# Function which takes one argument, selected chart type
# Function returns a plot of the filtered data using the two lists that are returned in the filtered_data_creator function

def chart_creator(type):
    # Making pie charts
    if type == "Pie Chart":
        # If there is no additional filters put on the data
        if additional_filter == "No":
            fig,ax = plt.subplots()
            ax.pie(filtered_data_creator(option_choice)[0], labels=filtered_data_creator(option_choice)[1], autopct='%1.2f%%')
            plt.title(f"{chart_choice} of {option_choice}", fontweight="bold")
            return st.pyplot(fig)
        # If there are additional filters put on the data
        if additional_filter == "Yes":
            fig,ax = plt.subplots()
            ax.pie(filtered_data_creator(option_choice, filter_choice)[0], labels=filtered_data_creator(option_choice, filter_choice)[1], autopct='%1.2f%%')
            plt.title(f"{chart_choice} of {option_choice} Filtered by {' and '.join(filter_choice)}", fontweight="bold")
            return st.pyplot(fig)
    # Making bar charts
    if type == "Bar Chart":
        # If there is no additional filters put on the data
        if additional_filter == "No":
            fig,ax = plt.subplots()
            ax.bar(filtered_data_creator(option_choice)[1], filtered_data_creator(option_choice)[0], color=st.sidebar.selectbox(f"Please select your desired {option_choice} color", colors))
            plt.title(f"{chart_choice} of {option_choice}", fontweight="bold")
            plt.xlabel(option_choice, fontweight="bold")
            plt.xticks(rotation=90)
            plt.ylabel("Count", fontweight="bold")
            if max(filtered_data_creator(option_choice)[0]) > 10:
                plt.yticks(np.arange(0, max(filtered_data_creator(option_choice)[0])+10, 10))
                return st.pyplot(fig)
            else:
                plt.yticks(np.arange(0, max(filtered_data_creator(option_choice)[0])+1, 2))
                return st.pyplot(fig)
        # If there are additional filters put on the data
        if additional_filter == "Yes":
            fig,ax = plt.subplots()
            ax.bar(filtered_data_creator(option_choice, filter_choice)[1], filtered_data_creator(option_choice, filter_choice)[0], color=st.sidebar.selectbox(f"Please select your desired {option_choice} color", colors))
            plt.title(f"{chart_choice} of {option_choice} Filtered by {' and '.join(filter_choice)}", fontweight="bold")
            plt.xlabel(option_choice, fontweight="bold")
            plt.ylabel("Count", fontweight="bold")
            if max(filtered_data_creator(option_choice)[0]) > 10:
                plt.yticks(np.arange(0, max(filtered_data_creator(option_choice)[0])+10, 10))
                return st.pyplot(fig)
            else:
                plt.yticks(np.arange(0, max(filtered_data_creator(option_choice)[0])+1, 2))
                return st.pyplot(fig)
    if type == "Line Chart":
        # No filters can be added to line charts, only the ability to see different lines
        fig,ax = plt.subplots()
        if len(option_choice) == 1:
            ax.plot(filtered_data_creator_for_line(option_choice)[1], filtered_data_creator_for_line(option_choice)[0], color=st.sidebar.selectbox(f"Please select your desired {option_choice[0]} color", colors))
            # legend is produced with the appropriate label, based on what they option they chose (location, material, function, status)
            plt.legend(labels = option_choice, loc = 0)
            # x axis tick marks are rotated so that it is easier for the user to see the year
            plt.xticks(rotation=90)
            plt.title(f"{chart_choice} of {''.join(option_choice)}", fontweight="bold")
            plt.xlabel("Year", fontweight="bold")
            plt.ylabel("Count", fontweight="bold")
            if max(filtered_data_creator_for_line(option_choice)[0]) > 10:
                plt.yticks(np.arange(0, max(filtered_data_creator_for_line(option_choice)[0])+10, 10))
                return st.pyplot(fig)
            else:
                plt.yticks(np.arange(0, max(filtered_data_creator_for_line(option_choice)[0])+1, 2))
                return st.pyplot(fig)
        if len(option_choice) == 2:
            ax.plot(filtered_data_creator_for_line(option_choice)[2], filtered_data_creator_for_line(option_choice)[0], color=st.sidebar.selectbox(f"Please select your desired {option_choice[0]} color", colors))
            ax.plot(filtered_data_creator_for_line(option_choice)[2], filtered_data_creator_for_line(option_choice)[1], color=st.sidebar.selectbox(f"Please select your desired {option_choice[1]} color", colors))
            # legend is produced with the appropriate label, based on what they option they chose (location, material, function, status)
            plt.legend(labels = option_choice, loc = 0)
            # x axis tick marks are rotated so that it is easier for the user to see the year
            plt.xticks(rotation=90)
            plt.title(f"{chart_choice} of {' and '.join(option_choice)}", fontweight="bold")
            plt.xlabel("Year", fontweight="bold")
            plt.ylabel("Count", fontweight="bold")
            if max(filtered_data_creator_for_line(option_choice)[0]) > 10 or max(filtered_data_creator_for_line(option_choice)[1]) > 10:
                plt.yticks(np.arange(0, max(max(filtered_data_creator_for_line(option_choice)[0]), max(filtered_data_creator_for_line(option_choice)[1]))+10, 10))
                return st.pyplot(fig)
            else:
                plt.yticks(np.arange(0, max(max(filtered_data_creator_for_line(option_choice)[0]), max(filtered_data_creator_for_line(option_choice)[1]))+1, 2))
                return st.pyplot(fig)
        if len(option_choice) == 3:
            ax.plot(filtered_data_creator_for_line(option_choice)[3], filtered_data_creator_for_line(option_choice)[0], color=st.sidebar.selectbox(f"Please select your desired {option_choice[0]} color", colors))
            ax.plot(filtered_data_creator_for_line(option_choice)[3], filtered_data_creator_for_line(option_choice)[1], color=st.sidebar.selectbox(f"Please select your desired {option_choice[1]} color", colors))
            ax.plot(filtered_data_creator_for_line(option_choice)[3], filtered_data_creator_for_line(option_choice)[2], color=st.sidebar.selectbox(f"Please select your desired {option_choice[2]} color", colors))
            # legend is produced with the appropriate label, based on what they option they chose (location, material, function, status)
            plt.legend(labels = option_choice, loc = 0)
            # x axis tick marks are rotated so that it is easier for the user to see the year
            plt.xticks(rotation=90)
            plt.title(f"{chart_choice} of {' and '.join(option_choice)}", fontweight="bold")
            plt.xlabel("Year", fontweight="bold")
            plt.ylabel("Count", fontweight="bold")
            if max(filtered_data_creator_for_line(option_choice)[0]) > 10 or max(filtered_data_creator_for_line(option_choice)[1]) > 10 or max(filtered_data_creator_for_line(option_choice)[2]) > 10:
                plt.yticks(np.arange(0, max(max(filtered_data_creator_for_line(option_choice)[0]), max(filtered_data_creator_for_line(option_choice)[1]), max(filtered_data_creator_for_line(option_choice)[2]))+10, 10))
                return st.pyplot(fig)
            else:
                plt.yticks(np.arange(0, max(max(filtered_data_creator_for_line(option_choice)[0]), max(filtered_data_creator_for_line(option_choice)[1]), max(filtered_data_creator_for_line(option_choice)[2]))+1, 2))
                return st.pyplot(fig)
        if len(option_choice) == 4:
            ax.plot(filtered_data_creator_for_line(option_choice)[4], filtered_data_creator_for_line(option_choice)[0], color=st.sidebar.selectbox(f"Please select your desired {option_choice[0]} color", colors))
            ax.plot(filtered_data_creator_for_line(option_choice)[4], filtered_data_creator_for_line(option_choice)[1], color=st.sidebar.selectbox(f"Please select your desired {option_choice[1]} color", colors))
            ax.plot(filtered_data_creator_for_line(option_choice)[4], filtered_data_creator_for_line(option_choice)[2], color=st.sidebar.selectbox(f"Please select your desired {option_choice[2]} color", colors))
            ax.plot(filtered_data_creator_for_line(option_choice)[4], filtered_data_creator_for_line(option_choice)[3], color=st.sidebar.selectbox(f"Please select your desired {option_choice[3]} color", colors))
            # legend is produced with the appropriate label, based on what they option they chose (location, material, function, status)
            plt.legend(labels = option_choice, loc = 0)
            # x axis tick marks are rotated so that it is easier for the user to see the year
            plt.xticks(rotation=90)
            plt.title(f"{chart_choice} of {' and '.join(option_choice)}", fontweight="bold")
            plt.xlabel("Year", fontweight="bold")
            plt.ylabel("Count", fontweight="bold")
            if max(filtered_data_creator_for_line(option_choice)[0]) > 10 or max(filtered_data_creator_for_line(option_choice)[1]) > 10 or max(filtered_data_creator_for_line(option_choice)[2]) > 10 or max(filtered_data_creator_for_line(option_choice)[3]) > 10:
                plt.yticks(np.arange(0, max(max(filtered_data_creator_for_line(option_choice)[0]), max(filtered_data_creator_for_line(option_choice)[1]), max(filtered_data_creator_for_line(option_choice)[2]), max(filtered_data_creator_for_line(option_choice)[3]))+10, 10))
                return st.pyplot(fig)
            else:
                plt.yticks(np.arange(0, max(max(filtered_data_creator_for_line(option_choice)[0]), max(filtered_data_creator_for_line(option_choice)[1]), max(filtered_data_creator_for_line(option_choice)[2]), max(filtered_data_creator_for_line(option_choice)[3]))+1, 2))
                return st.pyplot(fig)

# Creating list of the different options users will be presented with
variables = [" ", "Location", "Material", "Function"]
charts = [" ", "Bar Chart", "Line Chart", "Pie Chart"]
additional_filter_yn = ["", "Yes", "No"]
colors = ["red", "green", "blue", "orange", "pink", "purple"]

# Asking user to select their desired chart
chart_choice = st.sidebar.selectbox("Please select the type of chart you would like to see", charts)

# Only asks the next question once the user has selected an initial variable choice
if chart_choice == "Bar Chart" or chart_choice == "Pie Chart":
    # Asking user which chart they want and if they want to add filters
    option_choice = st.sidebar.selectbox(f"Please select what options you would like to a {chart_choice} of", variables)
    additional_filter = st.sidebar.selectbox(f"Would you like to add additional filters for {chart_choice}?", additional_filter_yn)
    # If they choose that they want to see location
    if option_choice == "Location":
        # Asking which locations they want to see and limiting them at five because if there is more than 5 the charts look messy
        location_choice = st.sidebar.multiselect("Please select the cities you would like to view (Limit of 5)", cities)
        if len(location_choice) > 5:
            st.write("There are too many cities chosen please select less cities")
        elif len(location_choice) > 0:
            # Creating charts
            if additional_filter == "No":
                chart_creator(chart_choice)
            elif additional_filter == "Yes":
                filter_choice = st.sidebar.multiselect("Please select the filters", variables)
                # Displaying the correct follow up questions given the filters they want to see and creating charts based on inputs
                if "Material" in filter_choice and "Function" not in filter_choice:
                    material_choice = st.sidebar.multiselect("Please select the material", materials)
                    if len(material_choice) > 0:
                        chart_creator(chart_choice)
                elif "Material" not in filter_choice and "Function" in filter_choice:
                    function_choice = st.sidebar.multiselect("Please select the function", functions)
                    if len(function_choice) > 0:
                        chart_creator(chart_choice)
                elif "Status" not in filter_choice and "Material" in filter_choice and "Function" in filter_choice:
                    material_choice = st.sidebar.multiselect("Please select the materials", materials)
                    function_choice = st.sidebar.multiselect("Please select the functions", functions)
                    if len(material_choice) > 0 and len(function_choice) > 0:
                        chart_creator(chart_choice)
    # If they choose that they want to see material
    elif option_choice == "Material":
        # Asking which materials they want to see
        material_choice = st.sidebar.multiselect("Please select the materials you would like to view", materials)
        if len(material_choice) > 0:
            if additional_filter == "No":
                chart_creator(chart_choice)
            elif additional_filter == "Yes":
                # Displaying the correct follow up questions given the filters they want to see and creating charts based on inputs
                filter_choice = st.sidebar.multiselect("Please select the filters", variables)
                if "Location" in filter_choice and "Function" not in filter_choice:
                    location_choice = st.sidebar.multiselect("Please select the cities", cities)
                    if len(location_choice) > 5:
                        st.write("There are too many cities chosen please select less cities")
                    elif len(location_choice) > 0:
                        chart_creator(chart_choice)
                elif "Location" not in filter_choice and "Function" in filter_choice:
                    function_choice = st.sidebar.multiselect("Please select the function", functions)
                    if len(function_choice) >0:
                        chart_creator(chart_choice)
                elif "Location" in filter_choice and "Function" in filter_choice:
                    location_choice = st.sidebar.multiselect("Please select the cities", cities)
                    function_choice = st.sidebar.multiselect("Please select the functions", functions)
                    if len(location_choice) > 5:
                        st.write("There are too many cities chosen please select less cities")
                    elif len(location_choice) > 0 and len(function_choice) > 0:
                        chart_creator(chart_choice)
    # If they choose that they want to see function
    elif option_choice == "Function":
        # Asking which functions they want to see
        function_choice = st.sidebar.multiselect("Please select the functions you would like to view", functions)
        if len(function_choice) > 0:
            # Creating charts
            filter_choice = st.sidebar.multiselect("Please select the filters", variables)
            if additional_filter == "No":
                chart_creator(chart_choice)
            if additional_filter == "Yes":
                # Displaying the correct follow up questions given the filters they want to see and creating charts based on inputs
                if "Location" in filter_choice and "Material" not in filter_choice:
                    location_choice = st.sidebar.multiselect("Please select the cities", cities)
                    if len(location_choice) > 5:
                        st.write("There are too many cities chosen please select less cities")
                    elif len(location_choice) > 0:
                        chart_creator(chart_choice)
                elif "Location" not in filter_choice and "Material" in filter_choice:
                    material_choice = st.sidebar.multiselect("Please select the materials", materials)
                    if len(material_choice) > 0:
                        chart_creator(chart_choice)
                elif "Location" in filter_choice and "Material" in filter_choice:
                    location_choice = st.sidebar.multiselect("Please select the cities", cities)
                    material_choice = st.sidebar.multiselect("Please select the materials", materials)
                    if len(location_choice) > 5:
                        st.write("There are too many cities chosen please select less cities")
                    elif len(location_choice) > 0 and len(material_choice) > 0:
                        chart_creator(chart_choice)

elif chart_choice == "Line Chart":
    # for line charts users cannot filter the data rather they can choose different lines on the line chart based on the options they chose
    option_choice = st.sidebar.multiselect(f"Please select what options you would like to a {chart_choice} of", variables)
    # sorting the option_choice list so that when it comes time to make the chart the options are in the same order each time so the legend is correct
    # ex. if the list was not sorted and the user chose "location" then "status" the line chart would assign the legend based on that order so if the user then if the user tried it again but chose "status" then "location" the legend would be flipped and the user would not know which is the correct one.
    option_choice = sorted(option_choice)
    # If they choose that they want to see location only
    if "Location" in option_choice and "Material" not in option_choice and "Function" not in option_choice:
        # Asking which locations they want to see and limiting them at five because if there is more than 5 the charts look messy
        location_choice = st.sidebar.multiselect("Please select the cities you would like to view (Limit of 5)", cities)
        if len(location_choice) > 5:
            st.write("There are too many cities chosen please select less cities")
        elif len(location_choice) > 0:
            # Creating charts
            chart_creator(chart_choice)
    # If they choose that they want to see material only
    if "Location" not in option_choice and "Material" in option_choice and "Function" not in option_choice:
        # Asking which locations they want to see and limiting them at five because if there is more than 5 the charts look messy
        material_choice = st.sidebar.multiselect("Please select the materials", materials)
        if len(material_choice) > 0:
            # Creating charts
            chart_creator(chart_choice)
    # If they choose that they want to see function only
    if "Location" not in option_choice and "Material" not in option_choice and "Function" in option_choice:
        # Asking which locations they want to see and limiting them at five because if there is more than 5 the charts look messy
        function_choice = st.sidebar.multiselect("Please select the functions", functions)
        if len(function_choice) > 0:
            # Creating charts
            chart_creator(chart_choice)
    # If they choose that they want to see location and material only
    if "Location" in option_choice and "Material" in option_choice and "Function" not in option_choice:
        # Asking which locations they want to see and limiting them at five because if there is more than 5 the charts look messy
        location_choice = st.sidebar.multiselect("Please select the cities you would like to view (Limit of 5)", cities)
        material_choice = st.sidebar.multiselect("Please select the materials", materials)
        if len(location_choice) > 5:
            st.write("There are too many cities chosen please select less cities")
        elif len(location_choice) and len(material_choice) > 0:
            # Creating charts
            chart_creator(chart_choice)
    # If they choose that they want to see location and function only
    if "Location" in option_choice and "Material" not in option_choice and "Function" in option_choice:
        # Asking which locations they want to see and limiting them at five because if there is more than 5 the charts look messy
        location_choice = st.sidebar.multiselect("Please select the cities you would like to view (Limit of 5)", cities)
        function_choice = st.sidebar.multiselect("Please select the functions", functions)
        if len(location_choice) > 5:
            st.write("There are too many cities chosen please select less cities")
        elif len(location_choice) and len(function_choice) > 0:
            # Creating charts
            chart_creator(chart_choice)
    # If they choose that they want to see material and function only
    if "Location" not in option_choice and "Material" in option_choice and "Function" in option_choice:
        # Asking which locations they want to see and limiting them at five because if there is more than 5 the charts look messy
        function_choice = st.sidebar.multiselect("Please select the functions", functions)
        material_choice = st.sidebar.multiselect("Please select the materials", materials)
        if len(function_choice) and len(material_choice) > 0:
            # Creating charts
            chart_creator(chart_choice)
    # If they choose that they want to see material, location, and function only
    if "Location" in option_choice and "Material" in option_choice and "Function" in option_choice:
        # Asking which locations they want to see and limiting them at five because if there is more than 5 the charts look messy
        location_choice = st.sidebar.multiselect("Please select the cities you would like to view (Limit of 5)", cities)
        function_choice = st.sidebar.multiselect("Please select the functions", functions)
        material_choice = st.sidebar.multiselect("Please select the materials", materials)
        if len(location_choice) > 5:
            st.write("There are too many cities chosen please select less cities")
        elif len(location_choice) > 0 and len(function_choice) > 0 and len(material_choice) > 0:
            # Creating charts
            chart_creator(chart_choice)



