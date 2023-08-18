import os
from pandas import read_csv, DataFrame
import json

def all_filepaths(root):

    path_lists = []
    for path, subdirs, files in os.walk(root):
        for name in files:
            path_lists.append(os.path.join(path, name).replace('\\', '/'))  # .replace('\\', '"/"')

    return path_lists

def get_initial_idx(img_paths, df_paths):

    if(len(df_paths)==0):
        return 0
    else:
        return img_paths.index(df_paths[-1])

def csv_to_jason(csv_path):

    df = read_csv(csv_path)

    paths = df.path.tolist()
    labels = df.label.tolist()

    IDs, Dates, img_names = [], [], []
    for path in paths:
        IDs.append(path.split('/')[-3])
        Dates.append(path.split('/')[-2])
        img_names.append(path.split('/')[-1])

    df = DataFrame({'ID':IDs, 'Date':Dates, 'Img_name':img_names, 'Label':labels})

    ID_set = set(IDs)

    output_data = []
    for id in ID_set:
        ID_df = df[df.ID==id]
        date_set = set(ID_df.Date)
        for date in date_set:
            ID_Date_df = ID_df[ID_df.Date==date]
            right_names = ID_Date_df[ID_Date_df.Label == 'right'].Img_name.tolist()
            left_names = ID_Date_df[ID_Date_df.Label == 'left'].Img_name.tolist()

            data_item = {
                            "ID": id,
                            "ScanDate": date,
                            "L-Picture": left_names,
                            "R-Picture": right_names
                        }
            output_data.append(data_item)

    csv_name = csv_path.split('\\')[-1]
    output_file = csv_path.replace(csv_name, 'label.json')
    with open(output_file, 'w') as json_file:
        json.dump(output_data, json_file, indent=4)


def main():

    # dir_path = r'C:\Learning\GUI_practice\open_file'
    
    # print(all_filepaths(dir_path))
    # print(len(all_filepaths(dir_path)))

    csv_to_jason(r'C:\Learning\GUI_practice\a.csv')

if __name__ == '__main__':
    main()