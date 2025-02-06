# Blockchain Simulation

## Description
This project is a simple blockchain simulation built using Python and Flask. It implements the core concepts of a blockchain, including blocks, transactions, and mining.

## Technologies Used
- Python
- Flask
- Docker

## Installation Instructions
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd blockchain_simulation
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To run the application using Docker, execute the following command:
```bash
docker-compose up
```
Access the API at `http://localhost:5000/blockchain`.

## API Endpoints
- **GET /blockchain**: Retrieve the current state of the blockchain.
