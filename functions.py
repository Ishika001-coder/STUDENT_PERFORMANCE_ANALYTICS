def calculate_summary(df,subjects):
    df["Total"] = df[subjects].sum(axis = 1)
    df["Average"] = df[subjects].mean(axis = 1)
    return df


def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >=70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def check_result(row, subjects):
    for subject in subjects:
        if row[subject] < 40:
            return "FAIL"
    if row[subjects].mean() < 50:
        return "FAIL"

    return "PASS"
