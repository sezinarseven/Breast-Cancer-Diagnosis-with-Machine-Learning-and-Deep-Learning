import requests

# Define the URL of the API endpoint
url = "http://127.0.0.1:8000/predict/"

data1 = { # Malignant
  "radius_mean": 17.08,
  "texture_mean": 27.15,
  "perimeter_mean": 111.2,
  "area_mean": 930.9,
  "smoothness_mean": 0.09898,
  "compactness_mean": 0.111,
  "concavity_mean": 0.1007,
  "concave_points_mean": 0.06431,
  "symmetry_mean": 0.1793,
  "fractal_dimension_mean": 0.06281,
  "radius_se": 0.9291,
  "texture_se": 1.152,
  "perimeter_se": 6.051,
  "area_se": 115.2,
  "smoothness_se": 0.00874,
  "compactness_se": 0.02219,
  "concavity_se": 0.02721,
  "concave_points_se": 0.01458,
  "symmetry_se": 0.02045,
  "fractal_dimension_se": 0.004417,
  "radius_worst": 22.96,
  "texture_worst": 34.49,
  "perimeter_worst": 152.1,
  "area_worst": 1648,
  "smoothness_worst": 0.16,
  "compactness_worst": 0.2444,
  "concavity_worst": 0.2639,
  "concave_points_worst": 0.1555,
  "symmetry_worst": 0.301,
  "fractal_dimension_worst": 0.0906
}

data2 = { # Benign
  "radius_mean": 11.68,
  "texture_mean": 16.17,
  "perimeter_mean": 75.49,
  "area_mean": 420.5,
  "smoothness_mean": 0.1128,
  "compactness_mean": 0.09263,
  "concavity_mean": 0.04279,
  "concave_points_mean": 0.03132,
  "symmetry_mean": 0.1853,
  "fractal_dimension_mean": 0.06401,
  "radius_se": 0.3713,
  "texture_se": 1.154,
  "perimeter_se": 2.554,
  "area_se": 27.57,
  "smoothness_se": 0.008998,
  "compactness_se": 0.01292,
  "concavity_se": 0.01851,
  "concave_points_se": 0.01167,
  "symmetry_se": 0.02152,
  "fractal_dimension_se": 0.003213,
  "radius_worst": 13.32,
  "texture_worst": 21.59,
  "perimeter_worst": 86.57,
  "area_worst": 549.8,
  "smoothness_worst": 0.1526,
  "compactness_worst": 0.1477,
  "concavity_worst": 0.149,
  "concave_points_worst": 0.09815,
  "symmetry_worst": 0.2804,
  "fractal_dimension_worst": 0.08024
}

data3 = { # Malignant
  "radius_mean": 15.46,
  "texture_mean": 23.95,
  "perimeter_mean": 103.8,
  "area_mean": 731.3,
  "smoothness_mean": 0.1183,
  "compactness_mean": 0.187,
  "concavity_mean": 0.203,
  "concave_points_mean": 0.0852,
  "symmetry_mean": 0.1807,
  "fractal_dimension_mean": 0.07083,
  "radius_se": 0.3331,
  "texture_se": 1.961,
  "perimeter_se": 2.937,
  "area_se": 32.52,
  "smoothness_se": 0.009538,
  "compactness_se": 0.0494,
  "concavity_se": 0.06019,
  "concave_points_se": 0.02041,
  "symmetry_se": 0.02105,
  "fractal_dimension_se": 0.006,
  "radius_worst": 17.11,
  "texture_worst": 36.33,
  "perimeter_worst": 117.7,
  "area_worst": 909.4,
  "smoothness_worst": 0.1732,
  "compactness_worst": 0.4967,
  "concavity_worst": 0.5911,
  "concave_points_worst": 0.2163,
  "symmetry_worst": 0.3013,
  "fractal_dimension_worst": 0.1067
}

data4 = { # Benign
  "radius_mean": 12.07,
  "texture_mean": 13.44,
  "perimeter_mean": 77.83,
  "area_mean": 445.2,
  "smoothness_mean": 0.11,
  "compactness_mean": 0.09009,
  "concavity_mean": 0.03781,
  "concave_points_mean": 0.02798,
  "symmetry_mean": 0.1657,
  "fractal_dimension_mean": 0.06608,
  "radius_se": 0.2513,
  "texture_se": 0.504,
  "perimeter_se": 1.714,
  "area_se": 18.54,
  "smoothness_se": 0.007327,
  "compactness_se": 0.01153,
  "concavity_se": 0.01798,
  "concave_points_se": 0.007986,
  "symmetry_se": 0.01962,
  "fractal_dimension_se": 0.002234,
  "radius_worst": 13.45,
  "texture_worst": 15.77,
  "perimeter_worst": 86.92,
  "area_worst": 549.9,
  "smoothness_worst": 0.1521,
  "compactness_worst": 0.1632,
  "concavity_worst": 0.1622,
  "concave_points_worst": 0.07393,
  "symmetry_worst": 0.2781,
  "fractal_dimension_worst": 0.08052
}

data5 = { # Malignant
  "radius_mean": 16.6,
  "texture_mean": 28.08,
  "perimeter_mean": 108.3,
  "area_mean": 858.1,
  "smoothness_mean": 0.08455,
  "compactness_mean": 0.1023,
  "concavity_mean": 0.09251,
  "concave_points_mean": 0.05302,
  "symmetry_mean": 0.159,
  "fractal_dimension_mean": 0.05648,
  "radius_se": 0.4564,
  "texture_se": 1.075,
  "perimeter_se": 3.425,
  "area_se": 48.55,
  "smoothness_se": 0.005903,
  "compactness_se": 0.03731,
  "concavity_se": 0.0473,
  "concave_points_se": 0.01557,
  "symmetry_se": 0.01318,
  "fractal_dimension_se": 0.003892,
  "radius_worst": 18.98,
  "texture_worst": 34.12,
  "perimeter_worst": 126.7,
  "area_worst": 1124,
  "smoothness_worst": 0.1139,
  "compactness_worst": 0.3094,
  "concavity_worst": 0.3403,
  "concave_points_worst": 0.1418,
  "symmetry_worst": 0.2218,
  "fractal_dimension_worst": 0.0782
}

data6 = { # All values 0
    "radius_mean": 0,
    "texture_mean": 0,
    "perimeter_mean": 0,
    "area_mean": 0,
    "smoothness_mean": 0,
    "compactness_mean": 0,
    "concavity_mean": 0,
    "concave_points_mean": 0,
    "symmetry_mean": 0,
    "fractal_dimension_mean": 0,
    "radius_se": 0,
    "texture_se": 0,
    "perimeter_se": 0,
    "area_se": 0,
    "smoothness_se": 0,
    "compactness_se": 0,
    "concavity_se": 0,
    "concave_points_se": 0,
    "symmetry_se": 0,
    "fractal_dimension_se": 0,
    "radius_worst": 0,
    "texture_worst": 0,
    "perimeter_worst": 0,
    "area_worst": 0,
    "smoothness_worst": 0,
    "compactness_worst": 0,
    "concavity_worst": 0,
    "concave_points_worst": 0,
    "symmetry_worst": 0,
    "fractal_dimension_worst": 0
}

datas = [data1, data2, data3, data4, data5, data6]

for i, data in enumerate(datas):
    try:
        response = requests.post(url, json=data)

        if response.status_code == 200:
            print(f"Data - {i+1}: {response.json()}")

        else:
            print(f"Error - {i+1}: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error - {i+1}: {e}")
