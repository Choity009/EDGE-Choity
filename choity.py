def sub_index_ph(ph):
    """ Calculate sub-index for pH. """
    if 6.5 <= ph <= 8.5:
        return 100  # Excellent
    elif 6.0 <= ph < 6.5 or 8.5 < ph <= 9.0:
        return 80  # Good
    else:
        return 50  # Poor

def sub_index_do(do):
    """ Calculate sub-index for Dissolved Oxygen (DO). """
    if do >= 8:
        return 100  # Excellent
    elif 5 <= do < 8:
        return 75  # Good
    else:
        return 50  # Poor

def sub_index_turbidity(turbidity):
    """ Calculate sub-index for Turbidity. """
    if turbidity <= 5:
        return 100  # Excellent
    elif 5 < turbidity <= 10:
        return 75  # Good
    else:
        return 50  # Poor

def sub_index_tds(tds):
    """ Calculate sub-index for Total Dissolved Solids (TDS). """
    if tds <= 300:
        return 100  # Excellent
    elif 300 < tds <= 600:
        return 75  # Good
    else:
        return 50  # Poor

def calculate_wqi(ph, do, turbidity, tds):
    """ Calculate the overall Water Quality Index (WQI). """
    score_ph = sub_index_ph(ph)
    score_do = sub_index_do(do)
    score_turbidity = sub_index_turbidity(turbidity)
    score_tds = sub_index_tds(tds)

    # Weighting the scores for different parameters (optional)
    wqi = (0.25 * score_ph) + (0.25 * score_do) + (0.25 * score_turbidity) + (0.25 * score_tds)
    return wqi

# Sample input values based on your query
ph_values = [4.1, 6.7, 8.2]
do_values = [10.6, 11.7, 4.4]
turbidity_values = [14.0, 6.1, 3.6]
tds_values = [260.5, 1530.5, 2030.0]

# Calculate WQI for each set of values
wqi_values = []
for i in range(len(ph_values)):
    wqi = calculate_wqi(ph_values[i], do_values[i], turbidity_values[i], tds_values[i])
    wqi_values.append(wqi)

# Print the calculated WQI for each input set
for i, wqi in enumerate(wqi_values):
    print(f"Calculated Water Quality Index (WQI) for sample {i + 1}: {wqi:.2f}")

# WQI Interpretation for each sample
for i, wqi in enumerate(wqi_values):
    if wqi >= 80:
        print(f"Sample {i + 1}: Water quality is Excellent.")
    elif 60 <= wqi < 80:
        print(f"Sample {i + 1}: Water quality is Good.")
    elif 40 <= wqi < 60:
        print(f"Sample {i + 1}: Water quality is Fair.")
    else:
        print(f"Sample {i + 1}: Water quality is Poor.")

