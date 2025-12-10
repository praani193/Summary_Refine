# Summary Refinement Workflow Engine

## Project Overview
This project is a **FastAPI-based workflow engine** for text summarization and refinement. It allows creating and running summary graphs, refining outputs, and storing results.

---

## Project Structure
Summary_Refine/
│
├── app/
│ ├── engine/
│ │ ├── graph.py
│ │ └── test.py
│ ├── memory/
│ │ ├── graphs.json
│ │ ├── runs.json
│ │ └── memory.py
│ ├── nodes/
│ │ ├── refine_edge.py
│ │ ├── refine_summary.py
│ │ ├── split.py
│ │ ├── summarize.py
│ │ └── test.py
│ └── main.py
├── venv/
├── LICENSE
├── README.md
├── requirements.txt
├── External Libraries/
└── Scratches and Consoles/

yaml
Copy code

---

## Installation

1. Clone the repository:

git clone <your-repo-url>
cd Summary_Refine
Activate the virtual environment:

# Windows
venv\Scripts\activate

Install dependencies:

bash
Copy code
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
Usage
Start the FastAPI server:

bash
Copy code
uvicorn app.main:app --reload
Visit http://127.0.0.1:8000 to see the home endpoint.

API endpoints:

Endpoint	Method	Description
/	GET	Welcome message
/graphs/create	POST	Create a new summary graph
/graphs/{graph_id}/graph_run	POST	Run a specific graph with input payload
/graphs	GET	List all graphs
/graphs/{graph_id}	GET	Get a specific graph
/runs	GET	List all runs
/runs/{run_id}	GET	Get details of a specific run

Notes
graphs.json and runs.json store the state of graphs and runs persistently.

All nodes (split, summarize, refine) are modular functions in app/nodes/.

FastAPI automatically handles input/output validation and API docs at /docs.

Improvements (Future)
Add Pydantic models for structured payload validation.

Add unit tests for graph runs and nodes.

Add authentication for API endpoints.

Enhance refinement algorithms with NLP models.
