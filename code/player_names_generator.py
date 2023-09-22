import pandas as pd
import numpy as np
import random

# Define 100 fictional player names
player_names = ["James_A", "Derek_B", "William_C", "Daniel_D", "Edward_E", "Frank_F", 
                "Gregory_G", "Harrison_H", "Isaac_I", "Jack_J", "Kevin_K", "Leo_L",
                "Mike_M", "Ned_N", "Oscar_O", "Paul_P", "Quinn_Q", "Ron_R", "Sam_S",
                "Tom_T", "Ulysses_U", "Victor_V", "Walter_W", "Xander_X", "Yankee_Y",
                "Zack_Z"] + [f"Player_{i}" for i in range(75)]

# Function to generate random baseball stats for each player
def generate_data():
    return {
        "Batting_Avg": round(np.random.uniform(0.200, 0.350), 3),
        "Home_Runs": np.random.randint(0, 41),
        "RBIs": np.random.randint(20, 121),
        "Walks": np.random.randint(15, 101),
        "Strikeouts": np.random.randint(50, 201),
        "Fielding_Percentage": round(np.random.uniform(0.950, 1.000), 3),
        "All_Star": np.random.choice([0, 1])
    }

# Generate the dataframe
data = pd.DataFrame({
    "Player": player_names,
    **{key: [generate_data()[key] for _ in player_names] for key in ["Batting_Avg", "Home_Runs", "RBIs", "Walks", "Strikeouts", "Fielding_Percentage", "All_Star"]}
})

# Save dataframe to a CSV file
data.to_csv('generated_baseball_data.csv', index=False)

print(f"Data saved to generated_baseball_data.csv")
