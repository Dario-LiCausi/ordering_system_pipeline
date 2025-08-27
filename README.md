# Café Management CLI App

## Project Description  

This project was developed individually during the Generation UK Data Engineering bootcamp, with the first 6 weeks fully dedicated to building it step by step. Each week introduced new topics in class, and I extended the project to put them into practice.  

It began as a simple command line menu and grew into a complete café management system with its own pipeline. The CLI works as the entry point, guiding the user through sub menus to manage products, couriers, and orders. Data evolved from in memory lists, to persistence in CSV files, and finally to PostgreSQL tables running in Docker with Adminer.  

By the final stage I had:  
- Designed **schemas** in SQL with primary and foreign keys for products, couriers, orders, and order status  
- Implemented **Python database modules** to handle queries and data operations  
- Built **CRUD logic** across all entities with validation and error handling in the CLI  
- Used **Docker and docker compose.yml** to containerise the app and manage the database environment  
- Linked **CSV files** and **SQL tables** in a hybrid persistence layer before moving fully to relational storage  

The project shows the progression from a prototype to a structured and containerised data system, applying the core concepts of object oriented programming, relational database design, and modular pipelines.  

---

## Tech Stack  

- **Python** – CLI logic, object oriented modules, database manager  
- **PostgreSQL** – schemas, keys, queries  
- **Docker and docker compose** – containerisation and orchestration  
- **Adminer** – database inspection  
- **CSV and TXT files** – early persistence stages  