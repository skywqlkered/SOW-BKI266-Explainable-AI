## 
This project was created by Julian Dinnissen s1135596 for the Explainable AI course.


## Install
To install the necessary files to grade/test this project:
```bash
pip install -r requirements.txt
```

Run the download script, this downloads the dataset and moves it to the current working directory:
```bash
py download_dataset.py
```
Note: If the file moving for whatever reason doesn't come through, the path of the dataset is printed in the console. The folder `network-intrusion-detection` including its content should be moved to the repository folder as seen in the file structure below.
 

-
    - [**network-intrusion-detection**](network-intrusion-detection)
        - [**versions**](network-intrusion-detection/versions)
            - [**1**](network-intrusion-detection/versions/1)
                - [**Test_data.csv**](network-intrusion-detection/versions/1/Test_data.csv)
                - [**Train_data.csv**](network-intrusion-detection/versions/1/Train_data.csv)
    - [**.gitignore**](.gitignore)
    - [**download_dataset.py**](download_dataset.py)
    - [**main.ipynb**](main.ipynb)
    - [**README.md**](README.md)
    - [**requirements.txt**](requirements.txt)


## Execution
When all the libraries and dataset are installed the code can be executed in the notebook. This will preprocess, train and evaluate the model, and will show the results as discussed in the paper.