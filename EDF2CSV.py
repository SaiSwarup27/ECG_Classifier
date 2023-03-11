import pyedflib
import numpy as np
from os import listdir


def all_edf_files(path):
    """
    Return a list of files with edf suffix under path
    :param path: the path to find all edf files
    :return: a list of all edf files under path
    """
    return [i for i in listdir(path) if i.endswith('.edf')]


def convert_edf_to_txt(path):
    """
    Convert one edf file to a csv file
    :param path: the edf file path
    :return: none - create a csv file with the same name as edf file
    """
    print("start converting " + path)
    # get edf reader
    f = pyedflib.EdfReader(path)
    # get signals in the file
    n = f.signals_in_file
    # get labels: channels from BrainAmp
    labels = f.getSignalLabels()
    # create data dict
    data_dict = dict()
    sigbufs = np.zeros((1, f.getNSamples()[0]))
    for i in np.arange(1):
        sigbufs[i, :] = f.readSignal(i)
        data_dict[str(labels[i])] = sigbufs[i]
    # create new txt file
    ff = open(path[:-4] + '.csv', 'w')
    # write header
    ff.write(','.join(data_dict.keys()) + '\n')
    # write data
    data_lst = zip(*[data_dict[i] for i in data_dict.keys()])
    for i in data_lst:
        data = [str(d) for d in i]
        ff.write(','.join(data) + '\n')
    ff.close()
    print("done")

if __name__ == '__main__':
    path="ADD_PATH_HERE" #Add the edf file path here to convert into csv
    convert_edf_to_txt(path)
