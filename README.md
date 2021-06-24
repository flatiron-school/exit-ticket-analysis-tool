# Exit Ticket Analysis Tool

This tool is to meant to do some quick/basic analysis of Exit Tickets given to students following data science lectures using [Streamlit](https://streamlit.io).



# Setup

## Formatting the Data

The tool expects a `data` directory with a specific structure to pull in the Exit Ticket data via CSVs.

The data should be organized to look something like this:

```
exit-ticket-analysis-tool/
├─ data/
│  ├─ MMDDYY-region1/
│  │  ├─ Phase1/
│  │  │  ├─ LECTURE_NAME0 Exit Ticket Survery Student Analysis Report.csv
│  │  │  ├─ LECTURE_NAME1 Exit Ticket Survery Student Analysis Report.csv
│  │  ├─ Phase2/
|  |  |  ├─ LECTURE_NAME3 Exit Ticket Survery Student Analysis Report.csv
│  ├─ MMDDYY-region2/
│  │  ├─ Phase1/
│  │  │  ├─ LECTURE_NAME0 Exit Ticket Survery Student Analysis Report.csv
│  │  │  ├─ LECTURE_NAME1 Exit Ticket Survery Student Analysis Report.csv
```

* `MMDDYY-region1/` and `MMDDYY-region2/` directories represent cohort names (so something like `013121-west`). These names will populate the selection options in the tool.
* Inside cohort directories are phase directories like `Phase1` or `Phase2`. These names will populate the selection options in the tool.
* Inside the phase directories are the relevant Exit Ticket CSVs that can be downloaded from Canvas. They come in the form of `<LECTURE_NAME> Exit Ticket Survery Student Analysis Report.csv` where `<LECTURE_NAME>` is the name of the lecture associated with the Exit Ticekt. 
    > Note the tool will populate the name of the lecture by using the first part of the file name before "`Exit Ticket`" part.

> Note that if more files are loaded into the data directory, the tool will need to be reloaded. This can be done simply by refreshing the web page. 

## Activate Environment

The YAML file `exit_tool_env.yml` should contain everything needed to run the tool.

Creating the environment should be as simple as running the following code (assuming `conda` is [installed](https://conda.io/projects/conda/en/latest/user-guide/install/index.html)):

```bash
conda env create --name exit_tool_env --file=exit_tool_env.yml
```

Once the environment has been created with the above command, it can be activated by running the command:

```bash
conda activate exit_tool_env
```

# Usage

To run the tool/app: 

0. First ensure that the `exit_tool_env` environment is activated 
1. Navigate in the terminal to where the `app.py` file resides
2. Run the command `streamlit run app.py`
4. A web address will appear in stdin and a new browswer window will apear with the tool loaded
5. To quit the app, terminate the job process started in the terminal