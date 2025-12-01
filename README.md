# wellness-suite

High level overview:

1. Track: Concierge Agents

2. Problem and solution pitch: Hiring a personal trainer, let alone a suite of experts dedicated to improving one's wellness, is expensive both monetarily and in terms of time spent interacting with said experts. We built an agentic wellness suite of agents (e.g. fitness trainer agent, nutritionist agent, etc.) to help users achieve better wellness outcomes.

3. Published: https://github.com/alexduh/FitnessAgent

4. This agent helped me restart fitness routines and habits I have struggled to maintain since finishing graduate school.

---

Architecture:

The specialist `fitness_trainer_agent` and `nutritionist_agent` agents are run in parallel. Alongside an aggregator agent `aggregator_agent` that is used to combine the fitness and nutritionist advice into a single wellness plan, with a focus on the synergy between fitness and nutrition advice, the parallel agent and aggregator agent are run in sequence via a sequential agent `sequential_wellness` which takes the output from the fitness training and nutritionist agents first, and then uses said output to create an aggregated wellness plan.

The root agent, named the `WellnessCoordinatorAgent`, chooses dynamically when to run this `sequential_wellness` agent, alongside an `intake_agent`, which is used to craft questions to obtain necessary personal information pertinent to customizing the user's wellness plans. 