curl -X POST -H "Content-Type: application/json" \
     -d '{"batchId": "10001", "data": [
         {
             "prompt": "[INST] Natalia sold clips to 48 of her friends in April, and then she sold half as many clips in May. How many clips did Natalia sell altogether in April and May? [/INST]",
             "adapter_id": "vineetsharma/qlora-adapter-Mistral-7B-Instruct-v0.1-gsm8k",
             "max_new_tokens": 64
         },
         {
             "prompt": "[INST] Write a SQL query to answer the question based on the table schema.\n\n context: CREATE TABLE table_name_74 (icao VARCHAR, airport VARCHAR)\n\n question: Name the ICAO for lilongwe international airport [/INST]",
             "adapter_id": "ai2sql/ai2sql_mistral_7b",
             "max_new_tokens": 128
         },
         {
             "prompt": "[INST] What is the capital of France? Provide a brief history. [/INST]",
             "adapter_id": "vineetsharma/qlora-adapter-Mistral-7B-Instruct-v0.1-gsm8k",
             "max_new_tokens": 128
         },
         {
             "prompt": "[INST] Write a SQL query to find the names of all employees who have been at the company for more than 5 years.\n\n context: CREATE TABLE employees (id INT, name VARCHAR, hire_date DATE) [/INST]",
             "adapter_id": "ai2sql/ai2sql_mistral_7b",
             "max_new_tokens": 128
         },
         {
             "prompt": "[INST] Explain the theory of relativity in simple terms. [/INST]",
             "adapter_id": "vineetsharma/qlora-adapter-Mistral-7B-Instruct-v0.1-gsm8k",
             "max_new_tokens": 128
         },
         {
             "prompt": "[INST] Write a SQL query to list all the orders with a total amount greater than $1000.\n\n context: CREATE TABLE orders (order_id INT, total_amount DECIMAL) [/INST]",
             "adapter_id": "ai2sql/ai2sql_mistral_7b",
             "max_new_tokens": 128
         },
         {
             "prompt": "[INST] Describe the process of photosynthesis. [/INST]",
             "adapter_id": "vineetsharma/qlora-adapter-Mistral-7B-Instruct-v0.1-gsm8k",
             "max_new_tokens": 128
         },
         {
             "prompt": "[INST] Write a SQL query to find the average salary of employees in each department.\n\n context: CREATE TABLE employees (id INT, name VARCHAR, department_id INT, salary DECIMAL) [/INST]",
             "adapter_id": "ai2sql/ai2sql_mistral_7b",
             "max_new_tokens": 128
         },
         {
             "prompt": "[INST] Summarize the main events of World War II. [/INST]",
             "adapter_id": "vineetsharma/qlora-adapter-Mistral-7B-Instruct-v0.1-gsm8k",
             "max_new_tokens": 128
         },
         {
             "prompt": "[INST] Write a SQL query to delete duplicate rows from a table.\n\n context: CREATE TABLE users (id INT, name VARCHAR, email VARCHAR) [/INST]",
             "adapter_id": "ai2sql/ai2sql_mistral_7b",
             "max_new_tokens": 128
         }
     ]}' \
     http://localhost:5001/lorax/upload