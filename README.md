# wellness-suite

High level overview:

1. Track: Concierge Agents

2. Problem: Despite the explosion of fitness apps and wearable devices, many people struggle to maintain consistent exercise routines and achieve long-term health coals. Hiring a personal trainer, let alone a suite of experts dedicated to improving one's wellness, is expensive both monetarily and in terms of time spent interacting with said experts. 
Solution: We built an agentic wellness suite of agents (e.g. fitness trainer agent, nutritionist agent, etc.) to help users achieve better wellness outcomes.

3. Published: https://github.com/alexduh/FitnessAgent

4. Our suite of wellness agents can accomplish the functions of personal trainers, nutritionists, and health coaches, but are accessible at all hours, more affordable, and more effective at taking user data and creating personalized plans and feedback.

---

Architecture:

The specialist `fitness_trainer_agent` and `nutritionist_agent` agents are run in parallel. Alongside an aggregator agent `aggregator_agent` that is used to combine the fitness and nutritionist advice into a single wellness plan, with a focus on the synergy between fitness and nutrition advice, the parallel agent and aggregator agent are run in sequence via a sequential agent `sequential_wellness` which takes the output from the fitness training and nutritionist agents first, and then uses said output to create an aggregated wellness plan.

The root agent, named the `WellnessCoordinatorAgent`, chooses dynamically when to run this `sequential_wellness` agent, alongside an `intake_agent`, which is used to craft questions to obtain necessary personal information pertinent to customizing the user's wellness plans. 

---

Setup Instructions:

On Unix / Linux:

1. Insert one's Gemini API key into the `.zshrc` or `.bashrc`, e.g. `export GOOGLE_API_KEY=insert_key_here`.

2. Install the Google ADK package via `pip` by running the following command in a virtual environment: `pip install google-adk`

3. Run the `.ipynb` file cell by cell, waiting for each cell to complete running before running the next. <= CHANGE FILE NAME HERE

On Windows:

1. Add the Gemini API key to the Environment variables (searchable in the control panel).

2. Install the Google ADK package via `pip` by running the following command in a virtual environment: `pip install google-adk`

3. Run the `.ipynb` file cell by cell, waiting for each cell to complete running before running the next. <= CHANGE FILE NAME HERE