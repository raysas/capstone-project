// importing bv brc js client (installed initially using npm install bvbrc-js-client)
const bvbrc = require('bvbrc-js-client');

const client = new BvbrcApiClient();

// function to fetch data
function fetchData(id) {
    const url = `https://www.bv-brc.org/api/sp_gene/${id}`;
    fetch(url)
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error('Error:', error));
    
    // print the data
    console.log(data);
}

// Use the function
fetchData('2e08d6b6-72cc-446a-bf94-b487b7902c55');

