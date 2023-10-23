import matplotlib.pyplot as plt
import read_data as rd

def grade_histograms(filename):
    '''
    Reads grade data from a file, plots histograms of the grades.
    '''
    # Read the file to get the grades data
    grades = rd.read_grades(filename)

    # Make 4 histograms to display the grades for each assignment
    # Note: this is not the only way to create subplots
    fig, ax = plt.subplots(1, 4)

    # Use a loop to draw all 4 histograms
    for i in range(4):
        # By grade:
        ax[i].hist(grades[:, i], bins=range(0, 101))
        ax[i].set(title=f'Assignment {i+1}', xlabel='Grade')

        # By band:
        #  ax[i].hist(grades[:, i], bins=range(0, 101, 10))
    plt.show()