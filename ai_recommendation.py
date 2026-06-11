def get_specialist(keluhan):

    mapping = {

        "Nyeri Dada": "Jantung",
        "Sesak Nafas": "Paru",
        "Cedera": "Bedah",
        "Sakit Kepala": "Syaraf"
    }

    return mapping.get(
        keluhan,
        "Jantung"
    )
