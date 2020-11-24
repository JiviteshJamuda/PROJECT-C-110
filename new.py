import pandas as pd
import statistics 
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

def random_data_set(counter):
    data_set = []
    
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        data_set.append(value)
    
    mean = statistics.mean(data_set)
    return mean


def show_graph(mean_list):
    data = mean_list
    mean = statistics.mean(data)
    graph = ff.create_distplot([data], ["reading_time"], show_hist = False)
    graph.add_trace(go.Scatter(x=[mean,mean],y=[0,1], mode="lines", name="reading_time"))
    graph.show()

def setup():
    mean_list = []

    for i in range(0,1000):
        set_of_means = random_data_set(4)
        mean_list.append(set_of_means)
    
    show_graph(mean_list)
    mean = statistics.mean(mean_list)
    print("sampling mean : " + str(mean))

setup()

population_mean = statistics.mean(data)
print("population mean : " + str(population_mean))

def standard_deviation():
    mean_list = []

    for i in range(0,1000):
        set_of_means = random_data_set(4)
        mean_list.append(set_of_means)
    
    stdev = statistics.stdev(mean_list)
    print("stanard deviation for sampling : " + str(stdev))

standard_deviation()

population_stdev = statistics.stdev(data)
print("population standard deviation : " + str(population_stdev))