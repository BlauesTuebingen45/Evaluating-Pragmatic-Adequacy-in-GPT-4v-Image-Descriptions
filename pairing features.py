# written by Christian Gerber and Ayodeji Olupinla

import random
from PIL import Image, ImageDraw
import pandas as pd
from tabulate import tabulate

# defined ground truths
ground_truths = {
    "1": {"shape": "pill", "color": "red", "scale": "large", "wall": "cyan", "floor": "orange",
          "orientation": "left corner"},
    "2": {"shape": "cylinder", "color": "orange", "scale": "gigantic", "wall": "cyan", "floor": "pink",
          "orientation": "left corner"},
    "3": {"shape": "ball", "color": "green", "scale": "gigantic", "wall": "red", "floor": "pink",
          "orientation": "middle"},
    "4": {"shape": "ball", "color": "light green", "scale": "tiny", "wall": "yellow", "floor": "pink",
          "orientation": "left corner"},
    "5": {"shape": "pill", "color": "red", "scale": "middle-sized", "wall": "yellow", "floor": "cyan",
          "orientation": "middle"},
    "6": {"shape": "cylinder", "color": "medium blue", "scale": "gigantic", "wall": "green", "floor": "yellow",
          "orientation": "middle"},
    "7": {"shape": "pill", "color": "green", "scale": "middle-sized", "wall": "cyan", "floor": "red",
          "orientation": "middle"},
    "8": {"shape": "cylinder", "color": "medium blue", "scale": "gigantic", "wall": "red", "floor": "light green",
          "orientation": "middle"},
    "9": {"shape": "ball", "color": "purple", "scale": "gigantic", "wall": "orange", "floor": "pink",
          "orientation": "left corner"},
    "10": {"shape": "pill", "color": "red", "scale": "large", "wall": "cyan", "floor": "light green",
           "orientation": "middle"},
    "11": {"shape": "block", "color": "green", "scale": "big", "wall": "yellow", "floor": "purple",
           "orientation": "left corner"},
    "12": {"shape": "ball", "color": "orange", "scale": "gigantic", "wall": "light green", "floor": "orange",
           "orientation": "middle"},
    "13": {"shape": "cylinder", "color": "light green", "scale": "large", "wall": "purple", "floor": "purple",
           "orientation": "right corner"},
    "14": {"shape": "pill", "color": "medium blue", "scale": "medium-sized", "wall": "pink", "floor": "cyan",
           "orientation": "middle"},
    "15": {"shape": "pill", "color": "light green", "scale": "small", "wall": "purple", "floor": "light green",
           "orientation": "middle"},
    "16": {"shape": "cylinder", "color": "orange", "scale": "tiny", "wall": "pink", "floor": "medium blue",
           "orientation": "right corner"},
    "17": {"shape": "pill", "color": "pink", "scale": "big", "wall": "orange", "floor": "yellow",
           "orientation": "right corner"},
    "18": {"shape": "block", "color": "cyan", "scale": "small", "wall": "medium blue", "floor": "purple",
           "orientation": "left corner"},
    "19": {"shape": "pill", "color": "dark blue", "scale": "huge", "wall": "red", "floor": "medium blue",
           "orientation": "middle"},
    "20": {"shape": "block", "color": "medium blue", "scale": "gigantic", "wall": "red", "floor": "orange",
           "orientation": "middle"},
    "21": {"shape": "cylinder", "color": "pink", "scale": "gigantic", "wall": "medium blue", "floor": "purple",
           "orientation": "middle"},
    "22": {"shape": "pill", "color": "red", "scale": "medium-sized", "wall": "light green", "floor": "green",
           "orientation": "middle"},
    "23": {"shape": "pill", "color": "purple", "scale": "medium-sized", "wall": "yellow", "floor": "red",
           "orientation": "right corner"},
    "24": {"shape": "ball", "color": "dark blue", "scale": "medium-sized", "wall": "pink", "floor": "medium blue",
           "orientation": "middle"},
    "25": {"shape": "pill", "color": "yellow", "scale": "gigantic", "wall": "cyan", "floor": "red",
           "orientation": "middle"},
    "26": {"shape": "ball", "color": "yellow", "scale": "tiny", "wall": "medium blue", "floor": "orange",
           "orientation": "left corner"},
    "27": {"shape": "block", "color": "purple", "scale": "large", "wall": "green", "floor": "orange",
           "orientation": "right corner"},
    "28": {"shape": "cylinder", "color": "dark blue", "scale": "big", "wall": "orange", "floor": "medium blue",
           "orientation": "middle"},
    "29": {"shape": "pill", "color": "purple", "scale": "small", "wall": "pink", "floor": "pink",
           "orientation": "right corner"},
    "30": {"shape": "block", "color": "light green", "scale": "medium-sized", "wall": "orange", "floor": "light green",
           "orientation": "right corner"},
    "31": {"shape": "block", "color": "light green", "scale": "medium-sized", "wall": "orange", "floor": "light green",
           "orientation": "right corner"},
    "32": {"shape": "ball", "color": "medium blue", "scale": "gigantic", "wall": "pink", "floor": "yellow",
           "orientation": "middle"},
    "33": {"shape": "pill", "color": "pink", "scale": "large", "wall": "orange", "floor": "light green",
           "orientation": "left corner"},
    "34": {"shape": "ball", "color": "dark blue", "scale": "medium-sized", "wall": "yellow", "floor": "pink",
           "orientation": "right corner"},
    "35": {"shape": "ball", "color": "medium blue", "scale": "medium-sized", "wall": "cyan", "floor": "cyan",
           "orientation": "left corner"},
    "36": {"shape": "ball", "color": "cyan", "scale": "tiny", "wall": "light green", "floor": "medium blue",
           "orientation": "right corner"},
    "37": {"shape": "ball", "color": "medium blue", "scale": "large", "wall": "orange", "floor": "cyan",
           "orientation": "middle"},
    "38": {"shape": "cylinder", "color": "yellow", "scale": "tiny", "wall": "green", "floor": "light green",
           "orientation": "middle"},
    "39": {"shape": "ball", "color": "medium blue", "scale": "huge", "wall": "purple", "floor": "red",
           "orientation": "left corner"},
    "40": {"shape": "ball", "color": "medium blue", "scale": "big", "wall": "purple", "floor": "light green",
           "orientation": "right corner"},
    "41": {"shape": "pill", "color": "orange", "scale": "gigantic", "wall": "purple", "floor": "red",
           "orientation": "middle"},
    "42": {"shape": "pill", "color": "orange", "scale": "gigantic", "wall": "red", "floor": "red",
           "orientation": "left corner"},
    "43": {"shape": "ball", "color": "yellow", "scale": "huge", "wall": "cyan", "floor": "green",
           "orientation": "left corner"},
    "44": {"shape": "block", "color": "cyan", "scale": "medium-sized", "wall": "cyan", "floor": "purple",
           "orientation": "left corner"},
    "45": {"shape": "cylinder", "color": "green", "scale": "medium-sized", "wall": "medium blue",
           "floor": "medium blue",
           "orientation": "left corner"},
    "46": {"shape": "cylinder", "color": "green", "scale": "large", "wall": "pink", "floor": "yellow",
           "orientation": "middle"},
    "47": {"shape": "block", "color": "orange", "scale": "tiny", "wall": "light green", "floor": "pink",
           "orientation": "left corner"},
    "48": {"shape": "pill", "color": "dark blue", "scale": "small", "wall": "yellow", "floor": "red",
           "orientation": "right corner"},
    "49": {"shape": "cylinder", "color": "orange", "scale": "small", "wall": "yellow", "floor": "cyan",
           "orientation": "right corner"},
    "50": {"shape": "ball", "color": "purple", "scale": "gigantic", "wall": "green", "floor": "dark blue",
           "orientation": "middle"}}


def common_features(gt1, gt2):
    """
        Calculate the number of common features between two images.

        Parameters:
        gt1 (dict): The feature set of the first image, where keys are feature names and values are feature values.
        gt2 (dict): The feature set of the second image, where keys are feature names and values are feature values.

        Returns:
        int: The number of common features between the two images.
        """
    return sum(1 for k in gt1 if k in gt2 and gt1[k] == gt2[k])


# Compare each image with every other image
def featured_images(gt1, x):
    """
        This function compares the features of each image in the provided dictionary
        with every other image to find pairs that either have a specified number
        of common features or at least 3 common features, based on the value of 'x'.

        Parameters:
        gt1 (dict): A dictionary where keys are image identifiers and values are their features.
        x (int): The specific number of common features to look for in the image pairs.

        Returns:
        list of tuple: A list of tuples, where each tuple contains a pair of image identifiers
        that meet the criteria.

    """
    paired_images = []
    for img1, features1 in gt1.items():
        for img2, features2 in gt1.items():
            if img1 < img2:  # To avoid duplicate pairs and self-comparison
                similarities = common_features(features1, features2)
                if similarities == x:
                    paired_images.append((img1, img2))
                # If 'x' is 3, pairs with at least 3 common features are included.
                elif x == 3 and similarities >= 3:
                    paired_images.append((img1, img2))

    return paired_images


def random_pairs(gt, x):
    """
        Generate a list of randomly paired images until the specified number of pairs ('x') is reached.

        Parameters:
        gt (dict): A dictionary containing image identifiers as keys.
        x (int): The desired number of image pairs.

        Returns:
        list of list: A list where each element is a pair (list of two elements) of randomly chosen images.
        """
    paired_images_randomly = []
    image_keys = list(gt.keys())
    while len(paired_images_randomly) < x:
        pair = random.sample(image_keys, 2)
        paired_images_randomly.append(pair)

    return paired_images_randomly


# example usage
"""
print(featured_images(ground_truths, 3))
print(random.sample(featured_images(ground_truths, 3), 10))

print(len(featured_images(ground_truths, 3)))


# print(random_pairs(ground_truths, 69))
# print(len(random_pairs(ground_truths, 69)))
"""



def pair_images(image_pairs, line_width=10):
    """
       Pair images together and insert a white line between them for easier distinguishing.

       Parameters:
       image_pairs (list of tuples): A list where each tuple contains two image identifiers to be paired.
       line_width (int, optional): The width of the white line to be drawn between the images. Defaults to 10.

    """
    for pair in image_pairs:
        img1_path = f'images/{pair[0]}_cropped.png'  # Adjust path and file format as needed
        img2_path = f'images/{pair[1]}_cropped.png'  # Adjust path and file format as needed

        # Open the images
        img1 = Image.open(img1_path)
        img2 = Image.open(img2_path)

        # calculate the image demension
        total_width = img1.width + img2.width
        max_height = max(img1.height, img2.height)

        # Creates a new blank image with the correct size
        new_img = Image.new('RGB', (total_width, max_height))

        # Paste the two images into the new image
        new_img.paste(img1, (0, 0))
        new_img.paste(img2, (img1.width, 0))
        # Draws a white line between the two images in order for easier distinction
        draw = ImageDraw.Draw(new_img)
        draw.line([(img1.width, 0), (img1.width, max_height)], fill="white", width=line_width)

        # Save the new image
        new_img_path = f'three_features/{pair[0]}_{pair[1]}.png'  # change here for the output directory
        new_img.save(new_img_path)


# Example usage
# image_pairs = random.sample(featured_images(ground_truths, 3), 10)
# pair_images(image_pairs)


def crop_scale_from_images(image_paths):
    """
        Crop a specific portion from each image in a given list of image paths.

        Parameters:
        image_paths (list of str): A list of file paths to the images that need cropping.

        Returns:
        list of str: A list of file paths to the cropped images.
        """
    cropped_image_paths = []

    for path in image_paths:
        with Image.open(path) as img:
            width, height = img.size
            cropped_img = img.crop((width * 0.1, height * 0.1, width * 0.9, height * 0.9))

            # Save the cropped image
            cropped_path = path.replace(".png", "_cropped.png")
            cropped_img.save(cropped_path)
            cropped_image_paths.append(cropped_path)

    return cropped_image_paths

# Example usage for a dataset:

"""image_paths = [f"images/{i}.png" for i in range(1, 51)]  # 50 images as an example

# Crop the scales from the images
cropped_image_paths = crop_scale_from_images(image_paths)
print(cropped_image_paths)"""


def calculate_metrics(c, k, z):
    """
        This function computes three metrics: discriminativity, relevance, and
        optimal discriminativity, based on the given parameters.

        Parameters:
        c (int): number of contrastive features mentioned in a generated
        caption y
        k (int): the total number of features mentioned in y
        z (int): the ground truth number of contrastive features between the images

        Returns:
        dict: A dictionary containing the calculated metrics.
        """
    d = 1 if c > 0 else 0  # Discriminativity
    r = 1 - (k - c) / (6 - z)  # Relevance
    od = 1 if c == 1 else 0  # Optimal discriminativity

    return {'Discriminativity (d)': d, 'Relevance (r)': r, 'Optimal Discriminativity (od)': od}


def mean_efficiency_for_contrastive_efficiency(caption_result):
    """
       Calculate the mean efficiency for contrastive efficiency from a set of caption results.

       Parameters:
       caption_result (list of dicts): A list of dictionaries, each containing the keys 'c', 'k', and 'z',
                                       which are used for metric calculation.

       Returns:
       float: The mean efficiency calculated from the given caption results. Returns 0 if no valid
              efficiencies are found.

    """
    efficiencies = []
    for result in caption_result:
        metrics = calculate_metrics(result['c'], result['k'], result['z'])
        d = metrics['Discriminativity (d)']
        if d == 1:
            e = 1 if result['k'] == result['c'] == 1 else 1 - (result['c'] - 1) / (result['k'] - 1)
            efficiencies.append(e)
    mean_efficiency = sum(efficiencies) / len(efficiencies) if efficiencies else 0
    return mean_efficiency

# Results for the metrics
one_feature_wgt = [
    {'c': 5, 'k': 5, 'z': 5}, {'c': 4, 'k': 4, 'z': 5}, {'c': 4, 'k': 4, 'z': 5},
    {'c': 3, 'k': 4, 'z': 5}, {'c': 3, 'k': 4, 'z': 5}, {'c': 4, 'k': 4, 'z': 5},
    {'c': 3, 'k': 4, 'z': 5}, {'c': 3, 'k': 4, 'z': 5}, {'c': 3, 'k': 4, 'z': 5},
    {'c': 3, 'k': 4, 'z': 5}
]

one_feature_gt = [
    {'c': 5, 'k': 5, 'z': 5}, {'c': 3, 'k': 3, 'z': 5}, {'c': 5, 'k': 5, 'z': 5},
    {'c': 5, 'k': 6, 'z': 5}, {'c': 5, 'k': 6, 'z': 5}, {'c': 5, 'k': 5, 'z': 5},
    {'c': 5, 'k': 6, 'z': 5}, {'c': 5, 'k': 6, 'z': 5}, {'c': 5, 'k': 6, 'z': 5},
    {'c': 5, 'k': 5, 'z': 5}
]

two_features_wgt = [
    {'c': 2, 'k': 2, 'z': 4}, {'c': 2, 'k': 2, 'z': 4}, {'c': 1, 'k': 2, 'z': 4},
    {'c': 2, 'k': 2, 'z': 4}, {'c': 2, 'k': 2, 'z': 4}, {'c': 2, 'k': 2, 'z': 4},
    {'c': 1, 'k': 2, 'z': 4}, {'c': 1, 'k': 2, 'z': 4}, {'c': 3, 'k': 3, 'z': 4},
    {'c': 2, 'k': 3, 'z': 4}
]

two_features_gt = [
    {'c': 3, 'k': 3, 'z': 4}, {'c': 3, 'k': 3, 'z': 4}, {'c': 3, 'k': 4, 'z': 4},
    {'c': 3, 'k': 4, 'z': 4}, {'c': 3, 'k': 4, 'z': 4}, {'c': 3, 'k': 3, 'z': 4},
    {'c': 2, 'k': 3, 'z': 4}, {'c': 2, 'k': 4, 'z': 4}, {'c': 2, 'k': 3, 'z': 4},
    {'c': 2, 'k': 3, 'z': 4}
]

three_features_wgt = [
    {'c': 1, 'k': 2, 'z': 2}, {'c': 2, 'k': 3, 'z': 3}, {'c': 1, 'k': 1, 'z': 2},
    {'c': 1, 'k': 2, 'z': 3}, {'c': 1, 'k': 2, 'z': 3}, {'c': 2, 'k': 3, 'z': 3},
    {'c': 3, 'k': 5, 'z': 3}, {'c': 2, 'k': 4, 'z': 3}, {'c': 2, 'k': 4, 'z': 3},
    {'c': 3, 'k': 4, 'z': 3}
]

three_features_gt = [
    {'c': 2, 'k': 3, 'z': 2}, {'c': 2, 'k': 2, 'z': 3}, {'c': 2, 'k': 3, 'z': 2},
    {'c': 2, 'k': 3, 'z': 3}, {'c': 3, 'k': 4, 'z': 3}, {'c': 2, 'k': 5, 'z': 3},
    {'c': 3, 'k': 5, 'z': 3}, {'c': 3, 'k': 5, 'z': 3}, {'c': 3, 'k': 5, 'z': 3},
    {'c': 3, 'k': 5, 'z': 3}
]

"""# Calculate the mean efficiency
mean_efficiency = "{:.4f}".format(mean_efficiency_for_contrastive_efficiency(one_feature_wgt))
print(str(mean_efficiency) + " one_wgt")

mean_efficiency = "{:.4f}".format(mean_efficiency_for_contrastive_efficiency(one_feature_gt))
print(str(mean_efficiency) + " one_gt")

mean_efficiency = "{:.4f}".format(mean_efficiency_for_contrastive_efficiency(two_features_wgt))
print(str(mean_efficiency) + " two_wgt")

mean_efficiency = "{:.4f}".format(mean_efficiency_for_contrastive_efficiency(two_features_gt))
print(str(mean_efficiency) + " two_gt")

mean_efficiency = "{:.4f}".format(mean_efficiency_for_contrastive_efficiency(three_features_wgt))
print(str(mean_efficiency) + " three_wg")

mean_efficiency = "{:.4f}".format(mean_efficiency_for_contrastive_efficiency(three_features_gt))
print(str(mean_efficiency) + " three_gt")
"""

# data for the metrics
results_by_feature_count_category = {
    'one_feature_wgt': [
        {'c': 5, 'k': 5, 'z': 5}, {'c': 4, 'k': 4, 'z': 5}, {'c': 4, 'k': 4, 'z': 5},
        {'c': 3, 'k': 4, 'z': 5}, {'c': 3, 'k': 4, 'z': 5}, {'c': 4, 'k': 4, 'z': 5},
        {'c': 3, 'k': 4, 'z': 5}, {'c': 3, 'k': 4, 'z': 5}, {'c': 3, 'k': 4, 'z': 5},
        {'c': 3, 'k': 4, 'z': 5}
    ],

    'one_feature_gt': [
        {'c': 5, 'k': 5, 'z': 5}, {'c': 3, 'k': 3, 'z': 5}, {'c': 5, 'k': 5, 'z': 5},
        {'c': 5, 'k': 6, 'z': 5}, {'c': 5, 'k': 6, 'z': 5}, {'c': 5, 'k': 5, 'z': 5},
        {'c': 5, 'k': 6, 'z': 5}, {'c': 5, 'k': 6, 'z': 5}, {'c': 5, 'k': 6, 'z': 5},
        {'c': 5, 'k': 5, 'z': 5}
    ],

    'two_features_wgt': [
        {'c': 2, 'k': 2, 'z': 4}, {'c': 2, 'k': 2, 'z': 4}, {'c': 1, 'k': 2, 'z': 4},
        {'c': 2, 'k': 2, 'z': 4}, {'c': 2, 'k': 2, 'z': 4}, {'c': 2, 'k': 2, 'z': 4},
        {'c': 1, 'k': 2, 'z': 4}, {'c': 1, 'k': 2, 'z': 4}, {'c': 3, 'k': 3, 'z': 4},
        {'c': 2, 'k': 3, 'z': 4}
    ],

    'two_features_gt': [
        {'c': 3, 'k': 3, 'z': 4}, {'c': 3, 'k': 3, 'z': 4}, {'c': 3, 'k': 4, 'z': 4},
        {'c': 3, 'k': 4, 'z': 4}, {'c': 3, 'k': 4, 'z': 4}, {'c': 3, 'k': 3, 'z': 4},
        {'c': 2, 'k': 3, 'z': 4}, {'c': 2, 'k': 4, 'z': 4}, {'c': 2, 'k': 3, 'z': 4},
        {'c': 2, 'k': 3, 'z': 4}
    ],

    'three_features_wgt': [
        {'c': 1, 'k': 2, 'z': 2}, {'c': 2, 'k': 3, 'z': 3}, {'c': 1, 'k': 1, 'z': 2},
        {'c': 1, 'k': 2, 'z': 3}, {'c': 1, 'k': 2, 'z': 3}, {'c': 2, 'k': 3, 'z': 3},
        {'c': 3, 'k': 5, 'z': 3}, {'c': 2, 'k': 4, 'z': 3}, {'c': 2, 'k': 4, 'z': 3},
        {'c': 3, 'k': 4, 'z': 3}
    ],
    'three_features_gt': [
        {'c': 2, 'k': 3, 'z': 2}, {'c': 2, 'k': 2, 'z': 3}, {'c': 2, 'k': 3, 'z': 2},
        {'c': 2, 'k': 3, 'z': 3}, {'c': 3, 'k': 4, 'z': 3}, {'c': 2, 'k': 5, 'z': 3},
        {'c': 3, 'k': 5, 'z': 3}, {'c': 3, 'k': 5, 'z': 3}, {'c': 3, 'k': 5, 'z': 3},
        {'c': 3, 'k': 5, 'z': 3}
    ],
}


# Processes the results to calculate average metrics
# Creates a dataframe in order to portray the results
average_results = {}
for category, results in results_by_feature_count_category.items():
    df = pd.DataFrame([calculate_metrics(**result) for result in results])
    average_results[category] = df.mean()

# Creates a DataFrame from the average results
df_scores = pd.DataFrame.from_dict(average_results, orient='index')

# Transposes the DataFrame
df_scores_transposed = df_scores.T

# Names of columns
df_scores_transposed.columns = ['one-feature wgt', 'one-feature gt',
                                'two-features wgt', 'two-features gt',
                                'three-features wgt', 'three-features gt']

# Inserts 'Score' as a column
df_scores_transposed.reset_index(inplace=True)
df_scores_transposed.rename(columns={'index': 'Score'}, inplace=True)

# Display the DataFrame
"""
print(tabulate(df_scores_transposed, headers='keys', tablefmt='psql'))
"""