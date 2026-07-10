import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    if len(sys.argv) != 2:
        sys.exit("Usage: python model.py data/dropshipping.csv")

    evidence, labels = load_data(sys.argv[1])

    X_train, X_test, y_train, y_test = train_test_split(
        evidence,
        labels,
        test_size=TEST_SIZE
    )

    model = train_model(X_train, y_train)

    predictions = model.predict(X_test)

    sensitivity, specificity = evaluate(y_test, predictions)

    print(f"Correct Predictions : {(y_test == predictions).sum()}")
    print(f"Incorrect Predictions : {(y_test != predictions).sum()}")
    print(f"Sensitivity : {100 * sensitivity:.2f}%")
    print(f"Specificity : {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load dropshipping data from a CSV file and return
    (evidence, labels).
    """

    categories = {
        "Electronics": 0,
        "Fashion": 1,
        "Beauty": 2,
        "Home": 3,
        "Sports": 4,
        "Pets": 5
    }

    platforms = {
        "Facebook": 0,
        "Instagram": 1,
        "TikTok": 2,
        "Google": 3,
        "Pinterest": 4
    }

    evidence = []
    labels = []

    with open(filename, newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:

            record = [
                float(row["Price"]),
                int(row["ShippingDays"]),
                float(row["SupplierRating"]),
                int(row["SupplierExperience"]),
                int(row["CustomerReviews"]),
                float(row["RefundRate"]),
                float(row["MarketingBudget"]),
                int(row["DiscountPercent"]),
                categories[row["Category"]],
                platforms[row["Platform"]],
                1 if row["FreeShipping"] == "TRUE" else 0,
                1 if row["ExpressDelivery"] == "TRUE" else 0,
                int(row["StockAvailable"]),
                float(row["ConversionRate"])
            ]

            evidence.append(record)

            labels.append(
                1 if row["HighRating"] == "TRUE" else 0
            )

    return evidence, labels



def train_model(evidence, labels):
    model = KNeighborsClassifier(n_neighbors=1)

    model.fit(evidence, labels)

    return model



def evaluate(labels, predictions):
    true_positive = 0
    positive = 0

    true_negative = 0
    negative = 0

    for actual, predicted in zip(labels, predictions):

        if actual == 1:

            positive += 1

            if predicted == 1:
                true_positive += 1

        else:

            negative += 1

            if predicted == 0:
                true_negative += 1

    sensitivity = true_positive / positive

    specificity = true_negative / negative

    return sensitivity, specificity



if __name__ == "__main__":
    main()
