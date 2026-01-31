# 📄 Technical Report  
## AI Healthcare Agent System

---

## 1. System Architecture

### Overview
The AI Healthcare Agent System is a production-ready Generative AI application designed to provide grounded healthcare-related answers using Retrieval-Augmented Generation (RAG). The system integrates a vector database, an AI agent workflow, and an automated evaluation framework, all exposed via a FastAPI interface and deployed using Docker.

---

### High-Level Architecture Flow

User Query  
→ FastAPI API Endpoint  
→ Retriever (ChromaDB Vector Store)  
→ Relevant Context (Top-K Chunks)  
→ LLM-based Healthcare Agent  
→ Evaluation Framework  
→ Final Answer + Metrics  

---

### Key Components

- **FastAPI**: Handles API requests and responses  
- **RAG Pipeline**: Retrieves relevant context using semantic search  
- **AI Agent**: Generates responses constrained by retrieved context  
- **Evaluation Framework**: Assesses output quality and performance  
- **Docker**: Ensures reproducible and production-ready deployment  

---

## 2. Design Decisions and Rationale

### 2.1 Choice of RAG Architecture
Healthcare information requires accuracy and grounding. Pure LLM generation risks hallucinations, so a Retrieval-Augmented Generation approach was chosen to ensure answers are based on trusted source documents.

**Benefits:**
- Reduced hallucinations  
- Improved factual accuracy  
- Transparent source grounding  

---

### 2.2 Vector Database: ChromaDB
ChromaDB was selected as the vector database due to:
- Lightweight local deployment  
- Easy integration with SentenceTransformers  
- No external cloud cost (important for free-tier constraints)  

---

### 2.3 Embedding Model: SentenceTransformers
The `all-MiniLM-L6-v2` model was used for embeddings because:
- Strong semantic similarity performance  
- Low latency  
- Suitable for CPU-only environments  

---

### 2.4 AI Agent Framework: LangChain + LangGraph
LangChain was used for prompt templating and tool integration, while LangGraph was chosen to manage agent execution flow and state.

**Rationale:**
- Clear separation of agent logic  
- Extensible to multi-agent workflows  
- Explicit control over execution steps  

---

### 2.5 Open-Source LLMs
Open-source HuggingFace models were used instead of paid APIs to:
- Avoid cost constraints  
- Ensure reproducibility  
- Maintain offline deployability  

---

### 2.6 Evaluation Framework
A custom evaluation framework was implemented to measure:
- **Relevance**: Semantic similarity between question and answer  
- **Faithfulness**: Answer alignment with retrieved context  
- **Confidence**: Heuristic score based on response structure  
- **Latency**: End-to-end response time  

This ensures the system is not only functional but measurable and monitorable.

---

### 2.7 Dockerized Deployment
Docker was used to containerize the application to ensure:
- Consistent runtime environment  
- Easy deployment to cloud platforms (AWS EC2/ECS)  
- Simplified dependency management  

---

## 3. Challenges Faced and Solutions

### 3.1 Dependency and Environment Issues
**Challenge:** Managing ML dependencies across environments caused version conflicts.  
**Solution:** Docker was used to lock Python version and dependencies, ensuring consistency.

---

### 3.2 Model Loading Latency
**Challenge:** Initial model loading caused slow startup times.  
**Solution:** Models are loaded once at startup and reused for subsequent requests, reducing per-request latency.

---

### 3.3 Agent Hallucinations
**Challenge:** Early versions of the agent generated information not present in retrieved context.  
**Solution:** Prompt constraints were added to force the agent to rely only on retrieved documents, otherwise respond with “I don’t know”.

---

### 3.4 Vector Store Persistence
**Challenge:** Ensuring vector embeddings persist correctly across runs.  
**Solution:** ChromaDB persistence was configured and ingestion was separated as a one-time process.

---

### 3.5 Evaluation Design
**Challenge:** Designing lightweight evaluation metrics without external APIs.  
**Solution:** Semantic similarity-based scoring was used to approximate relevance and faithfulness efficiently.

---

## 4. Performance Benchmarks

### Test Environment
- **OS:** Windows  
- **CPU:** x64  
- **Deployment:** Docker container  
- **Model Inference:** CPU-based  

---

### Sample Query
> *"What are the symptoms of type 2 diabetes?"*

---

### Observed Metrics (Typical)

| Metric | Value |
|------|------|
| Relevance Score | ~0.70 – 0.80 |
| Faithfulness Score | ~0.55 – 0.75 |
| Confidence Score | ~0.8 – 1.0 |
| Latency | ~10–12 seconds (cold start) |

---

### Notes
- First request latency is higher due to model initialization  
- Subsequent requests are significantly faster  
- Performance is acceptable for a CPU-based, open-source setup  

---

## 5. Conclusion
This project demonstrates an end-to-end, production-ready AI system that combines:
- Retrieval-Augmented Generation  
- AI agent orchestration  
- Automated evaluation  
- API-based interaction  
- Containerized deployment  

The system is cloud-ready, extensible, and designed with reliability and transparency in mind, making it suitable for real-world GenAI applications in sensitive domains such as healthcare.

---

## 6. Future Improvements
- Redis caching for frequent queries  
- Multi-agent architecture (triage + specialist agents)  
- Advanced RAG techniques (hybrid search, re-ranking)  
- Monitoring with LangSmith or Weights & Biases  
- Deployment to AWS ECS with autoscaling  
