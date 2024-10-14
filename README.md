# IGBC green credit-based search
---
Application for a simple interface to search and retrieve information from the IGBC Green New Buildings Rating System guidelines. The green credit metadata enhances the search of the vector database to find relevant information based on user queries efficiently.

## Instructions

- install `requirement.txt`
- To run the app: `streamlit run app.py`
- LLM is not connected to the current implementation, search results are only fetched from the vector database.
- name of the credit(e.g. -Water Efficiency) is attached to the metadata of the corresponding chunk.
- Running the app for the first time might take time since it is creating vector db from the PDF

## Demo

![demo](https://github.com/adhikarinarayan/IGBC_green_credit_search/blob/dbfc0f805c425b552f743c0c8b826d96319aa38c/demo.png)
