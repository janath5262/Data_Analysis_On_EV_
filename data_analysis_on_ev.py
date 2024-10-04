# -*- coding: utf-8 -*-
"""Data_Analysis_on_EV.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aQgcseiGjmPY7XfhMX4pPaLxkmoP8of9
"""

import pandas as pd
import numpy as np
import warnings

PATH="/content/dataset.csv"
df=pd.read_csv(PATH)
df

"""# **TASK 1**"""

df.shape

df.columns

df.info()

df.head()

df.tail()

print(df.count())

df.describe()

df.isnull().sum()

df_null = df.fillna(0)
df_null.isnull().sum()

!pip install plotly

import plotly.express as px

"""# **Univariate  Analysis**



"""

fig_ev_type = px.bar(df['Electric Vehicle Type'].value_counts(), title='Count of Electric Vehicle Types')
fig_ev_type.show()

fig_cafv_eligibility = px.bar(df['Clean Alternative Fuel Vehicle (CAFV) Eligibility'].value_counts(),
                              title='Count of CAFV Eligibility')
fig_cafv_eligibility.show()

fig_range = px.histogram(df, x='Electric Range', nbins=30, title='Electric Range Distribution')
fig_range.show()

fig_msrp = px.histogram(df, x='Base MSRP', nbins=50, title='Base MSRP Distribution', range_x = [0, 210000])
fig_msrp.show()

company_counts = df['Make'].value_counts().reset_index()
company_counts.columns = ['Company', 'EV Count']
company_counts = company_counts.sort_values(by='EV Count', ascending=False)

fig_bar = px.bar(company_counts, x='Company', y='EV Count', title='Number of Electric Vehicles by Company')
fig_bar.show()

county_counts = df['County'].value_counts().reset_index()
county_counts.columns = ['County', 'EV Count']

county_counts = county_counts.sort_values(by='EV Count', ascending=False)


fig_bar = px.bar(county_counts, x='County', y='EV Count', title='Number of Electric Vehicles by County')
fig_bar.show()

df_counts = df['Model Year'].value_counts().reset_index()
df_counts.columns = ['Model Year', 'Count']
df_counts.sort_values(by='Model Year', inplace=True)

fig = px.bar(df_counts, x='Model Year', y='Count', title='Electric Vehicles Count by Model Year', labels={'Model Year': 'Model Year', 'Count': 'Count'})
fig.show()

ev_type_counts = df['Electric Vehicle Type'].value_counts().reset_index()
ev_type_counts.columns = ['Electric Vehicle Type', 'EV Count']
ev_type_counts = ev_type_counts.sort_values(by='EV Count', ascending=False)

fig_bar = px.bar(ev_type_counts, x='Electric Vehicle Type', y='EV Count', title='Number of Electric Vehicles by Electric Vehicle Type')
fig_bar.show()

electric_utility_counts = df['Electric Utility'].value_counts().reset_index()
electric_utility_counts.columns = ['Electric Utility', 'EV Count']

fig_bar = px.bar(electric_utility_counts, x='Electric Utility', y='EV Count', title='Electric Vehicles Count by Electric Utility')
fig_bar.show()

"""# **Bivariate Analysis**"""

fig_scatter_ev_range_msrp = px.scatter(df, x='Electric Range', y='Base MSRP', title='Electric Range vs. Base MSRP')
fig_scatter_ev_range_msrp.show()

fig_scatter_ev_range_model_year = px.scatter(df, x='Model Year', y='Electric Range', title='Electric Range vs. Model Year')
fig_scatter_ev_range_model_year.show()

fig_box_ev_type_range = px.box(df, x='Electric Vehicle Type', y='Electric Range', title='Electric Vehicle Type vs. Electric Range')
fig_box_ev_type_range.show()

fig_scatter_model_year_ev_count = px.scatter(df['Model Year'].value_counts(), title='Number of Electric Vehicles by Model Year')
fig_scatter_model_year_ev_count.show()

fig_box = px.box(df, x='Electric Vehicle Type', y='Base MSRP', title='Electric Vehicle Type vs. Base MSRP')
fig_box.show()

fig_scatter_model_year = px.scatter(df, x='Model Year', y='Base MSRP', title='Model Year vs. Base MSRP')
fig_scatter_model_year.show()

fig_box_ev_type = px.violin(df, x='Electric Vehicle Type', y='Electric Range', title='Electric Vehicle Type vs. Electric Range')
fig_box_ev_type.show()

fig_box = px.box(df, x='Clean Alternative Fuel Vehicle (CAFV) Eligibility', y='Electric Range',
                 title='Clean Alternative Fuel Vehicle (CAFV) Eligibility vs. Electric Range',
                 labels={'Clean Alternative Fuel Vehicle (CAFV) Eligibility': 'CAFV Eligibility',
                         'Electric Range': 'Electric Range (miles)'})

fig_box.show()

mean_electric_range = df.groupby('Model Year')['Electric Range'].mean().reset_index()

fig_line = px.line(mean_electric_range, x='Model Year', y='Electric Range', title='Model Year vs. Mean Electric Range',
                   labels={'Model Year': 'Model Year', 'Electric Range': 'Mean Electric Range (miles)'})

fig_line.show()

df_counts = df.groupby(['Model Year', 'Electric Vehicle Type']).size().reset_index(name='Count')

fig_bar = px.bar(df_counts, x='Model Year', y='Count', color='Electric Vehicle Type',
                 title='Count of Different Electric Vehicle Types by Model Year')

fig_bar.show()

"""#**Multivariate Analysis**"""

fig_splof = px.scatter_matrix(df, dimensions=['Electric Range', 'Base MSRP', 'Model Year'],
                              title='Scatter Plot Matrix (SPLOM)')
fig_splof.show()

fig_sunburst = px.sunburst(df, path=['State', 'County', 'City'],
                           title='Sunburst Chart of Electric Vehicles by State, County, and City')
fig_sunburst.show()

fig_3d_scatter = px.scatter_3d(df, x='Electric Range', y='Base MSRP', z='Model Year', color='Electric Vehicle Type',
                               title='3D Scatter Plot of Electric Range, Base MSRP, and Model Year')
fig_3d_scatter.show()

df['EV_Type_Num'] = df['Electric Vehicle Type'].map({'Plug-in Hybrid Electric Vehicle (PHEV)': 1,
                                                     'Battery Electric Vehicle (BEV)': 2,
                                                     'Hybrid Electric Vehicle (HEV)': 3})

fig_parallel_coordinates = px.parallel_coordinates(df, color='EV_Type_Num',
                                                   dimensions=['Electric Range', 'Base MSRP', 'Model Year'],
                                                   title='Parallel Coordinates Plot')
fig_parallel_coordinates

"""# **TASK 2**"""

df['Vehicle Location'].isna().sum()

df['Vehicle Location'].apply(type).value_counts()

df = df[df['Vehicle Location'].notna() & df['Vehicle Location'].str.contains(r'\(\d+.\d+, \d+.\d+\)')]

df['Longitude'] = df['Vehicle Location'].apply(lambda loc: float(loc.split()[1][1:]) if pd.notna(loc) else None)
df['Latitude'] = df['Vehicle Location'].apply(lambda loc: float(loc.split()[2][:-1]) if pd.notna(loc) else None)
location_counts = df.groupby(['Latitude', 'Longitude', 'Postal Code', 'County', "State"]).size().reset_index(name='EV Count')

fig_scatter_map = px.scatter_mapbox(location_counts,
                                    lat='Latitude',
                                    lon='Longitude',
                                    color='EV Count',
                                    size='EV Count',
                                    mapbox_style='carto-positron',
                                    zoom=3,
                                    center={'lat': 37.0902, 'lon': -95.7129},
                                    title='Scatter Map of Electric Vehicle Locations')

fig_scatter_map.show()

"""# **TASK 3**"""

!pip install bar-chart-race

import pandas as pd
import bar_chart_race as bcr
import warnings

data=pd.read_csv(PATH)

data["Make"].unique()

ev_counts=data.groupby(['Model Year','Make']).size().unstack(fill_value=0)

display(bcr.bar_chart_race(
                   df=ev_counts,
                   orientation='h',
                  #  filename='ev_makes_racing_bar_plot.mp4',
                   title='Electric Vehicle Makes Over Years',
                   cmap='tab10',
                   sort='desc',
                   n_bars=10,
                   period_label={'x':0.5,'y':0.95},
                   filter_column_colors=True,
                   period_length=1000,
                   bar_label_size=8,
                   tick_label_size=8,
                   figsize=(6,4)
                   ))

