__Note:__

Please note that all experiments were carried out within the Mayo Clinic Cloud environment - a HIPAA-compliant, secure platform - in which we can work with patient data. We are unable to provide our patient data, but we do provide detailed explanations of our data formatting and code used for our experiments as well as subsequent performance evaluation metrics and statistics. In order to run the code shared through the following notebooks, you will need to import your own data and manipulate it into the recommended dataframe formats.

__<ins>shared_functions.py</ins>__

This file contains functions for access token creation and large language model (LLM) prompting that are often used throughout the other notebooks in this repository. Because some of this information is specific to the Mayo API, you may want to modify this code to fit your institution's API that allows you to access LLMs in a HIPAA-compliant manner.

__<ins>timing_classification.ipynb</ins>__

This notebook contains the code pipeline for our index metastasis report identification experiment, which yields metastatic timing classification.

__<ins>volume_classification.ipynb</ins>__

This notebook contains the code pipeline for volume classification. We include four experimental frameworks incorporating varying degrees of prompt decomposition (PD): none, low, high, high with rule-based programming (RBP). The collaborative LLM experiments, as explained further in the notebook,  utilized the none PD framework. 

__<ins>performance_metrics_and_statistics.ipynb</ins>__

This notebook contains all formulas and imported packages used for performance metrics and statistical calculations. The usage of each formula as well as each function from imported packages is individually explained. We provide example arrays for volume classification so that this code can be tested.
