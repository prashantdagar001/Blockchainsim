document.getElementById('transactionForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const sender = document.getElementById('sender').value;
    const receiver = document.getElementById('receiver').value;
    const amount = document.getElementById('amount').value;

    // Here you would typically send the transaction to the backend
    console.log(`Transaction: ${sender} -> ${receiver}: ${amount}`);

    // Clear the form
    this.reset();
});

// Function to fetch and display the blockchain
function fetchBlockchain() {
    fetch('http://localhost:5000/blockchain')
        .then(response => response.json())
        .then(data => {
            const blockchainDisplay = document.getElementById('blockchainDisplay');
            blockchainDisplay.textContent = JSON.stringify(data, null, 2);
        })
        .catch(error => console.error('Error fetching blockchain data:', error));
}

// Call the function to fetch the blockchain on page load
fetchBlockchain();
