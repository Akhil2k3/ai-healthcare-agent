# AI Healthcare Agent System

## Overview
This project is a production-ready AI Healthcare Agent that uses Retrieval-Augmented Generation (RAG) to provide grounded, reliable medical information.  
The system combines a vector database, an AI agent workflow, and an automated evaluation framework to ensure response quality and reliability.

## Architecture
- FastAPI backend for API interaction
- RAG pipeline using SentenceTransformers and ChromaDB
- AI agent orchestration using LangChain and LangGraph
- Automated evaluation framework (relevance, faithfulness, confidence, latency)
- Fully Dockerized for production deployment

## System Architecture Flow

User Query  
→ FastAPI Endpoint  
→ Retriever (Vector Database)  
→ Context Injection  
→ LLM-based Healthcare Agent  
→ Evaluation Framework  
→ Final Response + Metrics  

## Tech Stack
- Python 3.10
- FastAPI
- LangChain
- LangGraph
- SentenceTransformers
- ChromaDB
- HuggingFace Transformers (Open-source LLMs)
- Docker

## Deployment

The application is fully containerized using Docker and can be deployed on cloud platforms such as AWS EC2 or ECS without modification.