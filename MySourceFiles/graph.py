def visualize_days():

    data_file = parse(MY_FILE, ",")

    counter = Counter(item["dayOfWeek"] for item in data_file)

    data_list=[

         counter["Monday"],
         counter["Tuesday"],
         counter["Wednesday"],
         counter["Thursday"],
         counter["Friday"],
         counter["Saturday"],
         counter["Sunday"]

     ]

    day_tuple = tuple(["Mon", "Tues","Wed", "Thurs"])
    plt.plot(data_list)

    # Assign labels to the plot
    plt.xticks(range(len(day_tuple)), day_tuple)

    # Save the plot!
    plt.savefig("Days.png")

    # Close figure
    plt.clf()