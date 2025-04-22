# 📚 Strategy2: Modular Agent-Based Research Workflow

`strategy2` is a structured, agent-based system for executing iterative and deep research workflows using a combination of modular LLM agents and research tools. This framework emphasizes flexibility, structured outputs, and high-quality synthesis using both open-source and proprietary language models.

---

## 🔓 Open-Source Models Used

| Purpose                    | Model Name                                     | Role                                                                 |
|----------------------------|-----------------------------------------------|----------------------------------------------------------------------|
| Function Calling           | `hivata/functionary-small-v3.2-AWQ`           | Selects appropriate tools based on user queries and context         |
| Structured JSON Output     | `AMead10/SuperNova-Medius-AWQ`                | Generates clean, nested JSON from unstructured LLM outputs          |

These models are chosen for their performance, efficiency, and strong prompt adherence in structured automation tasks.

---

## 🧠 Agent System Overview

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

## 🔧 Core Components

- **IterativeResearcher**  
  Executes an in-depth iterative research loop on a single topic or question.

- **DeepResearcher**  
  Coordinates multiple IterativeResearchers in parallel with an initial outline and final synthesis step.

- **LLMConfig**  
  Manages and abstracts model usage to support plug-and-play with various models.

---

## 🧪 Model Strategy (Proprietary)

We use OpenAI models in strategic roles based on performance and cost benchmarks:

| Task            | Model            | Reason                                                              |
|----------------|------------------|---------------------------------------------------------------------|
| Tool Selection  | `gpt-4o-mini`    | Cost-effective and accurate; performs better than `o3-mini`         |
| Planning        | `o3-mini`        | Strong for multi-step task and long-term planning                   |
| Final Writing   | `gpt-4o`         | High-quality generation and language fluency                        |

---

## 🛠️ Research Tools

- **Web Search**  
  Interfaces with search engines to retrieve the most relevant information from SERP results.

---

## ⚙️ Customization & Extensibility

- Tool agents are modular and extensible — you can plug in your own web scrapers, knowledge bases, or API wrappers.
- Language models can be swapped easily via `LLMConfig`.

---

## 💡 Summary

`strategy2` combines the power of open-source LLMs, modular agent architecture, and structured workflows to automate research with high accuracy and speed. It’s ideal for generating reliable, well-structured insights across domains.

---

> 💬 *"Open-source flexibility meets enterprise-level research automation in strategy2."*
