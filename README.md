#  Deep Research Framework: Plan, Search, Self-Reflect, and Write
 
 - a multi-agent AI framework for conducting deep, high-quality research using a systematic methodology. Inspired by human-like reasoning and self-reflection techniques, the system breaks down complex queries, gathers information from the web, and composes well-cited research reports.

---

##  Key Features

- **Structured Workflow**: Plan → Search → Reflect → Write.
- **Mixture of LLM Agents (MoA)**, each with specialized roles.
- **Summarization & Source Ranking** to manage long content.
- **Self-Reflection Loop** to detect and address knowledge gaps.
- **JSON Extraction** for structured outputs.

---

##  Agent Architecture

| Role            | Description                                                             | Model Used                                            |
|-----------------|-------------------------------------------------------------------------|--------------------------------------------------------|
|  Planner       | Breaks down user input into actionable queries                         | `Qwen/Qwen2.5-72B-Instruct-Turbo`                     |
|  Summarizer    | Summarizes raw web content into concise, relevant extracts             | `meta-llama/Llama-3.3-70B-Instruct-Turbo`            |
|  JSON Extractor| Extracts structured data from summarized content                        | `meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo`       |
|  Report Writer | Writes a well-structured and sourced research report                   | `deepseek-ai/DeepSeek-V3`                |

---

##  Workflow Overview

1. **Planning**
   - Decompose the user query into focused sub-queries.
2. **Searching**
   - Perform web search and collect top results.
3. **Summarizing**
   - Use LLM to reduce content length while preserving meaning.
4. **Ranking**
   - Rank sources by relevance and reliability.
5. **Self-Reflection**
   - Check for knowledge gaps or missing components.
6. **Writing**
   - Aggregate insights into a clean, coherent research report.
  

![67ffdfdcc14446d60a2a9d0e_AD_4nXedElgrxG9r72Qx0ASenFOwpU2sg7AqWXy_tReaAVpxwBM_NtjasugR0jQEkACRBulSdUztfUVACbGsEsQkyh9ESADAsPdu1QQzfRQEDyMK3ph9WUorZNwYLfFMFWS7CYIfVOlg](https://github.com/user-attachments/assets/f561a80d-5e01-49ec-bd18-0a2a747bff69)


##  Example Use Case

**Query**:  
> "What are the five largest companies in the green/renewable energy sector by market capitalization, and what are their current stock prices?"

**Execution Plan**:
1. Planner identifies need to:
   - Search for top green energy companies.
   - Get their market cap and stock price.
2. Sources retrieved, summarized, and ranked.
3. JSON extractor pulls relevant financial data.
4. Writer generates report with citations.

---

##  Strengths

- Modular & extensible agent pipeline
- Accurate source selection
- Robust handling of long-form content
- Reflection-based completeness check

---

##  Future Enhancements

-  **Advanced TTL caching system**
-  **Multi-modal inputs (e.g., charts, infographics)**
-  **Entity-aware citation system**
-  **Enterprise deployment & monitoring tools**
- **Caching Layer**
    - Temporary local cache to avoid repeated web searches.
    - TTL-based refresh system for fresh results in production.

 - **Multi-modal Extension (Planned)**
     - Ability to handle images, charts, and infographics.
---

#  Strategy2: Modular Agent-Based Research Workflow

`strategy2` is a structured, agent-based system for executing iterative and deep research workflows using a combination of modular LLM agents and research tools. This framework emphasizes flexibility, structured outputs, and high-quality synthesis using both open-source and proprietary language models.

---

##  Open-Source Models Used

| Purpose                    | Model Name                                     | Role                                                                 |
|----------------------------|-----------------------------------------------|----------------------------------------------------------------------|
| Function Calling           | `hivata/functionary-small-v3.2-AWQ`           | Selects appropriate tools based on user queries and context         |
| Structured JSON Output     | `AMead10/SuperNova-Medius-AWQ`                | Generates clean, nested JSON from unstructured LLM outputs          |

These models are chosen for their performance, efficiency, and strong prompt adherence in structured automation tasks.

---

##  Agent System Overview

- **Knowledge Gap Agent**  
  Identifies gaps in collected information and suggests additional areas for research.

- **Tool Selector Agent**  
  Determines the appropriate research tools to invoke for filling knowledge gaps.

- **Tool Agents**  
  Specialized modules that perform individual tasks:
  - `Web Search Agent`: Queries the web to find information
  - `Website Crawler Agent`: Extracts and processes content from targeted sites

- **Writer Agent**  
  Synthesizes the information into well-structured, readable research reports.

---

##  Core Components

- **IterativeResearcher**  
  Executes an in-depth iterative research loop on a single topic or question.

- **DeepResearcher**  
  Coordinates multiple IterativeResearchers in parallel with an initial outline and final synthesis step.

- **LLMConfig**  
  Manages and abstracts model usage to support plug-and-play with various models.

---

##  Model Strategy (Proprietary)

We use OpenAI models in strategic roles based on performance and cost benchmarks:

| Task            | Model            | Reason                                                              |
|----------------|------------------|---------------------------------------------------------------------|
| Tool Selection  | `gpt-4o-mini`    | Cost-effective and accurate; performs better than `o3-mini`         |
| Planning        | `o3-mini`        | Strong for multi-step task and long-term planning                   |
| Final Writing   | `gpt-4o`         | High-quality generation and language fluency                        |

---

##  Research Tools

- **Web Search**  
  Interfaces with search engines to retrieve the most relevant information from SERP results.

---

## ⚙️ Customization & Extensibility

- Tool agents are modular and extensible — you can plug in your own web scrapers, knowledge bases, or API wrappers.
- Language models can be swapped easily via `LLMConfig`.


---

# Sample Output

### Deep Research (using DeepResearcher) :
   - [final_report_electric_vehicle_deep.md](https://github.com/abdalrahmenyousifMohamed/DepthScan/blob/main/examples/sample_output/final_report_electric_vehicle_deep.md)
### Simple Research Examples (using IterativeResearcher):
   - [final_report_electric_vehicle_iterative.md](https://github.com/abdalrahmenyousifMohamed/DepthScan/blob/main/examples/sample_output/final_report_electric_vehicle_iterative.md)

## 🏁 Getting Started

To clone and run locally:

```bash
git clone https://github.com/abdalrahmenyousifMohamed/DepthScan.git
cd DepthScan
pip install -r requirements.txt

Then create a .env file with your API keys:

cp .env.example .env
Edit the .env file to add your OpenAI, Serper and other settings as needed, e.g.:

OPENAI_API_KEY=<your_key>
SEARCH_PROVIDER=serper  # or set to openai
SERPER_API_KEY=<your_key>

python iterative_example.py
