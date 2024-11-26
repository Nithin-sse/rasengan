import math

def calculate_entropy(data, target_attr):
    values = [row[target_attr] for row in data]
    value_counts = {v: values.count(v) for v in set(values)}
    total = len(values)
    return -sum((count / total) * math.log2(count / total) for count in value_counts.values())

def information_gain(data, attr, target_attr):
    total_entropy = calculate_entropy(data, target_attr)
    values = [row[attr] for row in data]
    value_counts = {v: values.count(v) for v in set(values)}
    weighted_entropy = sum(
        (count / len(data)) * calculate_entropy(
            [row for row in data if row[attr] == value], target_attr
        )
        for value, count in value_counts.items()
    )
    return total_entropy - weighted_entropy

def build_tree(data, features, target_attr):
    target_values = [row[target_attr] for row in data]
    if len(set(target_values)) == 1:
        return target_values[0]  # All samples have the same target
    if not features:
        return max(set(target_values), key=target_values.count)  # Majority class
    
    gains = {attr: information_gain(data, attr, target_attr) for attr in features}
    best_attr = max(gains, key=gains.get)
    tree = {best_attr: {}}
    
    for value in set(row[best_attr] for row in data):
        subset = [row for row in data if row[best_attr] == value]
        if not subset:
            tree[best_attr][value] = max(set(target_values), key=target_values.count)
        else:
            tree[best_attr][value] = build_tree(
                subset, [f for f in features if f != best_attr], target_attr
            )
    return tree

def predict(tree, sample):
    if not isinstance(tree, dict):
        return tree  # Leaf node
    attr = next(iter(tree))
    value = sample.get(attr)
    return predict(tree[attr].get(value, None), sample) if value in tree[attr] else None

# Input features and dataset
features = input("Enter features (comma-separated): ").split(',')
target = input("Enter target label: ")
n = int(input("Enter number of data entries: "))

data = []
print("Enter data row-wise (comma-separated values including target):")
for _ in range(n):
    row = input().split(',')
    data.append({features[i]: row[i] for i in range(len(features))} | {target: row[-1]})

# Build decision tree
tree = build_tree(data, features, target)
print("\nDecision Tree:", tree)

# Prediction
while True:
    test = input("\nEnter test data (comma-separated, matching features) or 'exit' to quit: ").split(',')
    if test == ['exit']:
        break
    if len(test) != len(features):
        print("Error: Test data does not match the number of features. Try again.")
        continue
    test_sample = {features[i]: test[i] for i in range(len(features))}
    result = predict(tree, test_sample)
    print("Prediction:", result if result else "Unable to classify")
 
