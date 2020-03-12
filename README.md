# Colorful Extended Cleanup World (CECW)

## Introduction
As the name suggests, the Colorful Extended Cleanup World (CECW) dataset is a color-extended version of the Cleanup World (CW) borrowed from the mobile-manipulation robot domain [(MacGlashan et al., 2015)](./reference/Grounding_English_Commands_to_Reward_Functions.pdf). CW refers to a world equipped with a movable object as well as four rooms in four colors, including "blue," "green," "red," and "yellow," which is designed as a simulation environment where the agent can act based on the instructions received [(Gopalan et al., 2018)](./reference/Sequence-to-Sequence_Language_Grounding_of_Non-Markovian_Task_Specifications.pdf). CW obeys a particular Geometric Linear Temporal Logic (GLTL) to parse commands by grammatical syntax, resulting in a total of 3382 commands reflecting 39 GLTL expressions. In addition, commands can be represented in textual expressions as shown in the table.

|                       Command                       | Textual Expression |
|:----------------------------------------------------|:-------------------|
|                  go to the red room                 | F R                |
| go to the red room and then go to the blue room     | F & R F B          |
| go to red room but do not enter yellow room         | & F R G ! Y        |
| go through the red or blue room to the yellow room  | F &丨R B F Y       |
| push the chair from the red room into the blue room | F & R F X          |
| go to the red room move chair to the green room     | F & R F Z          |

The task in CW can be formatted as a supervised semantic parsing problem to translate commands (e.g., "go to the red room") to their textual expressions (e.g., "F R"). In this repository, we show how CECW is generated on the basis of CW in detail. I hope the publication of the CECW dataset can promote the research in related fields, as well as yours.

## Directory
+ **CW** - the folder contains the original CW dataset
+ **train_test_split.ipynb** - the main process to generate CECW from CW
+ **pp_data.ipynb** - the data preprocessing to generate 6 subsets from CECW so as to investigate synonymous generalization
+ **train_src.txt** - CECW source data for training
+ **train_tar.txt** - CECW target data for training
+ **test_src.txt** - CECW source data for testing
+ **test_tar.txt** - CECW target data for testing
```
CECW
├── ALL
├── B
├── BC
├── BCR
├── BCRY
├── CW
├── Colorless
├── README.md
├── helper_functions.py
├── pp_data.ipynb
├── reference
├── test_src.txt
├── test_tar.txt
├── train_src.txt
├── train_tar.txt
└── train_test_split.ipynb
```
## Dependencies
+ python >= 3.7.6
+ jupyter >= 1.0.0
+ numpy>=1.18.1

## Setup
Please ensure the following packages are already installed. A virtual environment is recommended.
+ Jupyter Notebook (for .ipynb)

```
$ cd CECW/
$ pip install pip --upgrade
$ pip install notebook
$ pip install -r requirements.txt
```
## Run
Simply view _train_test_split.ipynb_ and _pp_data.ipynb_ via jupyter notebook. You can also use _train_src.txt_, _train_tar.txt_, _test_src.txt_, and _test_tar.txt_ directly.

## Authors
* **[Ning Shi](https://mrshininnnnn.github.io/)** - MrShininnnnn@gmail.com

## Reference
1. Squire, S., Tellex, S., Arumugam, D., & Yang, L. Grounding English Commands to Reward Functions.
2. Gopalan, N., Arumugam, D., Wong, L. L., & Tellex, S. (2018). Sequence-to-Sequence Language Grounding of Non-Markovian Task Specifications. In Robotics: Science and Systems.