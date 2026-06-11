import pandas as pd
import os

def build_graph():

    current_dir = os.path.dirname(
        os.path.abspath(__file__)
    )

    csv_path = os.path.join(
        current_dir,
        "hospital.csv"
    )

    df = pd.read_csv(csv_path)

    graph = {

        "Denpasar": {
            "RSUP Sanglah": 3,
            "RS BaliMed": 5
        },

        "RSUP Sanglah": {
            "Denpasar": 3,
            "Sanur": 4,
            "Nusa Dua": 8,
            "RS BaliMed": 5,
            "RS Kasih Ibu": 8
        },

        "RS BaliMed": {
            "Denpasar": 5,
            "Kuta": 7,
            "Jimbaran": 6,
            "Nusa Dua": 7,
            "RSUP Sanglah": 5,
            "RS Kasih Ibu": 3,
            "RS Surya Husadha": 4
        },

        "RS Kasih Ibu": {
            "Kuta": 6,
            "Ubud": 8,
            "RSUP Sanglah": 8,
            "RS BaliMed": 3,
            "RS Surya Husadha": 2
        },

        "RS Surya Husadha": {
            "Jimbaran": 5,
            "RS BaliMed": 4,
            "RS Kasih Ibu": 2
        },

        "Sanur": {
            "RSUP Sanglah": 4
        },

        "Ubud": {
            "RS Kasih Ibu": 8
        },

        "Jimbaran": {
            "RS BaliMed": 6,
            "RS Surya Husadha": 5
        },

        "Nusa Dua": {
            "RS BaliMed": 7,
            "RSUP Sanglah": 8
        }
    }
    return graph, df
