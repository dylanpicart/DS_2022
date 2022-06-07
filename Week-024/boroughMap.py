boroughMap = [
    {"Borough" : "Brooklyn", "Color" : "green"},
    {"Borough" : "Queens", "Color" : "blue"},
    {"Borough" : "Staten Island", "Color" : "red"},
    {"Borough" : "Bronx", "Color" : "yellow"},
]

for i in range(len(boroughMap)): 0 - 3
    for j in range(0, 2) : 0 - 1
     0, 0
     0, 1
     1, 0
     ...
     axs[i, j].plot()
    
for curDict in boroughMap:
    

years = [2016, 2017]
boroughs = ['Queens', ...]
recdiv = dataframe[dataframe['Year'] == 2016, dataframe['Borough'] == 'Queens']
# df mean which you give column
'''
axs[0, 0].plot(x1, y1)
axs[0, 0].set_title('Brooklyn Total Diversion Rate', fontsize=20)
axs[0, 1].plot(x2, y2, 'tab:orange')
axs[0, 1].set_title('Queens Total Diversion Rate', fontsize=20)
axs[1, 0].plot(x3, y3, 'tab:green')
axs[1, 0].set_title('Manhattan Total Diversion Rate', fontsize=20)
axs[1, 1].plot(x4, y4, 'tab:red')
axs[1, 1].set_title('The Bronx Total Diversion Rate', fontsize=20)
axs[2, 0].plot(x5, y5, 'tab:purple')
axs[2, 0].set_title('Staten Island Total Diversion Rate', fontsize=20)
axs[2][0].set_position([0.325,0.125, .38, .2])
axs[2][1].set_visible(False)
'''


masterDf = [
    {"Borough" : "Queens", "Data" : recdiv[recdiv["Borough"] == "Queens"]},
    {"Borough" : "Brooklyn", "Data" : recdiv[recdiv["Borough"] == "Brooklyn"]},
] 

for curBorough in masterDf:
    curBorough["Data"]["Normalized Capture Rate"] = (curBourugh["Data"]["Capture Rate"] - curBourugh["Data"]["Capture Rate"].min())/(curBourugh["Data"]["Capture Rate"]. max() - curBourugh["Data"]["Capture Rate"].min())
curDf = ["2015", "17.312", "25.0435"]
        ["2016", "21.312", "25.0435"]
        ["2018", "27.312", "25.0435"]
        
        27.312 - 17.312 = 10
        
        10/(27.312 - 17.312) = 1
        
        21.312 - 17.312 = 4
        
        4/(27.312 - 17.312) = 0.4