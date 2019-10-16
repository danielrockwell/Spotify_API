import json
import pandas as pd
import matplotlib.pyplot as plt
from spotify_api.spotify_scripts.spotify import getTop50
from spotify_api.spotify_scripts.credentials import getToken

credentials = getToken()
df = getTop50(credentials)

print(df)
#
# print(df['tempo'].describe())
#
#
# plt.bar(df['id'],sorted(df['acousticness']), align='center', alpha=0.5,width=1)
# # plt.xticks(y_pos, objects)
# # plt.ylabel('Usage')
# plt.title('Acousticness')

# plt.show()
