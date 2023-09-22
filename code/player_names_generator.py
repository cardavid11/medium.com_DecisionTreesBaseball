# import pandas as pd
# import numpy as np
# import random

# # Define 100 fictional player names
# player_names = ["James_A", "Derek_B", "William_C", "Daniel_D", "Edward_E", "Frank_F", 
#                 "Gregory_G", "Harrison_H", "Isaac_I", "Jack_J", "Kevin_K", "Leo_L",
#                 "Mike_M", "Ned_N", "Oscar_O", "Paul_P", "Quinn_Q", "Ron_R", "Sam_S",
#                 "Tom_T", "Ulysses_U", "Victor_V", "Walter_W", "Xander_X", "Yankee_Y",
#                 "Zack_Z"] + [f"Player_{i}" for i in range(75)]

# # Function to generate random baseball stats for each player
# def generate_data():
#     return {
#         "Batting_Avg": round(np.random.uniform(0.200, 0.350), 3),
#         "Home_Runs": np.random.randint(0, 41),
#         "RBIs": np.random.randint(20, 121),
#         "Walks": np.random.randint(15, 101),
#         "Strikeouts": np.random.randint(50, 201),
#         "Fielding_Percentage": round(np.random.uniform(0.950, 1.000), 3),
#         "All_Star": np.random.choice([0, 1])
#     }

# # Generate the dataframe
# data = pd.DataFrame({
#     "Player": player_names,
#     **{key: [generate_data()[key] for _ in player_names] for key in ["Batting_Avg", "Home_Runs", "RBIs", "Walks", "Strikeouts", "Fielding_Percentage", "All_Star"]}
# })

# # Save dataframe to a CSV file
# data.to_csv('generated_baseball_data.csv', index=False)

# print(f"Data saved to generated_baseball_data.csv")

import pandas as pd
import random

# List of player names
players = ["Player" + str(i) for i in range(1, 101)]

# Generating random data for other features
data = {
    'Player': players,
    'Games_Played': [random.randint(50, 162) for _ in range(100)],
    'At_Bats': [random.randint(100, 600) for _ in range(100)],
    'Runs': [random.randint(0, 120) for _ in range(100)],
    'Hits': [random.randint(0, 200) for _ in range(100)],
    'Doubles': [random.randint(0, 50) for _ in range(100)],
    'Triples': [random.randint(0, 20) for _ in range(100)],
    'Home_Runs': [random.randint(0, 50) for _ in range(100)],
    # ... add other statistics
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Adding the MVP feature based on home run count
df['MVP'] = df['Home_Runs'].apply(lambda x: 1 if x > 35 else 0)

# Saving to a CSV file
df.to_csv('generated_baseball_data.csv', index=False)