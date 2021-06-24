# Exit Ticket Analysis Tool

This tool is to meant to do some quick/basic analysis of Exit Tickets given to students following data science lectures using [Streamlit](https://streamlit.io).


# Setup

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