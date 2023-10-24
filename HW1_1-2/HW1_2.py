{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "toc_visible": true,
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/M2bayati/MachineLearning2023/blob/main/HW1_1-2/HW1_2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Problem 1:** Create a NumPy array of 20 random integers between 1 and 100. Calculate the mean, median, and standard deviation of the array."
      ],
      "metadata": {
        "id": "5jP9Bu4Ysx6g"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "We_SKcMhsxWZ"
      },
      "outputs": [],
      "source": [
        "import numpy as np\n",
        "\n",
        "# Create a NumPy array of 20 random integers between 1 and 100\n",
        "arr1 = np.random.randint(1,101,20)\n",
        "\n",
        "print(\"Array:\",arr1)\n",
        "print(\"The mean of array:\",np.mean(arr1))\n",
        "print(\"The median of array:\",np.median(arr1))\n",
        "print(\"The standard derivation of array:\",np.std(arr1))"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Problem 2:** Create a Pandas DataFrame with three columns - 'Name', 'Age', and 'City' - and at least five rows of data. Perform a basic data exploration by displaying the first 3 rows, the last 2 rows, and a summary of statistics for the 'Age' column."
      ],
      "metadata": {
        "id": "-iiFwoVRs2s-"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "\n",
        "data = {\n",
        "    \"Name\" : [\"Ali\",\"Mohammad\",\"Zahra\",\"Ramin\",\"Habib\",\"Narges\"],\n",
        "    \"Age\" : [24,22,11,16,45,21],\n",
        "    \"City\" : [\"Kerman\",\"Tehran\",\"Isfahan\",\"Hamedan\",\"Shahrekord\",\"Yazd\"]\n",
        "}\n",
        "\n",
        "df = pd.DataFrame(data)\n",
        "\n",
        "print(\"The first 3 rows:\")\n",
        "print(df.head(3))\n",
        "print(\"\\nThe last 2 rows:\")\n",
        "print(df.tail(2))\n",
        "print(\"\\nAge column:\")\n",
        "print(df[\"Age\"])\n",
        "print(\"\\nA summary of statistics for the 'Age' column:\")\n",
        "print(df[\"Age\"].describe())"
      ],
      "metadata": {
        "id": "TreuEe0Us4uO"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Problem 3:** Create a bar chart using Matplotlib to visualize the following data: Monthly sales for a store (January to May). Use appropriate labels and titles for the chart."
      ],
      "metadata": {
        "id": "PNw-Io7Js0-Z"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import matplotlib.pyplot as plt\n",
        "import numpy as np\n",
        "\n",
        "# Create some data\n",
        "labels = [\"January\",\"February\",\"March\",\"April\",\"May\"]\n",
        "values = [5000,5500,8000,6000,7000]\n",
        "\n",
        "# Create a bar plot\n",
        "plt.figure(figsize = (9, 7))\n",
        "plt.bar(labels, values, color = \"blue\")\n",
        "plt.xlabel('Month')\n",
        "plt.ylabel('Monthly sales')\n",
        "plt.title('Bar plot of monthly sales for a store')\n",
        "plt.grid(axis='y', linestyle='--', alpha = 0.6)\n",
        "\n",
        "# Display values on top of bars\n",
        "for i, v in enumerate(values):\n",
        "    plt.text(i, v + 1, str(v), ha = \"center\", va = \"bottom\")\n",
        "\n",
        "# Show the plot\n",
        "plt.show()"
      ],
      "metadata": {
        "id": "0mLs7tD4s9q4"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Problem 4:** Create two NumPy arrays, 'arr1' and 'arr2', both of size 5x5 with random integer values. Perform element-wise addition, subtraction, multiplication, and division between the two arrays."
      ],
      "metadata": {
        "id": "Lj1_pouqtBU1"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "\n",
        "# Create two random 5x5 arrays with integer values between 1 and 10\n",
        "arr1 = np.array(np.random.randint(1,11,[5,5]))\n",
        "arr2 = np.array(np.random.randint(1,11,[5,5]))\n",
        "\n",
        "# addition\n",
        "add = arr1 + arr2\n",
        "\n",
        "# subtraction\n",
        "sub = arr1 - arr2\n",
        "\n",
        "# multiplication\n",
        "mul = arr1 * arr2\n",
        "\n",
        "# division\n",
        "div = arr1/arr2\n",
        "\n",
        "# Print the results\n",
        "print(\"arr1:\\n\", arr1)\n",
        "print(\"arr2:\\n\", arr2)\n",
        "print(\"Element-wise Addition:\\n\", add)\n",
        "print(\"Element-wise Subtraction:\\n\", sub)\n",
        "print(\"Element-wise Multiplication:\\n\", mul)\n",
        "print(\"Element-wise Division:\\n\", div)"
      ],
      "metadata": {
        "id": "gK1BxnVRtA4t"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Problem 5:** Given a Pandas DataFrame with information about employees, filter and display only the employees who are older than 30 years."
      ],
      "metadata": {
        "id": "kii_k_K7tE1S"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "\n",
        "# Create a sample DataFrame\n",
        "data = {\"Name\": [\"Ali\", \"Ehsan\", \"Mohammad\", \"Reza\", \"Narges\"],\n",
        "        'Age': [25, 30, 27, 35, 32]}\n",
        "\n",
        "employee_data = pd.DataFrame(data)\n",
        "\n",
        "# Filter employees older than 30\n",
        "filtered_employees = employee_data[employee_data['Age'] > 30]\n",
        "\n",
        "# display employees older than 30\n",
        "print(filtered_employees)"
      ],
      "metadata": {
        "id": "2tjtwMK5tLkW"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Problem 6:** Create a scatter plot using Matplotlib to visualize a dataset of 100 random (x, y) coordinates. Label the axes appropriately and give the plot a title."
      ],
      "metadata": {
        "id": "nWkeN_kxtNar"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import matplotlib.pyplot as plt\n",
        "import numpy as np\n",
        "\n",
        "# Set a random seed for reproducibility\n",
        "np.random.seed(0)\n",
        "\n",
        "# Generate random (x, y) coordinates\n",
        "x = np.random.rand(100)\n",
        "y = np.random.rand(100)\n",
        "\n",
        "# Create a scatter plot\n",
        "plt.figure(figsize=(8, 6))\n",
        "plt.scatter(x, y, label='Random Data', color='b', marker='o', s=30)\n",
        "plt.xlabel('x-axis')\n",
        "plt.ylabel('y-axis')\n",
        "plt.title('Scatter Plot of Random Data')\n",
        "plt.grid(True)\n",
        "plt.legend()\n",
        "plt.show()"
      ],
      "metadata": {
        "id": "kVctGlqwtSwd"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Problem 7:** Create two NumPy matrices, 'matrix1' (2x3) and 'matrix2' (3x4), with random values. Perform matrix multiplication between the two matrices."
      ],
      "metadata": {
        "id": "ex6ZssoNtUn-"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "\n",
        "# Create two random matrices\n",
        "matrix1 = np.random.rand(2, 3)\n",
        "matrix2 = np.random.rand(3, 4)\n",
        "\n",
        "# Perform matrix multiplication using numpy.dot\n",
        "# result = np.dot(matrix1, matrix2)\n",
        "\n",
        "# Initialize an empty result matrix with appropriate dimensions\n",
        "result = np.zeros((matrix1.shape[0], matrix2.shape[1]))\n",
        "\n",
        "# Perform matrix multiplication with nested for loops\n",
        "for i in range(matrix1.shape[0]):  # Rows of matrix1\n",
        "    for j in range(matrix2.shape[1]):  # Columns of matrix2\n",
        "        for k in range(matrix1.shape[1]):  # Common dimension\n",
        "            result[i, j] += matrix1[i, k] * matrix2[k, j]\n",
        "\n",
        "# Using the @ operator for matrix multiplication\n",
        "# result = matrix1 @ matrix2\n",
        "\n",
        "# Print the result\n",
        "print(\"Matrix 1 (2x3):\")\n",
        "print(matrix1)\n",
        "print(\"\\nMatrix 2 (3x4):\")\n",
        "print(matrix2)\n",
        "print(\"\\nMatrix Multiplication Result (2x4):\")\n",
        "print(result)"
      ],
      "metadata": {
        "id": "HKWDmVICtVuX"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Problem 8:** Given a Pandas DataFrame containing sales data, calculate and display the total sales for each product category."
      ],
      "metadata": {
        "id": "I_A6rPt8tYHF"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "\n",
        "# Create a dictionary to store data\n",
        "data = {\n",
        "    \"Product\": [\"Product A\", \"Product B\", \"Product C\", \"Product D\", \"Product E\", \"Product F\"],\n",
        "    \"Category\": [\"Category 2\", \"Category 3\", \"Category 1\", \"Category 3\", \"Category 2\", \"Category 1\"],\n",
        "    \"Sales\": [110, 190, 150, 320, 250, 370]\n",
        "}\n",
        "\n",
        "sales_df = pd.DataFrame(data)\n",
        "\n",
        "# Calculate total sales for each product category\n",
        "category_sales = sales_df.groupby(\"Category\")[\"Sales\"].sum()\n",
        "\n",
        "print(category_sales)"
      ],
      "metadata": {
        "id": "blNHInhXtbX_"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Problem 9:** Create a line chart using Matplotlib to visualize the population growth of a city over 10 years. Label the axes and provide a title."
      ],
      "metadata": {
        "id": "mtFKN7CStmr5"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import matplotlib.pyplot as plt\n",
        "\n",
        "# data\n",
        "years = [1381, 1382, 1383, 1384, 1385, 1386, 1387, 1388, 1389, 1390]\n",
        "population = [10000, 12000, 12500, 15000, 16500, 18000, 20000, 21000, 22500, 24000]\n",
        "\n",
        "# Create a line chart\n",
        "plt.figure(figsize=(8, 6))\n",
        "plt.plot(years, population, marker='o', linestyle='-')\n",
        "\n",
        "# Add labels and title\n",
        "plt.xlabel(\"Year\")\n",
        "plt.ylabel(\"Population\")\n",
        "plt.title(\"City Population Growth Over 10 Years\")\n",
        "plt.grid(True)\n",
        "plt.show()"
      ],
      "metadata": {
        "id": "-_O7t-titn_I"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Problem 10:** Given a Pandas DataFrame containing information about students, add a new column 'Grade' based on the following criteria:\n",
        "* If 'Score' >= 90, Grade is 'A'\n",
        "* If 'Score' >= 80, Grade is 'B'\n",
        "* If 'Score' >= 70, Grade is 'C'\n",
        "* If 'Score' < 70, Grade is 'D'"
      ],
      "metadata": {
        "id": "nPWzdcGFtrHS"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "\n",
        "# DataFrame\n",
        "data = {\n",
        "    \"Student_ID\": [1, 2, 3, 4, 5],\n",
        "    \"Name\": [\"Ali\", \"Babak\", \"Narges\", \"Zahra\", \"Amin\"],\n",
        "    \"Score\": [85, 72, 94, 60, 78]\n",
        "}\n",
        "\n",
        "student_df = pd.DataFrame(data)\n",
        "\n",
        "# Define a function to determine the grade\n",
        "def grade(score):\n",
        "    if score >= 90:\n",
        "        return \"A\"\n",
        "    elif score >= 80:\n",
        "        return \"B\"\n",
        "    elif score >= 70:\n",
        "        return \"C\"\n",
        "    else:\n",
        "        return \"D\"\n",
        "\n",
        "# Use grade function to create the 'Grade' column\n",
        "student_df[\"Grade\"] = student_df['Score'].apply(grade)\n",
        "\n",
        "# Display the DataFrame with the new 'Grade' column\n",
        "print(student_df)"
      ],
      "metadata": {
        "id": "L4cEUfKAtz_D"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Problem 11:** You are given a dataset containing monthly sales data for three products (A, B, and C) over a two-year period. Your task is to perform various data analysis tasks using NumPy, Pandas, and Matplotlib.\n",
        "\n",
        "\n",
        "*   Dataset:\n",
        "\n",
        "```\n",
        "import pandas as pd\n",
        "\n",
        "data = {\n",
        "    'Month': pd.date_range(start='2021-01-01', periods=24, freq='M'),\n",
        "    'Product A Sales': [500, 480, 600, 750, 900, 850, 920, 1100, 1300, 1350, 1500, 1450, 1550, 1600, 1650, 1600, 1500, 1400, 1600, 1700, 1800, 1750, 1850, 1900],\n",
        "    'Product B Sales': [300, 320, 400, 450, 500, 580, 700, 750, 820, 900, 950, 980, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1500, 1600, 1550, 1700],\n",
        "    'Product C Sales': [200, 210, 250, 280, 320, 350, 380, 400, 420, 440, 460, 480, 500, 520, 540, 560, 580, 600, 620, 640, 660, 680, 700, 720]\n",
        "}\n",
        "\n",
        "sales_df = pd.DataFrame(data)\n",
        "```\n",
        "*  Tasks:\n",
        "1. Calculate and display the total sales for each product over the two-year period.\n",
        "\n",
        "2. Calculate and display the average monthly sales for each product.\n",
        "\n",
        "3. Find the month with the highest sales for each product, and display the product and the sales value for that month.\n",
        "\n",
        "4. Calculate and display the percentage change in sales for each product from January to December in the second year (2022).\n",
        "\n",
        "5. Create a line chart using Matplotlib to visualize the monthly sales data for each product over the two-year period. Label the axes and provide a title for the chart.\n",
        "\n",
        "6. Calculate the correlation between Product A and Product B sales. Is there a strong correlation between these two products? Display the correlation coefficient.\n"
      ],
      "metadata": {
        "id": "ghA9GbcCuZIs"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "# Define the dataset\n",
        "data = {\n",
        "    'Month': pd.date_range(start='2021-01-01', periods=24, freq='M'),\n",
        "    'Product A Sales': [500, 480, 600, 750, 900, 850, 920, 1100, 1300, 1350, 1500, 1450, 1550, 1600, 1650, 1600, 1500, 1400, 1600, 1700, 1800, 1750, 1850, 1900],\n",
        "    'Product B Sales': [300, 320, 400, 450, 500, 580, 700, 750, 820, 900, 950, 980, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1500, 1600, 1550, 1700],\n",
        "    'Product C Sales': [200, 210, 250, 280, 320, 350, 380, 400, 420, 440, 460, 480, 500, 520, 540, 560, 580, 600, 620, 640, 660, 680, 700, 720]\n",
        "}\n",
        "\n",
        "sales_df = pd.DataFrame(data)\n",
        "\n",
        "# Task 1: Total sales for each product over the two-year period\n",
        "total_sales = sales_df.sum()\n",
        "print(\"Total Sales for Each Product:\")\n",
        "print(total_sales[['Product A Sales', 'Product B Sales', 'Product C Sales']])\n",
        "\n",
        "# Task 2: Average monthly sales for each product\n",
        "average_sales = sales_df[['Product A Sales', 'Product B Sales', 'Product C Sales']].mean()\n",
        "print(\"\\nAverage Monthly Sales for Each Product:\")\n",
        "print(average_sales)\n",
        "\n",
        "# Task 3: Month with the highest sales for each product\n",
        "max_sales_month = sales_df[['Product A Sales', 'Product B Sales', 'Product C Sales']].idxmax()\n",
        "max_sales_value = sales_df[['Product A Sales', 'Product B Sales', 'Product C Sales']].max()\n",
        "print(\"\\nMonth with the Highest Sales for Each Product:\")\n",
        "for product, month_index, sales in zip(max_sales_month.index, max_sales_month, max_sales_value):\n",
        "    month = sales_df.loc[month_index, 'Month']\n",
        "    print(f\"{product}: {month.strftime('%B %Y')}, Sales: {sales}\")\n",
        "\n",
        "\n",
        "# Task 4: Percentage change in sales from January to December in the second year (2022)\n",
        "sales_jan_2022 = sales_df.loc[12, ['Product A Sales', 'Product B Sales', 'Product C Sales']]\n",
        "sales_dec_2022 = sales_df.loc[23, ['Product A Sales', 'Product B Sales', 'Product C Sales']]\n",
        "percentage_change = ((sales_dec_2022 - sales_jan_2022) / sales_jan_2022) * 100\n",
        "print(\"\\nPercentage Change in Sales from January to December in 2022:\")\n",
        "print(percentage_change)\n",
        "\n",
        "# Task 5: Line chart to visualize monthly sales data\n",
        "plt.figure(figsize=(12, 6))\n",
        "\n",
        "for product in ['Product A Sales', 'Product B Sales', 'Product C Sales']:\n",
        "    plt.plot(sales_df['Month'], sales_df[product], label=product)\n",
        "\n",
        "plt.xlabel(\"Month\")\n",
        "plt.ylabel(\"Sales\")\n",
        "plt.title(\"Monthly Sales Data for Each Product (2021-2023)\")\n",
        "plt.legend()\n",
        "plt.grid(True)\n",
        "\n",
        "plt.show()\n",
        "\n",
        "# Task 6: Correlation between Product A and Product B sales\n",
        "correlation = sales_df['Product A Sales'].corr(sales_df['Product B Sales'])\n",
        "print(\"\\nCorrelation between Product A and Product B Sales:\")\n",
        "print(f\"Correlation Coefficient: {correlation:.2f}\")\n",
        "\n",
        "if abs(correlation) >= 0.7:\n",
        "    print(\"There is a strong correlation between Product A and Product B sales.\")\n",
        "else:\n",
        "    print(\"There is no strong correlation between Product A and Product B sales.\")"
      ],
      "metadata": {
        "id": "9NOWYCddvHyY"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}