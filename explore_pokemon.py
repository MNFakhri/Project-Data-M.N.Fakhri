import streamlit as st
from plotly import subplots
from plotly import graph_objs as go
from plotly.offline import init_notebook_mode
import numpy as np
import pandas as pd
init_notebook_mode(connected=True)

data = pd.read_csv("Pokemon.csv")
data.rename(columns={"#":"ID"},inplace=True)
data.fillna("None",inplace=True)
list_type1 = data["Type 1"].unique()
list_type2 = data["Type 2"].unique()
list_generation = data["Generation"].unique()
list_legendary = data["Legendary"].unique()
list_columns = data.columns.values

colours = ["#00FFFF","#7FFFD4","#000000","#0000FF","#8A2BE2","#A52A2A","#DEB887","#5F9EA0","#7FFF00","#D2691E",
            "#FF7F50","#6495ED","#DC143C","#00FFFF","#00008B","#008B8B","#B8860B","#A9A9A9","#006400","#BDB76B",
            "#8B008B","#556B2F","#FF8C00","#9932CC","#8B0000","#E9967A","#8FBC8F","#483D8B","#2F4F4F","#00CED1",
            "#9400D3","#FF1493","#00BFFF","#696969","#1E90FF","#B22222","#228B22","#FF00FF","#FFD700","#DAA520",
            "#808080","#008000","#ADFF2F","#FF69B4","#CD5C5C","#4B0082","#F0E68C","#7CFC00","#ADD8E6","#F08080",
            "#90EE90","#FFB6C1","#FFA07A","#20B2AA","#87CEFA","#778899","#B0C4DE","#00FF00","#32CD32","#FF00FF",
            "#800000","#66CDAA","#0000CD","#BA55D3","#9370DB","#3CB371","#7B68EE","#00FA9A","#48D1CC","#C71585",
            "#191970","#FFE4B5","#FFDEAD","#000080","#808000","#6B8E23","#FFA500","#FF4500","#DA70D6","#EEE8AA",
            "#98FB98","#AFEEEE","#DB7093","#CD853F","#FFC0CB","#DDA0DD","#B0E0E6","#800080","#663399","#FF0000",
            "#BC8F8F","#4169E1","#8B4513","#FA8072","#F4A460","#2E8B57","#A0522D","#C0C0C0","#87CEEB","#6A5ACD",
            "#708090","#00FF7F","#4682B4","#D2B48C","#008080","#D8BFD8","#FF6347","#40E0D0","#EE82EE","#F5DEB3",
            "#FFFF00","#9ACD32"]

amount_type1 = []
for a in list_type1:
    type1_list = data[data["Type 1"] == a]
    amount_type1.append(len(type1_list))
type1_bar = go.Bar(x=list_type1,y=amount_type1,marker=dict(color=colours[:len(amount_type1)]))
type1_layout = go.Layout(title={"text":"<b>Amount Of Pokemon Based On Type 1</b>","y":0.92,"x":0.5,
                        "xanchor":"center","yanchor":"top"},height=600,margin=go.layout.Margin())
data_type1 = [type1_bar]
type1_figure = go.Figure(data=data_type1,layout=type1_layout)

amount_type2 = []
for b in list_type1:
    type2_list = data[data["Type 2"] == b]
    amount_type2.append(len(type2_list))
type2_bar = go.Bar(x=list_type1,y=amount_type2,marker=dict(color=colours[:len(amount_type2)]))
type2_layout = go.Layout(title={"text":"<b>Amount Of Pokemon Based On Type 2</b>","y":0.92,"x":0.5,
                        "xanchor":"center","yanchor":"top"},height=600,margin=go.layout.Margin())
data_type2 = [type2_bar]
type2_figure = go.Figure(data=data_type2,layout=type2_layout)

amount_type_all = []
for c in list_type1:
    type_list_1 = data["Type 1"] == c
    type_list_2 = data["Type 2"] == c
    amount_type_all.append(len(data[type_list_1 | type_list_2]))
type_bar = go.Bar(x=list_type1,y=amount_type_all,marker=dict(color=colours[:len(amount_type_all)]))
type_layout = go.Layout(title={"text":"<b>Amount Of Pokemon Based On All Type</b>","y":0.92,"x":0.5,
                        "xanchor":"center","yanchor":"top"},height=600,margin=go.layout.Margin())
data_type = [type_bar]
type_figure = go.Figure(data=data_type,layout=type_layout)

amount_type_join = []
amount_type_join1 = []
amount_type_join2 = []
amount_type_join3 = []
amount_type_join4 = []
amount_type_join5 = []
amount_type_join6 = []
for f in list_type1:
    type1_join = data["Type 1"] == f
    type2_join = data["Type 2"] == f
    amount_type_all_join = type1_join | type2_join
    amount_type_join.append(len(data[amount_type_all_join]))
    amount_type_join1.append(len(data[amount_type_all_join & (data["Generation"] == 1)]))
    amount_type_join2.append(len(data[amount_type_all_join & (data["Generation"] == 2)]))
    amount_type_join3.append(len(data[amount_type_all_join & (data["Generation"] == 3)]))
    amount_type_join4.append(len(data[amount_type_all_join & (data["Generation"] == 4)]))
    amount_type_join5.append(len(data[amount_type_all_join & (data["Generation"] == 5)]))
    amount_type_join6.append(len(data[amount_type_all_join & (data["Generation"] == 6)]))
gen_bar1 = go.Bar(x=list_type1,y=amount_type_join1,marker=dict(color=colours[:len(amount_type_join)]),name="Gen 1")
gen_bar2 = go.Bar(x=list_type1,y=amount_type_join2,marker=dict(color=colours[:len(amount_type_join)]),name="Gen 2")
gen_bar3 = go.Bar(x=list_type1,y=amount_type_join3,marker=dict(color=colours[:len(amount_type_join)]),name="Gen 3")
gen_bar4 = go.Bar(x=list_type1,y=amount_type_join4,marker=dict(color=colours[:len(amount_type_join)]),name="Gen 4")
gen_bar5 = go.Bar(x=list_type1,y=amount_type_join5,marker=dict(color=colours[:len(amount_type_join)]),name="Gen 5")
gen_bar6 = go.Bar(x=list_type1,y=amount_type_join6,marker=dict(color=colours[:len(amount_type_join)]),name="Gen 6")
figure = subplots.make_subplots(rows=3,cols=2,subplot_titles=("Generation 1","Generation 2","Generation 3",
                                                            "Generation 4","Generation 5","Generation 6"))
figure.append_trace(gen_bar1, 1,1)
figure.append_trace(gen_bar2, 1,2)
figure.append_trace(gen_bar3, 2,1)
figure.append_trace(gen_bar4, 2,2)
figure.append_trace(gen_bar5, 3,1)
figure.append_trace(gen_bar6, 3,2)
figure["layout"].update(title={"text":"<b>Amount Of Pokemon Based On Type In Each Generation</b>","y":0.96,
                            "x":0.5,"xanchor":"center","yanchor":"top"},height=1000,margin=go.layout.Margin(),
                            showlegend=False)

@st.cache(suppress_st_warning=True)
def make_graph_hor(h):
    mean_type = []
    for g in list_type1:
        type_1 = data["Type 1"] == g
        type_2 = data["Type 2"] == g
        type_value = type_1 | type_2
        data_type = data[type_value]
        total_mean = data_type[h].mean()
        mean_type.append(total_mean)
    type_mean_bar = go.Bar(x = mean_type,y = list_type1,orientation = "h",
                            marker=dict(color=colours[:len(mean_type)]))
    type_mean_layout = go.Layout(title={"text":f"<b>Average Stats Of {h} Based On Type</b>","y":0.93,"x":0.5,
                                        "xanchor":"center","yanchor":"top"},height=700,margin=go.layout.Margin())
    data_type_bar = [type_mean_bar]
    mean_fig = go.Figure(data=data_type_bar, layout=type_mean_layout)
    st.plotly_chart(mean_fig)

mean_type_all = []
mean_type_hp = []
mean_type_atk = []
mean_type_def = []
mean_type_sp_atk = []
mean_type_sp_def = []
mean_type_speed = []
for i in list_type1:
    type1_all = data["Type 1"] == i
    type2_all = data["Type 2"] == i
    type_value_all = type1_all | type2_all
    data_type_all = data[type_value_all]
    hp_mean_all = data_type_all["HP"].mean()
    atk_mean_all = data_type_all["Attack"].mean()
    def_mean_all = data_type_all["Defense"].mean()
    sp_atk_mean_all = data_type_all["Sp. Atk"].mean()
    sp_def_mean_all = data_type_all["Sp. Def"].mean()
    speed_mean_all = data_type_all["Speed"].mean()
    mean_type_all.append(data_type_all)
    mean_type_hp.append(hp_mean_all)
    mean_type_atk.append(atk_mean_all)
    mean_type_def.append(def_mean_all)
    mean_type_sp_atk.append(sp_atk_mean_all)
    mean_type_sp_def.append(sp_def_mean_all)
    mean_type_speed.append(speed_mean_all)
hp_bar = go.Bar(x=mean_type_hp,y=list_type1,orientation="h",marker=dict(color=colours[:len(mean_type_all)]),
                name="HP")
atk_bar = go.Bar(x=mean_type_atk,y=list_type1,orientation="h",marker=dict(color=colours[:len(mean_type_all)]),
                name="Attack")
def_bar = go.Bar(x=mean_type_def,y=list_type1,orientation="h",marker=dict(color=colours[:len(mean_type_all)]),
                name="Defense")
sp_atk_bar = go.Bar(x=mean_type_sp_atk,y=list_type1,orientation="h",marker=dict(color=colours[:len(mean_type_all)]),
                    name="Sp. Atk")
sp_def_bar = go.Bar(x=mean_type_sp_def,y=list_type1,orientation="h",marker=dict(color=colours[:len(mean_type_all)]),
                    name="Sp. Def")
speed_bar = go.Bar(x=mean_type_speed,y=list_type1,orientation="h",marker=dict(color=colours[:len(mean_type_all)]),
                    name="Speed")
figure_all = subplots.make_subplots(rows=3,cols=2,vertical_spacing=0.05,
                                    subplot_titles=("Average HP","Average Attack","Average Defense",
                                                    "Average Sp. Atk","Average Sp. Def","Average Speed",))
figure_all.append_trace(hp_bar, 1,1)
figure_all.append_trace(atk_bar, 1,2)
figure_all.append_trace(def_bar, 2,1)
figure_all.append_trace(sp_atk_bar, 2,2)
figure_all.append_trace(sp_def_bar, 3,1)
figure_all.append_trace(speed_bar, 3,2)
figure_all["layout"].update(title={"text":"<b>Comparison Average Stats Based On Type</b>","y":0.97,"x":0.5,
                                "xanchor":"center","yanchor":"top"},height=1500,margin=go.layout.Margin(),
                                showlegend=False)

data_gen1 = data[data["Generation"]==1]
data_gen2 = data[data["Generation"]==2]
data_gen3 = data[data["Generation"]==3]
data_gen4 = data[data["Generation"]==4]
data_gen5 = data[data["Generation"]==5]
data_gen6 = data[data["Generation"]==6]

mean_total_gen1 = data_gen1["Total"].mean()
mean_total_gen2 = data_gen2["Total"].mean()
mean_total_gen3 = data_gen3["Total"].mean()
mean_total_gen4 = data_gen4["Total"].mean()
mean_total_gen5 = data_gen5["Total"].mean()
mean_total_gen6 = data_gen6["Total"].mean()

mean_hp_gen1 = data_gen1["HP"].mean()
mean_hp_gen2 = data_gen2["HP"].mean()
mean_hp_gen3 = data_gen3["HP"].mean()
mean_hp_gen4 = data_gen4["HP"].mean()
mean_hp_gen5 = data_gen5["HP"].mean()
mean_hp_gen6 = data_gen6["HP"].mean()

mean_attack_gen1 = data_gen1["Attack"].mean()
mean_attack_gen2 = data_gen2["Attack"].mean()
mean_attack_gen3 = data_gen3["Attack"].mean()
mean_attack_gen4 = data_gen4["Attack"].mean()
mean_attack_gen5 = data_gen5["Attack"].mean()
mean_attack_gen6 = data_gen6["Attack"].mean()

mean_defense_gen1 = data_gen1["Defense"].mean()
mean_defense_gen2 = data_gen2["Defense"].mean()
mean_defense_gen3 = data_gen3["Defense"].mean()
mean_defense_gen4 = data_gen4["Defense"].mean()
mean_defense_gen5 = data_gen5["Defense"].mean()
mean_defense_gen6 = data_gen6["Defense"].mean()

mean_sp_atk_gen1 = data_gen1["Sp. Atk"].mean()
mean_sp_atk_gen2 = data_gen2["Sp. Atk"].mean()
mean_sp_atk_gen3 = data_gen3["Sp. Atk"].mean()
mean_sp_atk_gen4 = data_gen4["Sp. Atk"].mean()
mean_sp_atk_gen5 = data_gen5["Sp. Atk"].mean()
mean_sp_atk_gen6 = data_gen6["Sp. Atk"].mean()

mean_sp_def_gen1 = data_gen1["Sp. Def"].mean()
mean_sp_def_gen2 = data_gen2["Sp. Def"].mean()
mean_sp_def_gen3 = data_gen3["Sp. Def"].mean()
mean_sp_def_gen4 = data_gen4["Sp. Def"].mean()
mean_sp_def_gen5 = data_gen5["Sp. Def"].mean()
mean_sp_def_gen6 = data_gen6["Sp. Def"].mean()

mean_speed_gen1 = data_gen1["Speed"].mean()
mean_speed_gen2 = data_gen2["Speed"].mean()
mean_speed_gen3 = data_gen3["Speed"].mean()
mean_speed_gen4 = data_gen4["Speed"].mean()
mean_speed_gen5 = data_gen5["Speed"].mean()
mean_speed_gen6 = data_gen6["Speed"].mean()

stats_type = ["HP","Attack","Defense","Sp. Atk","Sp. Def","Speed"]
data_total_mean = [mean_total_gen1,mean_total_gen2,mean_total_gen3,mean_total_gen4,mean_total_gen5,mean_total_gen6]

@st.cache(suppress_st_warning=True)
def make_scatter(j):
    if j == "Total":
        k = data_total_mean
        data_scatter = go.Scatter(x=list_generation,y=k,name=f"Avg {j} Stats")
        data_layout = go.Layout(title={"text":f"<b>Average {j} Stats For Each Generation</b>","y":0.91,"x":0.5,
                                    "xanchor":"center","yanchor":"top"},height=500,margin=go.layout.Margin(),
                                    showlegend=True)
        data_fig = go.Figure(data=data_scatter,layout=data_layout)
        st.plotly_chart(data_fig)
    else:
        print("Wrong Type")

mean_all_stats1 = [mean_hp_gen1,mean_attack_gen1,mean_defense_gen1,mean_sp_atk_gen1,mean_sp_def_gen1,
                   mean_speed_gen1]
mean_all_stats2 = [mean_hp_gen2,mean_attack_gen2,mean_defense_gen2,mean_sp_atk_gen2,mean_sp_def_gen2,
                   mean_speed_gen2]
mean_all_stats3 = [mean_hp_gen3,mean_attack_gen3,mean_defense_gen3,mean_sp_atk_gen3,mean_sp_def_gen3,
                   mean_speed_gen3]
mean_all_stats4 = [mean_hp_gen4,mean_attack_gen4,mean_defense_gen4,mean_sp_atk_gen4,mean_sp_def_gen4,
                   mean_speed_gen4]
mean_all_stats5 = [mean_hp_gen5,mean_attack_gen5,mean_defense_gen5,mean_sp_atk_gen5,mean_sp_def_gen5,
                   mean_speed_gen5]
mean_all_stats6 = [mean_hp_gen6,mean_attack_gen6,mean_defense_gen6,mean_sp_atk_gen6,mean_sp_def_gen6,
                   mean_speed_gen6]

all_stats_scatter1 = go.Scatter(x=stats_type,y=mean_all_stats1,name="Gen 1")
all_stats_scatter2 = go.Scatter(x=stats_type,y=mean_all_stats2,name="Gen 2")
all_stats_scatter3 = go.Scatter(x=stats_type,y=mean_all_stats3,name="Gen 3")
all_stats_scatter4 = go.Scatter(x=stats_type,y=mean_all_stats4,name="Gen 4")
all_stats_scatter5 = go.Scatter(x=stats_type,y=mean_all_stats5,name="Gen 5")
all_stats_scatter6 = go.Scatter(x=stats_type,y=mean_all_stats6,name="Gen 6")

stats_data = [all_stats_scatter1,all_stats_scatter2,all_stats_scatter3,all_stats_scatter4,all_stats_scatter5,
              all_stats_scatter6]
all_stats_layout = go.Layout(title={"text":"<b>Comparison Every Average Stats For Each Generation</b>","y":0.91,
                                    "x":0.5,"xanchor":"center","yanchor":"top"},height=500,
                                    margin=go.layout.Margin(),showlegend=True)
all_stats_figure = go.Figure(data=stats_data,layout=all_stats_layout)

amount_1type = len(data[data["Type 2"] == "None"])
amount_2type = len(data[data["Type 2"] != "None"])
type_label = ["1 Type","2 Type"]
type_value_data = [amount_1type,amount_2type]
type_pie = go.Pie(labels=type_label,values=type_value_data)
type_pie_layout = go.Layout(title={"text":f"<b>Comparison 1 Type And 2 Type Pokemon in %</b>","y":0.90,"x":0.5,
                                    "xanchor":"center","yanchor":"top"},showlegend=True)
type_pie_data = [type_pie]
type_pie_fig = go.Figure(data=type_pie_data,layout=type_pie_layout)

amount_non_legendary = len(data[data["Legendary"] == False])
amount_legendary = len(data[data["Legendary"] == True])
legendary_pie_label = ["Non-Legendary","Legendary"]
legendary_pie_value = [amount_non_legendary,amount_legendary]
legendary_pie_trace = go.Pie(labels=legendary_pie_label,values=legendary_pie_value)
legendary_pie_layout = go.Layout(title={"text":f"<b>Comparison Non-Legendary And Legendary Pokemon in %</b>",
                                        "y":0.90,"x":0.5,"xanchor":"center","yanchor":"top"},showlegend=True)
legendary_pie_data = [legendary_pie_trace]
legendary_pie_fig = go.Figure(data=legendary_pie_data,layout=legendary_pie_layout)

amount_non_legen1 = len(data[(data["Generation"]==1) & (data["Legendary"]==False)])
amount_non_legen2 = len(data[(data["Generation"]==2) & (data["Legendary"]==False)])
amount_non_legen3 = len(data[(data["Generation"]==3) & (data["Legendary"]==False)])
amount_non_legen4 = len(data[(data["Generation"]==4) & (data["Legendary"]==False)])
amount_non_legen5 = len(data[(data["Generation"]==5) & (data["Legendary"]==False)])
amount_non_legen6 = len(data[(data["Generation"]==6) & (data["Legendary"]==False)])

amount_legen1 = len(data[(data["Generation"] == 1) & (data["Legendary"]==True)])
amount_legen2 = len(data[(data["Generation"] == 2) & (data["Legendary"]==True)])
amount_legen3 = len(data[(data["Generation"] == 3) & (data["Legendary"]==True)])
amount_legen4 = len(data[(data["Generation"] == 4) & (data["Legendary"]==True)])
amount_legen5 = len(data[(data["Generation"] == 5) & (data["Legendary"]==True)])
amount_legen6 = len(data[(data["Generation"] == 6) & (data["Legendary"]==True)])

legen_pie_label1 = ["Non-Legendary Gen 1","Legendary Gen 1"]
legen_pie_label2 = ["Non-Legendary Gen 2","Legendary Gen 2"]
legen_pie_label3 = ["Non-Legendary Gen 3","Legendary Gen 3"]
legen_pie_label4 = ["Non-Legendary Gen 4","Legendary Gen 4"]
legen_pie_label5 = ["Non-Legendary Gen 5","Legendary Gen 5"]
legen_pie_label6 = ["Non-Legendary Gen 6","Legendary Gen 6"]

legen_pie_value1 = [amount_non_legen1,amount_legen1]
legen_pie_value2 = [amount_non_legen2,amount_legen2]
legen_pie_value3 = [amount_non_legen3,amount_legen3]
legen_pie_value4 = [amount_non_legen4,amount_legen4]
legen_pie_value5 = [amount_non_legen5,amount_legen5]
legen_pie_value6 = [amount_non_legen6,amount_legen6]

specs = [[{"type":"domain"},{"type":"domain"}],[{"type":"domain"},{"type":"domain"}],[{"type":"domain"},
        {"type":"domain"}]]
fig_pie = subplots.make_subplots(rows=3,cols=2,specs=specs,subplot_titles=("Generation 1","Generation 2",
                                                                        "Generation 3","Generation 4",
                                                                        "Generation 5","Generation 6"))
fig_pie.add_traces(go.Pie(labels=legen_pie_label1,values=legen_pie_value1,name="Pie Gen 1"), 1,1)
fig_pie.add_traces(go.Pie(labels=legen_pie_label2,values=legen_pie_value2,name="Pie Gen 2"), 1,2)
fig_pie.add_traces(go.Pie(labels=legen_pie_label3,values=legen_pie_value3,name="Pie Gen 3"), 2,1)
fig_pie.add_traces(go.Pie(labels=legen_pie_label4,values=legen_pie_value4,name="Pie Gen 4"), 2,2)
fig_pie.add_traces(go.Pie(labels=legen_pie_label5,values=legen_pie_value5,name="Pie Gen 5"), 3,1)
fig_pie.add_traces(go.Pie(labels=legen_pie_label6,values=legen_pie_value6,name="Pie Gen 6"), 3,2)
fig_pie.update_traces(textposition="inside")
fig_pie["layout"].update(title={"text":"<b>Percentage Of Non-Legendary And Legendary Pokemon In Each Generation</b>",
                                "y":0.96,"x":0.5,"xanchor":"center","yanchor":"top"},height=1000,
                                margin=go.layout.Margin(),showlegend=False)

data_non_legendary = data[data["Legendary"]==False]
stats_non_legendary = []
for m in stats_type:
    mean_non_legendary = data_non_legendary[m].mean()
    stats_non_legendary.append(mean_non_legendary)

data_legendary = data[data["Legendary"]==True]
stats_legendary = []
for n in stats_type:
    mean_legendary = data_legendary[n].mean()
    stats_legendary.append(mean_legendary)

data_scatter_polar = [go.Scatterpolar(r=stats_legendary,theta=stats_type,fill="toself",name="Legendary"),
                      go.Scatterpolar(r=stats_non_legendary,theta=stats_type,fill="toself",name="Non-Legendary")]
data_scatter_layout = go.Layout(title={"text":"<b>Comparison Of Non-Legendary And Legendary Pokemon's Stats</b>",
                                        "y":0.91,"x":0.5,"xanchor":"center","yanchor":"top"},showlegend=True)

scatter_polar_fig = go.Figure(data=data_scatter_polar,layout=data_scatter_layout)

non_legendary_data1 = data[(data["Generation"]==1)&(data["Legendary"]==False)]
non_legendary_data2 = data[(data["Generation"]==2)&(data["Legendary"]==False)]
non_legendary_data3 = data[(data["Generation"]==3)&(data["Legendary"]==False)]
non_legendary_data4 = data[(data["Generation"]==4)&(data["Legendary"]==False)]
non_legendary_data5 = data[(data["Generation"]==5)&(data["Legendary"]==False)]
non_legendary_data6 = data[(data["Generation"]==6)&(data["Legendary"]==False)]
non_legendary_stats1 = []
non_legendary_stats2 = []
non_legendary_stats3 = []
non_legendary_stats4 = []
non_legendary_stats5 = []
non_legendary_stats6 = []
for r in stats_type:
    non_legendary_mean1 = non_legendary_data1[r].mean()
    non_legendary_mean2 = non_legendary_data2[r].mean()
    non_legendary_mean3 = non_legendary_data3[r].mean()
    non_legendary_mean4 = non_legendary_data4[r].mean()
    non_legendary_mean5 = non_legendary_data5[r].mean()
    non_legendary_mean6 = non_legendary_data6[r].mean()
    non_legendary_stats1.append(non_legendary_mean1)
    non_legendary_stats2.append(non_legendary_mean2)
    non_legendary_stats3.append(non_legendary_mean3)
    non_legendary_stats4.append(non_legendary_mean4)
    non_legendary_stats5.append(non_legendary_mean5)
    non_legendary_stats6.append(non_legendary_mean6)
    
legendary_data1 = data[(data["Generation"]==1)&(data["Legendary"]==True)]
legendary_data2 = data[(data["Generation"]==2)&(data["Legendary"]==True)]
legendary_data3 = data[(data["Generation"]==3)&(data["Legendary"]==True)]
legendary_data4 = data[(data["Generation"]==4)&(data["Legendary"]==True)]
legendary_data5 = data[(data["Generation"]==5)&(data["Legendary"]==True)]
legendary_data6 = data[(data["Generation"]==6)&(data["Legendary"]==True)]
legendary_stats1 = []
legendary_stats2 = []
legendary_stats3 = []
legendary_stats4 = []
legendary_stats5 = []
legendary_stats6 = []
for s in stats_type:
    legendary_mean1 = legendary_data1[s].mean()
    legendary_mean2 = legendary_data2[s].mean()
    legendary_mean3 = legendary_data3[s].mean()
    legendary_mean4 = legendary_data4[s].mean()
    legendary_mean5 = legendary_data5[s].mean()
    legendary_mean6 = legendary_data6[s].mean()
    legendary_stats1.append(legendary_mean1)
    legendary_stats2.append(legendary_mean2)
    legendary_stats3.append(legendary_mean3)
    legendary_stats4.append(legendary_mean4)
    legendary_stats5.append(legendary_mean5)
    legendary_stats6.append(legendary_mean6)

specs = [[{"type":"polar"},{"type":"polar"}],[{"type":"polar"},{"type":"polar"}],[{"type":"polar"},{"type":"polar"}]]
fig_scatter = subplots.make_subplots(rows=3,cols=2,specs=specs,subplot_titles=("Generation 1","Generation 2",
                                                                                "Generation 3","Generation 4",
                                                                                "Generation 5","Generation 6"))

scatter_polar1 = [go.Scatterpolar(r=legendary_stats1,theta=stats_type,fill="toself",name="Legendary Generation 1"),
                  go.Scatterpolar(r=non_legendary_stats1,theta=stats_type,fill="toself",
                  name="Non-Legendary Generation 1")]
scatter_polar2 = [go.Scatterpolar(r=legendary_stats2,theta=stats_type,fill="toself",name="Legendary Generation 2"),
                  go.Scatterpolar(r=non_legendary_stats2,theta=stats_type,fill="toself",
                  name="Non-Legendary Generation 2")]
scatter_polar3 = [go.Scatterpolar(r=legendary_stats3,theta=stats_type,fill="toself",name="Legendary Generation 3"),
                  go.Scatterpolar(r=non_legendary_stats3,theta=stats_type,fill="toself",
                  name="Non-Legendary Generation 3")]
scatter_polar4 = [go.Scatterpolar(r=legendary_stats4,theta=stats_type,fill="toself",name="Legendary Generation 4"),
                  go.Scatterpolar(r=non_legendary_stats4,theta=stats_type,fill="toself",
                  name="Non-Legendary Generation 4")]
scatter_polar5 = [go.Scatterpolar(r=legendary_stats5,theta=stats_type,fill="toself",name="Legendary Generation 5"),
                  go.Scatterpolar(r=non_legendary_stats5,theta=stats_type,fill="toself",
                  name="Non-Legendary Generation 5")]
scatter_polar6 = [go.Scatterpolar(r=legendary_stats6,theta=stats_type,fill="toself",name="Legendary Generation 6"),
                  go.Scatterpolar(r=non_legendary_stats6,theta=stats_type,fill="toself",
                  name="Non-Legendary Generation 6")]

fig_scatter.add_traces(scatter_polar1, 1,1)
fig_scatter.add_traces(scatter_polar2, 1,2)
fig_scatter.add_traces(scatter_polar3, 2,1)
fig_scatter.add_traces(scatter_polar4, 2,2)
fig_scatter.add_traces(scatter_polar5, 3,1)
fig_scatter.add_traces(scatter_polar6, 3,2)
fig_scatter["layout"].update(
                    title={"text":"<b>Comparison Non-Legendary And Legendary Pokemon's Stats Every Generation</b>",
                    "y":0.96,"x":0.5,"xanchor":"center","yanchor":"top"},height=1000,margin=go.layout.Margin(),
                    showlegend=False)

array1 = np.array([])
array2 = []
array3 = np.array([])
for t in list_generation: 
    for u in list_type1:
        type1_criteria = data["Type 1"] == u
        generation_criteria = data["Generation"] == t
        array2_value = len(data[type1_criteria & generation_criteria])
        array2.append(array2_value)
    array1 = np.append(array1,[array2])
    array2.clear()
array3 = np.reshape(array1,(len(list_generation),len(list_type1)))

heatmap_trace1 = go.Heatmap(z=array3,x=list_type1,y=list_generation,colorscale="Hot",reversescale=True)

heatmap_layout1 = go.Layout(title={"text":"<b>Correlation Between Type 1 And Generations</b>","y":0.89,"x":0.5,
                                "xanchor":"center","yanchor":"top"},xaxis=dict(title="<b>Type 1</b>"),
                                yaxis=dict(title="<b>Generation</b>"),height=500)

data_heatmap1=[heatmap_trace1]
heatmap_figure1 = go.Figure(data=data_heatmap1, layout=heatmap_layout1)

array21 = np.array([])
array22 = []
array23 = np.array([])
for v in list_generation: 
    for w in list_type2:
        type2_criteria = data["Type 2"] == w
        generation_criteria = data["Generation"] == v
        array22_value = len(data[type2_criteria & generation_criteria])
        array22.append(array22_value)
    array21 = np.append(array21,[array22])
    array22.clear()
array23 = np.reshape(array21,(len(list_generation),len(list_type2)))

heatmap_trace2 = go.Heatmap(z=array23,x=list_type2,y=list_generation,colorscale="Hot",reversescale=True)

heatmap_layout2 = go.Layout(title={"text":"<b>Correlation Between Type 2 And Generations</b>","y":0.89,"x":0.5,
                                "xanchor":"center","yanchor":"top"},xaxis=dict(title="<b>Type 2</b>"),
                                yaxis=dict(title="<b>Generation</b>"),height=500)

data_heatmap2=[heatmap_trace2]
heatmap_figure2 = go.Figure(data=data_heatmap2, layout=heatmap_layout2)

list_sidebar = ["Amount Of Each Type","Average Stats Each Type","Average Stats Each Generation",
                "1 Type And 2 Type","Legendary and Non-Legendary Pokemon","Non-Legendary And Legendary Stats",
                "Correlation Type and Generation"]

list_type = ["Type 1","Type 2","Type 1 And Type 2","Each Generation"]

st.title("Exploring Pokemon Through Visualization")
st.write("In this case we will exploring Pokemon dataset with visualize it so you can understand about Pokemon.")

sidebar_selection = st.sidebar.selectbox("Choose what you want to see",list_sidebar)
if sidebar_selection == "Amount Of Each Type":
    st.write("1. Identifying Amount Of Each Type Pokemon")
    option = st.radio("Select one to show graph",list_type)
    if option == "Type 1":
        st.plotly_chart(type1_figure)
    elif option == "Type 2":
        st.plotly_chart(type2_figure)
    elif option == "Type 1 And Type 2":
        st.plotly_chart(type_figure)
    elif option == "Each Generation":
        st.plotly_chart(figure)
elif sidebar_selection == "Average Stats Each Type":
    st.write("2. Identifying Amount Average Of Pokemon's Stats For Each Type")
    make_graph_hor("Total")
    st.plotly_chart(figure_all)
elif sidebar_selection == "Average Stats Each Generation":
    st.write("3. Identifying Amount Average Of Pokemon's Stats For Each Generation")
    make_scatter("Total")
    st.plotly_chart(all_stats_figure)
elif sidebar_selection == "1 Type And 2 Type":
    st.write("4. Identifying 1 Type Pokemon And 2 Type Pokemon")
    st.plotly_chart(type_pie_fig)
elif sidebar_selection == "Legendary and Non-Legendary Pokemon":
    st.write("5. Identifying Legendary and Non-Legendary Pokemon")
    st.plotly_chart(legendary_pie_fig)
    st.plotly_chart(fig_pie)
elif sidebar_selection == "Non-Legendary And Legendary Stats":
    st.write("6. Identifying Non-Legendary And Legendary Pokemon's Stats")
    st.plotly_chart(scatter_polar_fig)
    st.plotly_chart(fig_scatter)
elif sidebar_selection == "Correlation Type and Generation":
    st.write("7. Identifying Correlation Between Pokemon's Type and Pokemon's Generation")
    st.plotly_chart(heatmap_figure1)
    st.plotly_chart(heatmap_figure2)